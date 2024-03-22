from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inbox')
def inbox():
    return render_template('inbox.html', messages=None)

@app.route('/squad')
def squad():
    return render_template('squad.html')

@app.route('/tactics')
def tactics():
    return render_template('tactics.html')

@app.route('/squad_planner')
def squad_planner():
    return render_template('squad_planner.html')

# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')
# @app.route('/tactics')
# def tactics():
#     return render_template('tactics.html')

if __name__ == "__main__":
    app.run(debug=True)