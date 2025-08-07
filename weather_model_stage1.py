<<<<<<< HEAD
import math

# Hardcoded example: ax² + bx + c = 0
a = 1
b = -3
c = 2

discriminant = b ** 2 - 4 * a * c

if discriminant >= 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"Roots: {root1}, {root2}")
else:
=======
import math

# Hardcoded example: ax² + bx + c = 0
a = 1
b = -3
c = 2

discriminant = b ** 2 - 4 * a * c

if discriminant >= 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"Roots: {root1}, {root2}")
else:
>>>>>>> 599b308eed2f76126754c2c88d48e11c003eafdc
    print("No real roots")