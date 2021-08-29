#compute a frequencey array for kmers
#the frequent words solver I made is already more efficent than it would be with this i belive
#so this is more just for the exercise and in cases I am wrong about the last part anyway lol
#The only reason mine might not be faster would probably be due to look up times but I think this would run into the same issues as my original code
def ComputeFreq(geneome, k):
    freqArray = []
    #initialize the frequency aray to zeros
    for i in range(0, (4**k)):
        freqArray.append(0)
    for i in range(len(geneome)-k):
        pattern = geneome[i:i+k]
        j = patternToNumber(pattern)
        #print("J: %d" %j)
        freqArray[j] += 1
    return freqArray

def patternToNumber(pattern):
    strnum = ""
    for i in pattern:
        strnum += toNum(i) #convert each letter in the pattern to it's number counter
    #print("strnum: %s" % strnum)
    num = int(strnum, 4) #put out converted pattern into a basse 4 int
    #print("num: %d" % num) 
    return num

#simple function to convert base to it' # counterpait for frequency array
def toNum(letter):
    if letter.upper() == "A":
        return "0"
    if letter.upper() == "C":
        return "1"
    if letter.upper() == "G":
        return "2"
    if letter.upper() == "T":
        return "3"

#find of the data we need to run the equation
file = input("Genome file path: ")
dna = open(file, "r") #open the file so we can use it as txt to iterate
k = int(input("kmer length: "))
print(ComputeFreq(dna.read(), k))
