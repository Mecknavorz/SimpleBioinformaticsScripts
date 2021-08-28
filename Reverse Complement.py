#itterate through the strand and switch ever letter with its complement
def compliment(strand):
    nstrand = ''
    for i in strand:
        if i == 'a':
            nstrand += 't'
        elif i == 't':
            nstrand += 'a'
        elif i == 'g':
            nstrand += 'c'
        elif i == 'c':
            nstrand += 'g'
    return nstrand

#reverse the strand order
def reverse(strand):
    rstrand = ''
    for i in reversed(strand):
        rstrand += i
    return rstrand

#take the dna as input
dna = input("enter dna string: ")
#output the orginal strand, and the reverse compliment for comparison
print('your strand:\t\t' + dna)
print('reverse compliment:\t' + reverse(compliment(dna)) + '\n')
