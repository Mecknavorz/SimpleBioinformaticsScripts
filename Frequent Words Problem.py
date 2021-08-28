def frequentWords(text, k):
    kmers = {} #list of kmers to return
    #text = txt.read() #read the thingy
    for i in range(len(text)):
        if i+k < len(text):
            #print(text[i:i+k])
            if text[i:i+k] not in kmers.keys(): #if the kmer isn't already a key in the dictionary (meaning it's new, add it
                kmers[text[i:i+k]] = text.count(text[i:i+k]) #add the count of the kmer in the geneome to the dictionary

    max_value = max(kmers.values())  # maximum value
    max_keys = [k for k, v in kmers.items() if v == max_value]
    print(max_value, max_keys)

#stuff to actually run our function
file = input("Genome file path: ")
k = int(input("k-mer length: "))
dna = open(file, "r") #open the file so we can use it as txt to iterate
frequentWords(dna.read(), k)
