def solve(input_str):
    # Parse input and create two lists of numbers
    numbers = [[int(x) for x in line.split()] for line in input_str.strip().splitlines()]
    left, right = zip(*numbers)
    
    # Calculate similarity score: sum of (number * its occurrences in right list)
    return sum(num * right.count(num) for num in left)

if __name__ == "__main__":
    import os
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_path) as f:
        print(f"Total similarity score: {solve(f.read())}")