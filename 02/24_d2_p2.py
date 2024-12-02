def is_safe_sequence(levels):
    if len(levels) <= 1:
        return True
        
    differences = [levels[i+1] - levels[i] for i in range(len(levels)-1)]
    all_increasing = all(d > 0 for d in differences)
    all_decreasing = all(d < 0 for d in differences)
    valid_differences = all(1 <= abs(d) <= 3 for d in differences)
    
    return valid_differences and (all_increasing or all_decreasing)

def solve(input_str):
    # Parse input into list of number lists
    reports = [[int(x) for x in line.split()] for line in input_str.strip().splitlines()]
    
    safe_count = 0
    for levels in reports:
        # First check if sequence is safe without removing any numbers
        if is_safe_sequence(levels):
            safe_count += 1
            continue
            
        # Try removing each number one at a time to see if it makes sequence safe
        for i in range(len(levels)):
            test_levels = levels[:i] + levels[i+1:]
            if is_safe_sequence(test_levels):
                safe_count += 1
                break
                
    return safe_count

if __name__ == "__main__":
    import os
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_path) as f:
        print(f"Number of safe reports with Problem Dampener: {solve(f.read())}")
