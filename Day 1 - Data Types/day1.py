import sys

# Declare second integer, double, and String variables.
for ind,line in enumerate(sys.stdin):
    if ind == 0:
        i2 = int(line)
    elif ind == 1:
        d2 = float(line)
    elif ind == 2:
        s2 = str(line)

# Read and save an integer, double, and String to your variables.

# Print the sum of both integer variables on a new line.
print(i+i2)

# Print the sum of the double variables on a new line.
print(d+d2)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.

print(s+s2)