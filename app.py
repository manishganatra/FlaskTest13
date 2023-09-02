from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello, {name}!'
    return render_template_string('''
        <form method="post">
            Name: <input type="text" name="name">
            <input type="submit">
        </form>
    ''')

if __name__ == '__main__':
    app.run(debug=True)