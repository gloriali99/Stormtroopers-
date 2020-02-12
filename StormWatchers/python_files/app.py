from stormtrooper import StormTrooper

print("Starting application...\n")

my_stormtrooper = StormTrooper()
my_stormtrooper.read_rules("test_files/rules")
my_stormtrooper.read_events("test_files/events", "test_files/event_info")

print("Rules are:")
for rid in my_stormtrooper.rules:
    r = my_stormtrooper.rules[rid]
    print("HERE:", r, "\nRoot:  ", r.get_node('0'))

print("events are:\n\n")
for eid in my_stormtrooper.events:
    e = my_stormtrooper.events[eid]
    print("Event<key:{}>".format(str(e.key)), e.attributes)
    

print("Closing application...")
