from arithmetic import add, subtract, multiply, divide
from input_functions import get_two_inputs

x, y = get_two_inputs()

print(f"The sum of {x} and {y} is:", add(x, y))
print(f"The difference between {x} and {y} is:", subtract(x, y))
print(f"The product of {x} and {y} is:", multiply(x, y))
print(f"The quotient of {x} divided by {y} is:", divide(x, y))

