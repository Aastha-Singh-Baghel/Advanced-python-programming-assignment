# Read data from input file

f = open("input.txt", "r")

lines = f.readlines()

f.close()

# Count number of lines
print("Total number of lines:", len(lines))

# Extract first two lines
first_two = lines[:2]

print("\nFirst two lines:")
for line in first_two:
    print(line, end="")

# Write first two lines into new file
f = open("output.txt", "w")

for line in first_two:
    f.write(line)

f.close()

print("\n\nData written to output.txt")