def uprlwrsum(message):
    a = sum([1 for c in message if c.islower()])
    b = sum([2 for c in message if c.isupper()])
    return a+b
assert uprlwrsum("") == 0, "Empty String"
assert uprlwrsum("A") == 2, "One upper case"
assert uprlwrsum("a") == 1, "One lower case"
assert uprlwrsum("Ac") == 3, "One upper+lower case"
print("All tests pass")
