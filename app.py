# python app.py

from flask import Flask, redirect, render_template, request, url_for, jsonify

app = Flask(__name__)

# -----------------------
# Home / Welcome Page
# -----------------------
@app.route("/", methods=["GET"])
def welcome():
    return """
    <h2>Welcome to Flask Tom.</h2>
    <br>
    <h3>Go to this page: <a href='/form'>Form Page</a></h3>
    """

# -----------------------
# Index Page
# -----------------------
@app.route("/index", methods=["GET"])
def index():
    return "<h2>Welcome to Index Page.</h2>"

# -----------------------
# Success Page (float score)
# -----------------------
@app.route('/success/<float:score>')
def success(score):
    return f"""
    <h1>Congratulations! The person has passed.</h1>
    <h2>Score: {score:.2f}</h2>
    <a href='/form'>Go Back to Form</a>
    """

# -----------------------
# Fail Page (float score)
# -----------------------
@app.route('/fail/<float:score>')
def fail(score):
    return f"""
    <h1>Oops! The person has failed.</h1>
    <h2>Score: {score:.2f}</h2>
    <a href='/form'>Go Back to Form</a>
    """

# -----------------------
# Form Page
# -----------------------
@app.route('/form', methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return render_template('form.html')
    else:
        # Get marks from form
        try:
            maths = float(request.form.get('maths', 0))
            science = float(request.form.get('science', 0))
            history = float(request.form.get('history', 0))
        except ValueError:
            return "<h3>Invalid input! Please enter numeric values.</h3><a href='/form'>Try Again</a>"

        average_marks = (maths + science + history) / 3
        res = "success" if average_marks > 50 else "fail"
        return redirect(url_for(res, score=average_marks))

# -----------------------
# API Route
# -----------------------
@app.route('/api', methods=['POST'])
def calculate_sum():
    data = request.get_json()
    a_val = float(data.get('a', 0))
    b_val = float(data.get('b', 0))
    return jsonify({"sum": a_val + b_val})

# -----------------------
# Run Flask App
# -----------------------
if __name__ == "__main__":
    app.run(debug=True)
    
