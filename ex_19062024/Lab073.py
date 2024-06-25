# inner function outer function
# ignore - word new - it is a new function will go away
def outer_function():
    var1 = 30

    # print(var1)
    # 1st call inner function
    def inner_function():
        print(var1)
    inner_function()

# pay attention to indentation
outer_function()
