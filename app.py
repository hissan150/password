from flask import Flask, render_template, request

app = Flask(__name__)

def check_password(password):
    score = 0
    if len(password) >= 8: score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.islower() for c in password): score += 1
    if any(c in "!@#$%^&*()-_=+;:,.<>?" for c in password): score += 1

    if score <= 2:
        return "Weak password 🔴"
    elif score <= 4:
        return "Medium password 🟡"
    else:
        return "Strong password 🟢"

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        password = request.form.get("password")
        result = check_password(password)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)