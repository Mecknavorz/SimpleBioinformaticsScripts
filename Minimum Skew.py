import plotly.graph_objects as go #used to make the skew graphs
import numpy as np
np.random.seed(1)

def minskew(geneome):
    skewrec = {} #record of minimum skews found
    rskew = [] #running skew value for graphing
    skew = 0 #the skew
    minskew = 0 #minimum skew found so far
    for i in range(len(geneome)): #itterated through the dna strand
        #increment skew accordingly
        if (geneome[i] == 'G'):
            skew += 1 
        if (geneome[i] == 'C'):
            skew -= 1

        #append the current skew to the graph
        #rskew.append(skew)
        
        #figure out if we're at a minimum
        if skew <= minskew:
            skewrec[i] = skew #add the current skew to the record of skews to use on the graph
            minskew = skew

    #sort out the less that true minimum skews
    for i in list(skewrec):
        if skewrec[i] > minskew: #if the skew isn't the min
            skewrec.pop(i) #remove the skew

    #graph stuff
    '''
    fig = go.Figure() #start the graph
    N = len(geneome) #used to make an x axis that was just counting up because nothing else sseemed to work
    random_x = np.linspace(0, len(geneome), N) #creation of the x axist
    fig.add_trace(go.Scatter(x=random_x,y=rskew, mode='lines', name='lines')) #actually add the line to the graph
    fig.show() #display the graph
    '''
    return skewrec #return the minimums

#find of the data we need to run the equation
file = input("Genome file path: ")
dna = open(file, "r") #open the file so we can use it as txt to iterate
print(minskew(dna.read()))
