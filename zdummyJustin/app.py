from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# from flask import Flask, render_template
# app = Flask('Fix Friends Calender')

# app.route('/')
# def home():
#     return render_template('index.html')

# if __name__ == "__main__":
#     app.run()