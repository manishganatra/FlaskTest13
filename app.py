from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        password = request.form['password']
        if password == '1000':
            return redirect(url_for('form'))
    return render_template_string('''
        <form method="post">
            Password: <input type="password" name="password">
            <input type="submit" value="Submit">
        </form>
    ''')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        return f'''
            <h1>Your Submitted Information</h1>
            <p>Name: {name}</p>
            <p>Email: {email}</p>
            <p>Phone: {phone}</p>
        '''
    return render_template_string('''
        <form method="post">
            Name: <input type="text" name="name"><br>
            Email: <input type="email" name="email"><br>
            Phone: <input type="tel" name="phone"><br>
            <input type="submit" value="Submit">
        </form>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
