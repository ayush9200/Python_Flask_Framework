from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/read")
def index():
    return render_template('hello.html')

@app.route("/welcome/<name>")
def welcome_name(name):
    return render_template('welcome.html', name=name)

@app.route("/sum")
def sum():
    a = request.args.get("a")
    b = request.args.get("b")
    c = int(a)+int(b)
    return str(c)

@app.route("/user-data", methods=['POST'])
def user_data():
    if request.method == 'POST':
        first_name = request.form.get("fname")
        last_name = request.form.get("lnm")
        dist = {"fname":first_name, "lname":last_name}
        result = '''
        <h1>First name : {}</h1>
        <h1>Last name : {}</h1>
        '''
    return result.format(first_name, last_name)
    # return dist #return dist as json in response

@app.route("/user")
def create_form():
    return render_template("user.html")

if __name__ == "__main__":
    app.run()