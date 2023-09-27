
# Made by Eric Eaton 9/25/2023

# µVision ARM assembly formatter
# This is extremely helpful to interactively understand how compilers convert c code into assembly.

# Boilerplate: This is free to use and distribute. I am not liable for anything that people do with it. It has no guarentee of working.

# It has been tested on a few functions, but not extensively
# This will convert copied assembly from µVision's Debugger's Disassembly to ARM assembly that can be copied and pasted in a function
# This works for both mixed mode and assembly mode

# To use it:
# 1. In µVision, execute code in the debugger and open the Disassembly to see the assembly code.
# 2. copy and paste one function of assembly code from the Disassembly into a new text file
# 4. run this script and follow the prompts. A text file will be created with the same name as your original file but appended with the suffix "-ARMFormatted".


filename = "test"
labelTag = "testLabel"
ADDRESS = 0
MISC = 1
COMMAND = 2
ARGUMENTS = 3

print("Paste the name of the file you would like to convert. EX: \"filename\" (.txt will automatically be appended)")
filename = input() + ".txt"

print("specify a tag that us unique to this function that will be used to make unique labels")
labelTag = input()

formattedFileSuffix = "-ARMFormatted"

fullText = ""
with open(filename) as f:
    fullText = f.read()
f.close()


lines = fullText.split("\n")
numLines = len(lines)
linesWords = [[""]]*numLines

for i in range(numLines):
    if lines[i][ADDRESS] != '0':
        linesWords[i] = lines[i]
        continue
    linesWords[i] = list(filter(None, lines[i].split(" ")))


labelIndexes = [0]  #dummy first
labelIndexes.clear()

labelNum = 0;
for i in range(numLines):
    if isinstance(linesWords[i], str):
        continue
    for j in range(numLines):
        if isinstance(linesWords[j], str):
            continue
        if len(linesWords[j]) <= ARGUMENTS:
            continue
        if(linesWords[i][ADDRESS] in linesWords[j][ARGUMENTS]):
            labelIndexes.append(j)

    if len(labelIndexes) > 0:
        label = labelTag + str(labelNum)
        labelNum = labelNum+1
        while len(labelIndexes) > 0:
            j = labelIndexes.pop()
            index = linesWords[j][ARGUMENTS].index(linesWords[i][0])
            linesWords[j][ARGUMENTS] = linesWords[j][ARGUMENTS][:index] + label
        linesWords[i][ADDRESS] = label
    else:
        linesWords[i][ADDRESS] = ""
    
for i in range(numLines):
    if isinstance(linesWords[i], str):
        lst = list(linesWords[i])
        lst.insert(0, ";")
        lines[i] = "".join(lst)
        continue
    del linesWords[i][MISC]
    lines[i] = "\t".join(linesWords[i])

fullText = "\n".join(lines)

i = filename.index('.')
filename = filename[:i] + formattedFileSuffix + filename[i:]

with open(filename, "w") as f:
    f.write(fullText)
f.close()

print("\nCreated file: " + filename)