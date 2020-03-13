# Revenge of the Pancakes
# see readme for problem and algorithm details

# Get the number of test cases
T = int(input())

for t in range(T):

    # Get the t^th stack of pancakes.
    # Add a face up pancake to the bottom of the stack. See readme for info about why
    S = input() + "+"

    # This boundary count is equivalent to the minimum number of flips needed make the stack all happy face up.
    boundary_count = S.count('+-') + S.count('-+')

    # 
    print(f"Case #{t+1}: {boundary_count}")

