from flask import Flask, render_template
app = Flask('Fix Friends Calender')

events_all = [
    {
        'todo' : 'travel to maldives',
        'date' : '2020-12-01'
    },
    {
        'todo' : 'eat burgers',
        'date' : '2021-09-07'
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calender')
def calender():
    return render_template('calendar.html',
    events = events_all)


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)