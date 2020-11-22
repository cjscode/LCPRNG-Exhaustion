# Initialize Variables
# Seed Value
seed = 0
# m parameter for LCPRNG
m = int(input("Enter an integer m to find suitable a, c values: "))
# Count for recursive breakout
count = 0
# Setup Empty Arrays
m_breakdown = []
random_output = []
sorted_output = []
ac_vals = []
ac_vals_all = []
# Input for search space for A, C Values
search_space = int(input("Enter the number of values to search (n^2): "))
# Generate list of all possible numbers in cycle
for i in range(0, m):
  m_breakdown.append(i)

# Main lcprng
def lcprng(x, count, a, c):
  if count == m:
    sorted_output = sorted(random_output)
    return sorted_output
  else:
    count += 1
    
    result = ((a * x + c) % m)
    # print("X sub ", str(count), ":", str(result))
    random_output.append(result)
    
    return lcprng(result, count, a, c)

# Identify A and C values for a given M
for j in range(0, search_space):
  for k in range(0, search_space):
    to_compare = lcprng(seed, count, j, k)

    if to_compare == m_breakdown:
      # print("FOUND: Valid Values - A: {} and C: {}".format(j, k))
      ac_vals.append(j)
      ac_vals.append(k)
      ac_vals_all.append(list(ac_vals))
      ac_vals = []

      print("FOUND: Valid [a, c] Pair for m =", m, "|", "[{}, {}]".format(j, k))
    else:
      # print("Invalid Combination - A {}),C {}".format(j, k))
      sorted_output = []
      random_output = []

print(ac_vals_all)

