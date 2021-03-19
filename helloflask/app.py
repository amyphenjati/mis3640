from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/hello/<name>')
def hello(name=None):
    if name is not None:
        # return f'<h1> hello, {name}!</h1><p>I am excited to learn Flask</p>'
        return render_template("hello.html", name=name)
    return 'Hello, world!'


# # make a route like 'square/<number>' so the webapp will display the sqare of the number

@app.route('/square/<number>')
def square(number):
    output = float(number) ** 2
    return f'the square of {number} is {output}'


if __name__ == "__main__":
    app.run(debug=True)
