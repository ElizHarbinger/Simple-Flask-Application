from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    return render_template('my_home.html', some_var="Hello, world!")


if __name__ == "__main__":
    app.run()
