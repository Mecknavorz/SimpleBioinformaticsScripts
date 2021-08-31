#recursively convert a number in bae 10 to a pattern of bases (inverse of last problemn)
def numberToPattern(index):
    if index <= 3: #if the only digit remaining is one we can convert to a base just do it
        return toSym(index)
    r = index % 4 #ge the remained of deviding by 4
    letter = toSym(r) #get the letter for the remainder
    preindex = int((index-r)/4) #so we have a whole number when we divide
    return numberToPattern(preindex) + letter #return the string recursively

#simple function to convert base to it' # counterpait for frequency array
def toSym(num):
    if num == 0:
        return "A"
    if num == 1:
        return "C"
    if num == 2:
        return "G"
    if num == 3:
        return "T"

#find of the data we need to run the equation
index = input("Number: ")
print(numberToPattern(int(index)))
