# is_float function definition goes here
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
# Do not change the lines below
print(is_float('3.45'))
print(is_float('3e4'))
print(is_float('abc'))
print(is_float('4'))
print(is_float('.5'))