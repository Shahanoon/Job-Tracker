# 🗂️ Job Application Tracker

A simple full-stack web application to track job applications — built with Python, Flask, and PostgreSQL.

## 🔧 Tech Stack

- **Backend:** Python, Flask
- **Database:** PostgreSQL
- **Frontend:** HTML, Bootstrap 5

## ✨ Features

- Add new job applications
- View all applications in a clean table
- Update application status
- Delete applications

## 🚀 How to Run Locally

1. Clone the repository
```bash
   git clone https://github.com/Shahanoon/Job-Tracker.git
   cd job-tracker
```

2. Create and activate virtual environment
```bash
   python -m venv venv
   venv\Scripts\activate
```

3. Install dependencies
```bash
   pip install -r requirements.txt
```

4. Set up PostgreSQL database
   - Create a database called `jobtracker`
   - Run the following SQL:
```sql
   CREATE TABLE applications (
       id SERIAL PRIMARY KEY,
       company      VARCHAR(100) NOT NULL,
       role         VARCHAR(100) NOT NULL,
       location     VARCHAR(100),
       applied_date DATE DEFAULT CURRENT_DATE,
       status       VARCHAR(50) DEFAULT 'Applied',
       notes        TEXT
   );
```

5. Update `db.py` with your PostgreSQL password

6. Run the app
```bash
   python app.py
```

7. Open browser and go to `http://127.0.0.1:5000`

## 📸 Screenshots

Coming soon!

## 👨‍💻 Author

Built by Shahanoon — BCA Graduate | Aspiring Data Analyst & SOC Analyst