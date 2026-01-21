# 🧠 Employee Information Chatbot (LLM + SQL)

A conversational **Employee Information Chatbot** built with **Flask**, **SQLite**, and **Groq LLM**.
The chatbot understands natural language questions about employees, converts them into SQL queries using an LLM, fetches data from a database, and responds in natural language.

It also supports **conversational memory** to handle **ambiguous names** and **follow-up clarifications**.

---

## ✨ Features

* 🔍 Natural Language → SQL using Groq (LLaMA 3.3)
* 🗄 SQLite employee database
* 💬 Conversational flow with memory (Flask sessions)
* ⚠️ Ambiguity handling (multiple employees with same name)
* 🧠 Follow-up clarification support
* 🌐 Simple web-based chat UI

---

## 📂 Project Structure

```
employee-chatbot/
│
├── app.py            # Flask backend + LLM logic
├── init_db.py        # Database initialization script
├── database.db       # SQLite database
├── requirements.txt  # Python dependencies
├── templates/
│   └── index.html    # Chat UI
├── .env              # Environment variables (API key)
└── README.md
```

---

## 🛠 Tech Stack

* **Backend:** Flask (Python)
* **LLM:** Groq – LLaMA 3.3 70B
* **Database:** SQLite
* **Frontend:** HTML + JavaScript
* **Session Memory:** Flask sessions

---

## 📥 Clone the Repository

Clone the project from GitHub using the command below:

```bash
git clone https://github.com/ShraddhaAlhat/sql-rag-pdb.git
```

Navigate into the project directory:

```bash
cd sql-rag-pdb
```

---

## 🔑 Environment Setup

### 1️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🗄 Database Setup

Initialize the SQLite database and seed employee data:

```bash
python init_db.py
```

This will create `database.db` with an `employee` table.

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 💬 Example Conversations

### 🔹 Ambiguous First Name

**User:**

```
What is the salary of Suresh?
```

**Bot:**

```
I found multiple employees. Please specify one:
1. Suresh Naresh Patil
2. Suresh Ganesh Patil
3. Suresh Naresh Patil
```

**User:**

```
I mean Suresh Ganesh Patil
```

**Bot:**

```
The salary of Suresh Ganesh Patil is ₹55,000.
```

---

### 🔹 Unique Name

**User:**

```
What is the department of Naresh Jadhav?
```

**Bot:**

```
Naresh Ashok Jadhav works in the Sales department.
```

---

### 🔹 Last Name Only Query

**User:**

```
What is the joining date of Patil?
```

**Bot:**

```
I found multiple employees. Please specify one:
1. Suresh Naresh Patil
2. Suresh Ganesh Patil
3. Ganesh Prakash Patil
```

---

## 🧠 How It Works (High Level)

1. **User Query** → Intent detection (salary / department / joining date)
2. **LLM (Groq)** converts natural language → SQL
3. **SQLite DB** executes SQL query
4. **Ambiguity Handler** checks multiple matches
5. **Session Memory** stores candidates for follow-up
6. **LLM** generates final natural language response


---

⭐ If you find this project useful, give it a star on GitHub!
