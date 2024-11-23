from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wall-of-fame')
def wall_of_fame():
    return render_template('wall_of_fame.html')

if __name__ == "__main__":
    app.run(debug=True)