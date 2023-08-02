from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secret key for your application

@app.route('/', methods=['GET', 'POST'])
def form_page():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        session['name'] = name
        session['age'] = age
        return redirect(url_for('result_page'))
    return render_template('form.html')

@app.route('/result')
def result_page():
    name = session.get('name')
    age = session.get('age')
    return render_template('result.html', name=name, age=age)

if __name__ == '__main__':
    app.run(debug=True)
