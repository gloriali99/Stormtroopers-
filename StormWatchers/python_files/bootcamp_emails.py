# coding=utf-8

import smtplib, sys, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import csv
import time
from python_files.kvstore import KVStore
from datetime import datetime
import json
import os

def send_email(to, cc, reply_email, issue_number, rule_id):
    # cwd = os.getcwd()
    # print(cwd)
    message = MIMEMultipart("alternative")
    to_str = ",".join(to)
    cc_str = ",".join(cc)
    all_recipients = to + cc

    # try:
    #     f = open("C:/Users/dstia/OneDrive/Desktop/credentials.json", "r")
    # except OSError:
    #     print("Could not open/read credentials file: credentials.json")
    #     return

    # with f:
    #     credentials = json.load(f)
        # username = credentials["aws_access_key_id"]
        # password = credentials["aws_secret_access_key"]
    username = ""
    password = ""

    sender = "stormtrooper2020labz@gmail.com"
    host = "email-smtp.ap-southeast-2.amazonaws.com"
    port = 587  # innovate wifi

    message["Subject"] = "Email Alert"
    message["From"] = "Stormtroopers <stormtrooper2020labz@gmail.com>"
    message["To"] = to_str
    message["CC"] = cc_str
    message['Reply-to'] = "StormWatch <" + reply_email + ">"
    cwd = os.getcwd()
    # print(cwd)
    # print(\n')
    # Access the event in the kvstore. Uses the format of the issues_detected.json schema
    issues_kv = KVStore(collection="python_files/test_files/issues_detected", key='issue-number') # Calls to Darius' kvstore.py
    issue = issues_kv.get_one(issue_number)

    # Format email content into string for MIMEText input
    html = format_html_generic(issue_number, issue["alert-chain"])

    # Original hardcoded text option:
    text = format_string_generic(issue_number, issue["alert-chain"])

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    message.attach(part1)
    message.attach(part2)

    # Logging in to server and sending email
    server = smtplib.SMTP(host=host, port=port)
    server.ehlo()
    server.starttls()
    server.set_debuglevel(1)
    server.login(username, password)
    server.sendmail(sender, all_recipients, message.as_string())
    server.quit()
    return True


# Currently, only the generic email template exists. With future alerts, different emails will be sent according to the alert type.
def format_string_generic(issue_number, alert_chain):

    alert_strings = []
    for alert in alert_chain:
        metric = ""
        metric_arr = []
        for key in alert:
            if (key == "host" or key == "tier"):
                continue
            elif (key == "severity" or key == "expected_value"):
                metric = "\t\t".join([str(key), str(alert[key])])
                metric_arr.append(metric)
            elif (key == "_time"):
                metric = "\t\t\t".join(["_time", datetime.fromtimestamp(float(alert[key])).strftime("%c")])
                metric_arr.append(metric)
            else:
                metric = "\t\t\t".join([str(key), str(alert[key])])
                metric_arr.append(metric)
        alert_string = "\n".join(metric_arr)
        alert_strings.append(alert_string)

    alerts = "\n\n".join(alert_strings)
    bodytext = ("An alert has been created for event {issue_number}, which is comprised of the following anomalies: \n\n {alerts}")

    return bodytext.format(issue_number=issue_number, alerts=alerts)


def format_html_generic(issue_number, alert_chain):
    # cwd = os.getcwd()
    # print(cwd + '\n')
    table = populate_table(alert_chain)

    try:
        f = open("../templates/email_generic.html", "r")
    except OSError:
        print("Could not open/read email template file: email_generic.html")
        return

    with f:
        htmltext = [line.rstrip('\n') for line in f]
        htmltext = ''.join(htmltext)

    rows = populate_table(alert_chain)

    #TODO: remove control reference from email heading
    return htmltext.format(event_id = issue_number, rows=rows)

def populate_table(alert_chain):

    rows = []

    # decimal places
    for anomaly in alert_chain:
        raw_time = float(anomaly["_time"])
        day = datetime.fromtimestamp(raw_time).strftime("%-d")
        month = datetime.fromtimestamp(raw_time).strftime("%b")
        year = datetime.fromtimestamp(raw_time).strftime("%Y")
        _time = datetime.fromtimestamp(raw_time).strftime("%X")

        date = " ".join([day,month,year])

        row = """<tr class="table">
                    <td class="table">{date}</td>
                    <td class="table">{_time}</td>
                    <td class="table">{metric}</td>
                    <td class="table">{value}</td>
                    <td class="table">{expected_value}</td>
                    <td class="table">{severity}</td>
                </tr>""".format(date = date, _time=_time, metric=anomaly["metric"], value=round(anomaly["value"], 4), expected_value=round(anomaly["expected_value"], 4), severity=round(anomaly["severity"], 4))
        rows.append(row)

    return "".join(rows)

if __name__ == "__main__":
    to = ['stormtrooper2020labz@gmail.com']
    cc = ['stormtrooper2020labz@gmail.com']
    reply_email = 'stormtrooper2020labz@gmail.com'
    issue_number = 3
    send_email(to, cc, reply_email, issue_number)
