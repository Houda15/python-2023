from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secret key for your application

@app.route('/')
def index():
    session['counter'] = session.get('counter', 0) + 1
    return render_template('index.html', counter=session['counter'], visits=session.get('visits', 0))

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect(url_for('index'))

@app.route('/increment', methods=['POST'])
def increment():
    increment_value = int(request.form.get('increment_value', 1))
    session['counter'] = session.get('counter', 0) + increment_value
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
