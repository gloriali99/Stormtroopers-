from flask import *
# Flask, render_template, json, current_app as app
import sys

sys.path.insert(0, '/the/folder/path/python_files')

from python_files.node_old import *
from python_files.pass_forms_data import *

o1 = OperatorNode('OR')
o2 = OperatorNode('AND')
o2.add_child(ConditionalNode('cpu', '>', '60'))
o2.add_child(ConditionalNode('ram', '>=', '80'))
o2.add_child(ConditionalNode('heat', '>=', '100'))

o1.add_child(ConditionalNode('cpu', '<', '2'))
o1.add_child(o2)

print(o1)

app = Flask(__name__)

# index
@app.route('/', methods=['GET', 'POST'])
def render_static_index():
    return render_template('index.html', num=10)

# another page
@app.route('/tree')
def render_static_tree():
    return render_template('sample_tree.html', o1=o1)

# email page
@app.route('/email')
def render_static_email():
    return render_template('email.html')

# Store json files using this method
@app.route('/form', methods=['GET', 'POST'])
def render_static_form():
    # do stuff when the form is submitted
    if request.method == 'POST':
        condition = request.form['condition']
        number = int(request.form['numberForLoop'])
        print(condition)

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return render_template('index.html', num=number, cond=condition)

    # show the form, it wasn't submitted
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
