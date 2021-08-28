#exercise 1g, hamming distance
#this function assumes the strings are of equal length
def hammingDist(string1, string2):
    dist = 0 #the hamming distance between two strings
    
    for i in range(len(string1)): #iterate over the string
        #print(i, ", ", string1[i], ", ", string2[i]) #debug stuff
        if not string1[i] == string2[i]: #if the characters aren't the same add one to the calculated distance
            #print("ding") #more debugging stuff
            dist = dist + 1

    return dist

#code to run the stuff
str1 = input("first string: ")
str2 = input("second string: ")
print("Hamming distance: ", hammingDist(str1, str2))
