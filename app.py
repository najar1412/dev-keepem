from flask import Flask, render_template, request
from func import generate_calendar


app = Flask(__name__)

@app.route('/')
def home():
    calendar = generate_calendar()

    return render_template('home.html', calendar=calendar)

@app.route('/updated_calender', methods=['POST'])
def update():
    value = request.form['slider_value']
    calendar = generate_calendar(int(value))

    return render_template('home.html', calendar=calendar, value=value)


if __name__ == '__main__':
    app.run(debug=True)
