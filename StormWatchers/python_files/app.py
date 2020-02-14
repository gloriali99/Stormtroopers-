from stormtrooper import StormTrooper

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

print()
print("Sending emails... not implemented")
# for r in rule_with_issues:
#     rule = my_stormtrooper.rules[r]
#     for issue_number in rule_with_issues[r]:


print("Closing application...")
