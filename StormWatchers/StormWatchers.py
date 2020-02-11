from flask import *
# Flask, render_template, json, current_app as app
import sys

sys.path.insert(0, '/the/folder/path/python_files')

from python_files.node import *
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
@app.route('/')
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

# form page
@app.route('/form', methods=['POST'])
def render_static_forms():
    projectpath = request.form['projectFilepath']
    return render_template('form.html')

if __name__ == '__main__':
    app.run()
