from flask import *
# Flask, render_template, json, current_app as app

import json
import sys
from python_files.stormtrooper import StormTrooper
from python_files.kvstore import KVStore


sys.path.insert(0, '/the/folder/path/python_files')

# from python_files.node import *
# from python_files.pass_forms_data import *
# from python_files.bootcamp_emails import *


# send_email('stormtrooperlabs2020@gmail.com', 'stormtrooperlabs2020@gmail.com', 'stormtrooperlabs2020@gmail.com', 1)

app = Flask(__name__)

my_stormtrooper = StormTrooper()
my_stormtrooper.read_rules("python_files/test_files/rules")  # TODO CHANGE locations
my_stormtrooper.read_events("python_files/test_files/events_short", "python_files/test_files/event_info_short")

rules_dict = {
    'id': "0"
}

# index
@app.route('/', methods=['GET', 'POST'])
def render_static_index():
    trooper = StormTrooper()
    rules_dict = json.dumps((StormTrooper().parse_path_to_list("python_files/test_files/rules", 'id')))

    


    return render_template('index.html', num=10, rules_dict=rules_dict)

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
    jsdata['id'] = jsdata['name']
    path = "python_files/test_files/rules"
    kv = KVStore(path, 'name')
    kv.put_one(jsdata['name'], jsdata)
    kv.post_all()


    return jsdata

@app.route('/getpythondata')
def get_python_data():  # get 
    return json.dumps((StormTrooper().parse_path_to_list("python_files/test_files/rules", 'id')))  # TODO change rules path

@app.route('/trigger_email', methods = ['POST'])
def trigger_email():
    print("Starting application...")

    print("Importing JSONs...\n")
    my_stormtrooper = StormTrooper()
    my_stormtrooper.read_rules("python_files/test_files/rules")
    print("events")
    my_stormtrooper.read_events("python_files/test_files/events_short", "python_files/test_files/event_info_short")

    print("Rules are:")
    for rid in my_stormtrooper.rules:
        r = my_stormtrooper.rules[rid]
        print("Rule {}:  ".format(r.rule_id), r.get_node('0'))

    print("\n")
    print("Events are:")
    for eid in my_stormtrooper.events:
        e = my_stormtrooper.events[eid]
        print("Event {}:".format(str(e.key)), e.attributes)

    print("\n")
    print("EMAILS")
    rule_with_issues = my_stormtrooper.get_rule_to_event_list()
    for r in rule_with_issues:
        rule = my_stormtrooper.rules[r]
        print("Alert for rule {} will be executed with issue numbers:".format(str(r)), rule_with_issues[r])
        print("   Emailed to: ", rule.to)
        print("        CC to: ", rule.cc)
        print("       BCC to: ", rule.bcc)
        print()

    my_stormtrooper.send_emails()
    return {}


if __name__ == '__main__':
    app.run()