text = ""
file = open("text.txt", "r")
for line in file:
    text += line
file.close()
print(len(text))
