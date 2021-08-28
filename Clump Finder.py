def clumpfinder(geneome, k, l, t):
    #variables to do stuff with
    kmers = [] #list of kmers that form an (L, t) clump in the genome
    tbr = [] #list of kmers that make the clump we wants
    place = 0 #for keeping track of where the window is in the geneome
    end = place + l #end of the window
    
    #generate the kmers we will check for clumps
    for i in range(len(geneome)-k): #we iterate over the geneome upto the kmer length
        if geneome[i:i+k] not in kmers: #if the kmer isn't already a key in the dictionary (meaning it's new, add it
            kmers.append(geneome[i:i+k])
            
    #now that e've generated kmers we can check groups
    if (end <= len(geneome)): #if the window isn't at the end of the geneome then...
        for i in range(len(kmers)): #for the window, check if all the kmers of a given length form clumps for the window
            if (geneome[place:end].count(kmers[i]) == t): #if the count equals the desireded clump level then add the kmer to the list
                if not (kmers[i] in tbr): #make sure the kmer isn't already here
                    tbr.append(kmers[i]) #add the kmer
            #itterate the variables used to keep track of things
            place = place + 1
            end = end + 1
    
    #return the kmers
    return tbr
    
#find of the data we need to run the equation
file = input("Genome file path: ")
k = int(input("k-mer length: "))
l = int(input("length of window: "))
t = int(input("cluseter size: "))
dna = open(file, "r") #open the file so we can use it as txt to iterate
#tbp = clumpfinder(dna.read(), k, l, t) #run the data we jsut got through the algorithm
#print(k +"-mers that form a (" + l + ", " + t + ") clumps are: " + tbp) #return the result
print(clumpfinder(dna.read(), k, l, t))
