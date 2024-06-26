try:  # try and install binpacking algorithm
    import binpacking
except:
    import os

    os.system("python3 -m pip install binpacking")
    import binpacking

try:
    with open("2020Cuts.csv", "r") as f:
        lines = f.readlines()
        lines.pop(0)  # remove header comment
        lines = [line.strip() for line in lines]  # remove whitespace
        lines = [line.replace(" ", "") for line in lines]  # remove spaces
except:
    print("Error: 2020Cuts.csv not found")
    exit()

# parse csv file
Lengths = []
Quantities = []
Is2020 = []

for line in lines:
    line = line.split(",")

    Lengths.append(float(line[0]))

    try:
        if line[1] == "":
            Quantities.append(1)
        else:
            Quantities.append(int(line[1]))
    except:
        Quantities.append(1)

    try:
        if line[2] == "2040":
            Is2020.append(False)
        else:
            Is2020.append(True)
    except:
        Is2020.append(False)

# display parsed data
print(Lengths, Quantities, Is2020)

# get user input
maxlength = float(input("Stock Material Length: "))

kerf = float(input("Saw Kerf (0 for no material lost in cuts): "))
for i in range(len(Lengths)):
    Lengths[i] += kerf

# sort by type 2020/2040
Smalls = []
for i in range(len(Lengths)):
    if Is2020[i]:
        for j in range(Quantities[i]):
            Smalls.append(Lengths[i])

Larges = []
for i in range(len(Lengths)):
    if not Is2020[i]:
        for j in range(Quantities[i]):
            Larges.append(Lengths[i])

# pack 2020s
bins = binpacking.to_constant_volume(d=Smalls, V_max=maxlength)
for i in range(len(bins)):
    for j in range(len(bins[i])):
        bins[i][j] -= kerf

# print results
print("2020 Packings:")
for i in range(len(bins)):
    print(bins[i])
print(len(bins), " Stock Material Lengths Required")

# pack 2040s
bins2 = binpacking.to_constant_volume(d=Larges, V_max=maxlength)
for i in range(len(bins2)):
    for j in range(len(bins2[i])):
        bins2[i][j] -= kerf

# print results
print("2040 Packings:")
for i in range(len(bins2)):
    print(bins2[i])
print(len(bins2), " Stock Material Lengths Required")

# Save to file
with open("2020CutsOutput.txt", "w") as f:
    f.write("2020 Packings:\n")
    for i in range(len(bins)):
        f.write(str(bins[i]) + "\n")
    f.write(str(len(bins)) + " Stock Material Lengths Required\n\n")
    f.write("2040 Packings:\n")
    for i in range(len(bins2)):
        f.write(str(bins2[i]) + "\n")
    f.write(str(len(bins2)) + " Stock Material Lengths Required\n")
print("Saved to 2020CutsOutput.txt")
