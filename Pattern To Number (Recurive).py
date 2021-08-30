#recursively convert a pattern of bases to a number
def patternToNumber(pattern):
    if pattern == "":
        return 0
    letter = pattern[-1]
    prefix = pattern[0:len(pattern)-1]
    return 4*patternToNumber(prefix)+toNum(letter)

#simple function to convert base to it' # counterpait for frequency array
def toNum(letter):
    if letter.upper() == "A":
        return 0
    if letter.upper() == "C":
        return 1
    if letter.upper() == "G":
        return 2
    if letter.upper() == "T":
        return 3

#find of the data we need to run the equation
k = input("Base sequences: ")
print(patternToNumber(k))
