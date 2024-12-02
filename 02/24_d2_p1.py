def solve(input_str):
    # Parse input into list of number lists
    reports = [[int(x) for x in line.split()] for line in input_str.strip().splitlines()]
    
    safe_count = 0
    for levels in reports:
        # Check if levels are strictly increasing or decreasing
        differences = [levels[i+1] - levels[i] for i in range(len(levels)-1)]
        all_increasing = all(d > 0 for d in differences)
        all_decreasing = all(d < 0 for d in differences)
        
        # Check if adjacent differences are between 1 and 3
        valid_differences = all(1 <= abs(d) <= 3 for d in differences)
        
        if valid_differences and (all_increasing or all_decreasing):
            safe_count += 1
            
    return safe_count

if __name__ == "__main__":
    import os
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_path) as f:
        print(f"Number of safe reports: {solve(f.read())}")
