text = input("file path to text: ")
pattern = input("Pattern to count: ")
f = open(text, "r")
print(f.read().count(pattern))
