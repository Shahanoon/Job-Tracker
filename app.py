from flask import Flask, render_template, request, redirect, url_for
from db import get_connection

app = Flask(__name__)

# ─── View all applications ───
@app.route("/")
def index():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM applications ORDER BY applied_date DESC;")
    jobs = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", jobs=jobs)

# ─── Add new application ───
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        company = request.form["company"]
        role = request.form["role"]
        location = request.form["location"]
        status = request.form["status"]
        notes = request.form["notes"]
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO applications (company, role, location, status, notes) VALUES (%s, %s, %s, %s, %s);",
            (company, role, location, status, notes)
        )
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for("index"))
    return render_template("add.html")

# ─── Edit application status ───
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    conn = get_connection()
    cur = conn.cursor()
    if request.method == "POST":
        status = request.form["status"]
        notes = request.form["notes"]
        cur.execute(
            "UPDATE applications SET status=%s, notes=%s WHERE id=%s;",
            (status, notes, id)
        )
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for("index"))
    cur.execute("SELECT * FROM applications WHERE id=%s;", (id,))
    job = cur.fetchone()
    cur.close()
    conn.close()
    return render_template("edit.html", job=job)

# ─── Delete application ───
@app.route("/delete/<int:id>")
def delete(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM applications WHERE id=%s;", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)