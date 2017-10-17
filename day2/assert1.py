def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])

assert count_upper_case("") == 0, "Empty String"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("5") == 0, "number as string"
assert count_upper_case("$%^&") == 0, "Only special caracters"
print("All tests pass")


upper 2
lower 1