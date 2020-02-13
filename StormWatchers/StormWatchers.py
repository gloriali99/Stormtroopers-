from flask import *
# Flask, render_template, json, current_app as app

import json
import sys
from python_files.stormtrooper import StormTrooper


sys.path.insert(0, '/the/folder/path/python_files')

# from python_files.node import *
# from python_files.pass_forms_data import *
# from python_files.bootcamp_emails import *


# send_email('stormtrooperlabs2020@gmail.com', 'stormtrooperlabs2020@gmail.com', 'stormtrooperlabs2020@gmail.com', 1)

app = Flask(__name__)

rules_dict = {
    'id': "0"
}

# index
@app.route('/', methods=['GET', 'POST'])
def render_static_index():
    return render_template('index.html', num=10, o1=rules_dict)

# # another page
# @app.route('/tree')
# def render_static_tree():
#     return render_template('sample_tree.html', o1=o1)

# email page
# @app.route('/email')
# def render_static_email():
#     return render_template('email_generic.html')

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




@app.route('/postmethod', methods = ['POST'])
def get_post_javascript_data():
    trooper = StormTrooper()
    jsdata = json.loads(request.form['javascript_data'])
    # trooper.convert_rule_json_js_to_python(jsdata)
    print("JSDATA IS SIS IS SIS S", jsdata)
    return jsdata


if __name__ == '__main__':
    app.run()