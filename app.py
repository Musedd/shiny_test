from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        return render_template_string("<h1>Hello, {{ name }}!</h1>", name=name)
    return '''
        <form method="post">
            Name: <input type="text" name="name">
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)