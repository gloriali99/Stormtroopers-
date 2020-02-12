from stormtrooper import StormTrooper

print("Starting application...\n")

my_stormtrooper = StormTrooper()
my_stormtrooper.read_rules("test_files/rules")

print("Rules are:")
for r in my_stormtrooper.rules:
    print("HERE:", r, "\nRoot:  ", r.get_node('0'))
    

print("Closing application...")
