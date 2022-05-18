#I worked with Andrew Dang

#Leisha (L), Benito (B), Delia (D), Charlotte (C), Weldon (W), Zina (Z)

#Facts about children
#Z < W < D
#L > B && L < D && L < W
#B != Shortest

#Print list of children from tallest to shortest

#True is taller, False is shorter, None is no information given

#L - False, B - True, D - False, W - False
#B - False, 

#Order is L, B, D, C, W, Z


L = [None, True, False, None, False, False]
B = [False, None, False, None, False, False]
D = [True, True, None, None, False, False]
C = [None, None, None, None, None, None]
W = [True, True, True, None, None, False]
Z = [True, True, True, None, True, None]
lists = [L, B, D, C, W, Z]
names = ["Leisha", "Benito", "Delia", "Charlotte", "Weldon", "Zina"]

#Number of children taller than person
counts = [0, 0, 0, 0, 0, 0]

# Print List of Children from Tallest to Shortest

for i in range(6): #goes through lists array
    for a in range(6): #goes through individual child array
        if (lists[i][a] is not None) and (lists[i][a]): #if data isn't none and it's true, add one
            counts[i] = counts[i] + 1

#finds current tallest
def chooseTall(counts):
    tallest = -1
    currentCount = -1
    for child in range(6):
        if counts[child] > currentCount:
            currentCount = counts[child]
            tallest = child
    return tallest

#tracks who is current tallest
tallest = -1
currentCount = -1
tallest = chooseTall(counts)

for x in range(5):
    #print name
    print(f"{names[tallest]}")
    #update count
    counts[tallest] = -1
    #update tallest child
    tallest = chooseTall(counts)


# if currentCount = 0 and hasPrinted[C] is False:
if (names[tallest] == "Benito"):
    print(f"{names[tallest]} {names[3]}")
else:
    print(f"{names[tallest]}")