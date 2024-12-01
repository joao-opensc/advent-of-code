def solve(input_str):
    # Parse input and create two lists of numbers
    numbers = [[int(x) for x in line.split()] for line in input_str.strip().splitlines()]
    left, right = zip(*numbers)
    
    # Calculate total minimum distance by pairing sorted numbers
    return sum(abs(l - r) for l, r in zip(sorted(left), sorted(right)))

if __name__ == "__main__":
    import os
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_path) as f:
        print(f"Total minimum distance: {solve(f.read())}")