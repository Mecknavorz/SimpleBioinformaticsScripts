#bioinformatics 1h
#hamming distance calculator from 1g
def hammingDist(string1, string2):
    dist = 0 #the hamming distance between two strings
    for i in range(len(string1)): #iterate over the string
        if not string1[i] == string2[i]: #if the characters aren't the same add one to the calculated distance
            dist = dist + 1
    return dist #return the distance calculated

#aproximate match calculator
#base    - the string w're trying to find aproximate matches for
#geneome - the text we're looking for matches of base in
#d       - the max hamming sitance we'll allow
def aproxMatch(base, geneome, d):
    matches = [] #the array of positions where we find approximate matches
    for i in (range(len(geneome)-len(base))): #iterate through the genome through anypart where we would see the base string
        if hammingDist(base, geneome[i:i+len(base)]) <= d:
            matches.append(i)
    return matches

base = input("Find matches for: ")
text = input("File for genome: ")
dna = open(text, "r") #open the file so we can use it as txt to iterate
dist = int(input("hamming distance: "))
print(aproxMatch(base, dna.read(), dist))
