import math

def solve_quadratic(a, b, c, index):
    result = f"\nEquation {index + 1}: a={a}, b={b}, c={c}\n"
    if a == 0:
        result += "Not a quadratic equation (a = 0)"
        return result

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        result += f"Two real and distinct roots: {root1}, {root2}"
    elif discriminant == 0:
        root = -b / (2 * a)
        result += f"One real root: {root}"
    else:
        real = -b / (2 * a)
        imag = math.sqrt(-discriminant) / (2 * a)
        result += f"Complex roots: {real} ± {imag}i"
    return result

try:
    with open("inputs.txt", "r") as file:
        lines = file.readlines()

    output_lines = []

    for i, line in enumerate(lines):
        if line.strip() == "":
            continue  # skip empty lines
        try:
            a, b, c = map(float, line.strip().split())
            result = solve_quadratic(a, b, c, i)
        except ValueError:
            result = f"\nEquation {i + 1}: Invalid input format: {line.strip()}"
        output_lines.append(result)

    # Save results to output.txt
    with open("output.txt", "w") as file:
        file.write("\n".join(output_lines))

    print("✅ Output written to output.txt")

except FileNotFoundError:
    print("❌ Error: inputs.txt file not found.")
