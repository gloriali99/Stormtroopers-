from flask import Flask, render_template

app = Flask(__name__)

# index
@app.route('/')
def render_static_1():
    return render_template('index.html', num=10)

# another page
@app.route('/home')
def render_static_2():
    return render_template('sample_tree.html', num=5)

if __name__ == '__main__':
    app.run()
