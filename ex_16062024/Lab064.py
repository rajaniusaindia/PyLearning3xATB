def make_pizza(*topings):
    print(topings)
    for topin in topings:
        print(topin)

# tupple - immutable ->
t = ("Pramod", "Rajani", "Lucky") # cannot change the value
t[0] = "Amit" # can change the value

pramod = make_pizza("tomato")

