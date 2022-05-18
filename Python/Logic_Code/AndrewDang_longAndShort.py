# Worked together with Elizabeth to codify this logic problem
# 
# Leisha (L), Benito (B), Delia (D) , Charlotte (C), Weldon (W), Zina (Z)

# Facts about children
# D < W < Z
# B < L < D < W
# B != Shortest


# Order is L, B, D, C, W, Z
from cgitb import small
from re import T




# Lists that hold comparisons between the user and others.
# True if user is taller than comparison, False = Shorter, None = no info given
# Order is L, B, D, C, W, Z

l = [None, True, False, None, False, False]
b = [False, None, False, None, False, False]
d = [True, True, None, None, False, False]
c = [None, None, None, None, None, None]
w = [True, True, True, None, None, False]
z = [True, True, True, None, True, None]
lists = [l, b, d, c, w, z]
names = ["Leisha", "Benito", "Delia", "Charlotte", "Weldon", "Zina"]

# Number of children taller then [person]
counts = [ 0, 0, 0, 0, 0, 0]

# Counts number of peers each child is taller than
for child in range(6):
    for a in range(6):
        if (lists[child][a] is not None) and (lists[child][a]):
            counts[child] = counts[child] + 1

# Function for finding the current tallest
def chooseTallest(counts):
    tallestChild = -1
    currentCount = -1
    # Compares if current child has the most number of taller peers
    for child in range(6):
        if counts[child] > currentCount:
            currentCount = counts[child]
            tallestChild = child
    return tallestChild

# Tracks who is the current tallest
tallestChild = -1
currentCount = -1
tallestChild = chooseTallest(counts)

# Print List of Children from Tallest to Shortest
for x in range(5):
    # Print Name
    print(f"{names[tallestChild]} ")
    # Update Count
    counts[tallestChild] = -1
    # Update Tallest Child
    tallestChild = chooseTallest(counts)
       

# Check if Charlotte has not printed yet
if (names[tallestChild] == "Benito"):
    print(f"{names[tallestChild]} {names[3]}")
else:
    print(f"{names[tallestChild]}")
