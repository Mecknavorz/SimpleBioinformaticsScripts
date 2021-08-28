#bioinformatics 1i
#Frequenct words with mismatch

#hamming distance calculator from 1g
def hammingDist(string1, string2):
    dist = 0 #the hamming distance between two strings
    for i in range(len(string1)): #iterate over the string
        if not string1[i] == string2[i]: #if the characters aren't the same add one to the calculated distance
            dist = dist + 1
    return dist #return the distance calculated

#aproximate match calculator from 1h
#base    - the string w're trying to find aproximate matches for
#geneome - the text we're looking for matches of base in
#d       - the max hamming sitance we'll allow
def aproxMatch(base, geneome, d):
    matches = 0 #number of matches found
    for i in (range(len(geneome)-len(base))): #iterate through the genome through anypart where we would see the base string
        if hammingDist(base, geneome[i:i+len(base)]) <= d:
            matches = matches + 1
    return matches

#frequent words alg
def frequentWords(gene, k, d):
    kmers = {} #list of kmers to return
    for i in range(len(gene)-k):
        if gene[i:i+k] not in kmers.keys(): #if the kmer isn't already a key in the dictionary (meaning it's new, add it
            kmers[gene[i:i+k]] = aproxMatch(gene[i:i+k], gene, d) #add the count of the kmer in the geneome to the dictionary

    max_value = max(kmers.values())  # maximum value
    max_keys = [k for k, v in kmers.items() if v == max_value]
    print(max_value, max_keys)

#take inputs and do stuff
file = input("Genome file path: ")
k = int(input("k-mer length: "))
d = int(input("# of max errors: "))
dna = open(file, "r") #open the file so we can use it as txt to iterate
frequentWords(dna.read(), k, d)
