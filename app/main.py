from src.recommendater import Recommendater
from flask import Flask, render_template, request

# cal = Calculator()
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    user_id = 0
    action = ""
    if request.method == "POST":
        user_id = request.form["user_id"]
        action = request.form["action"]

        message = "Welcome " + str(user_id) + ", you clicked button of " + action

    if (action == 'Content based'):
        return render_template("index.html", welcome_message=message, tables=[method2(user_id).to_html(classes='data', header="true")], titles=method2(user_id).columns.values)
    else:
        return render_template("index.html", welcome_message=message, tables=[method1(user_id).to_html(classes='data', header="true")], titles=method1(user_id).columns.values)

def method1(user_id):
    rec = Recommendater(user_id, "Get Default Recommendations")
    return rec.method1(user_id)

def method2(user_id):
    rec = Recommendater(user_id, "Content based")
    return rec.method2(user_id)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)