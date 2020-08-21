# Given an object/dictionary with keys and values that consist of both strings and integers, design an algorithm to calculate and return the sum of all of the numeric values.
# For example, given the following object/dictionary as input:

dict = {"cat": "bob", "dog": 23, 19: 18, 90: "fish"}

variable = 0

for key in dict.values():
    if isinstance(key, int):
        variable += key
print(variable)
