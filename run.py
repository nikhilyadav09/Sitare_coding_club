from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wall-of-fame')
def wall_of_fame():
    return render_template('wall_of_fame.html')

@app.route('/join')
def join():
    return render_template('join.html')

@app.route('/event')
def event():
    return render_template('event.html')

if __name__ == "__main__":
    app.run(debug=True)