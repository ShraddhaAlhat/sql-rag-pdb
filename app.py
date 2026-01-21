from flask import Flask, request, jsonify, render_template, session
import sqlite3, os, re
from groq import Groq
from dotenv import load_dotenv

# ---------------- SETUP ----------------
load_dotenv()

app = Flask(__name__)
app.secret_key = "employee-chatbot-secret"   # REQUIRED for session

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

DB_PATH = "database.db"


# ---------------- UTILS ----------------
def normalize(text):
    return re.sub(r"[^a-z]", "", text.lower())


def detect_intent(query):
    q = query.lower()
    if "salary" in q:
        return "salary"
    if "department" in q:
        return "department"
    if "joining" in q or "date" in q:
        return "joining_date"
    return None


# ---------------- DATABASE ----------------
def read_sql_query(sql):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]


# ---------------- GROQ: NL → SQL ----------------
def get_groq_sql(user_query):
    prompt = f"""
You are an SQL generator.

STRICT RULES:
- Output ONLY one SQL SELECT query
- NO explanation, NO markdown
- Table: employee
- Always select: first_name, middle_name, last_name
- Add salary ONLY if salary is asked
- Add department ONLY if department is asked
- Add joining_date ONLY if joining date is asked

User query:
{user_query}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    for line in response.choices[0].message.content.split("\n"):
        if line.lower().startswith("select"):
            return line.strip()

    return None


# ---------------- GROQ: DATA → NL ----------------
def generate_groq_response(intent, emp):

    prompt = f"""
You are a helpful assistant.

Rules:
- Answer ONLY for the requested intent
- Do NOT include extra fields
- Keep response short and clear

Employee Details:
First Name: {emp['first_name']}
Middle Name: {emp['middle_name']}
Last Name: {emp['last_name']}
Salary: {emp.get('salary')}
Department: {emp.get('department')}
Joining Date: {emp.get('joining_date')}

Intent: {intent}

Generate a natural language response.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()


# ---------------- MAIN HANDLER ----------------
def handle_employee_query(user_query):

    # 🔁 STEP 0: HANDLE FOLLOW-UP CLARIFICATION
    if session.get("awaiting_clarification"):
        clarified = normalize(user_query)
        candidates = session["candidates"]
        intent = session["intent"]

        for emp in candidates:
            full_name = normalize(
                f"{emp['first_name']} {emp['middle_name']} {emp['last_name']}"
            )

            # supports initials like "Suresh K Patil"
            if all(part in full_name for part in clarified.split()):
                session.clear()
                return generate_groq_response(intent, emp)

        return "Please specify the full correct name from the listed employees."


    # 🧠 STEP 1: DETECT INTENT
    intent = detect_intent(user_query)
    if not intent:
        return "Please ask about salary, department, or joining date."


    # 🤖 STEP 2: NL → SQL (Groq)
    sql = get_groq_sql(user_query)
    if not sql:
        return "Sorry, I could not understand your query."


    # 🗄 STEP 3: SQL → DB
    data = read_sql_query(sql)

    if not data:
        return "No employee found."


    # ⚠️ STEP 4: AMBIGUITY HANDLING (Python)
    if len(data) > 1:
        session["awaiting_clarification"] = True
        session["intent"] = intent
        session["candidates"] = data

        names = [
            f"{i+1}. {d['first_name']} {d['middle_name']} {d['last_name']}"
            for i, d in enumerate(data)
        ]

        return (
            "I found multiple employees. Please specify one:\n" +
            "\n".join(names)
        )


    # ✅ STEP 5: SINGLE RESULT → GROQ RESPONSE
    return generate_groq_response(intent, data[0])


# ---------------- ROUTES ----------------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_query = request.json.get("query")
    answer = handle_employee_query(user_query)
    return jsonify({"answer": answer})


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)