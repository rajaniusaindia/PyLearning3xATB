# use of *args - similar to List containing multiple args

def print_arguments(*args):
    for i in args:
        print(i, end="\n")

#print_arguments():
# *args -> List
a = ["Pramod", "Rajani", "Lucky"]
for i in a:
    print(i)

