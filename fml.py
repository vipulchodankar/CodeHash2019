# This program (FML) is not named after some fancy computer related acronym
# fml stands for Fuck My Lifehorizontals=[x.strip().split(" ") for x in f.readlines() if x.split[' '][0].strip()=='H']
# because writing this program
# Fucked My life
# Not really, it was a great experience!
# ~Team git_gud (Ashwin, Neil, Vipul)
import time
import copy
import random
with open('InputData/e_shiny_selfies.txt','r') as f: 
    horizontals=[x.strip().split(" ") for x in f.readlines()[1:] if x.split(' ')[0].strip()=='H']
    f.seek(0)
    verticals=[x.strip().split(" ") for x in f.readlines()[1:] if x.split(' ')[0].strip()=='V']
horizontals.sort(key=len)
verticals.sort(key=len)

while len(verticals)>1:
    
    tags=list(set(verticals[-1][2:]).union(set(verticals[-2][2:])))
    horizontals.append([(verticals[-1][0],verticals[-2][0]),len(tags)]+tags)
    print(len(verticals))
    # print(n)
    # print(len(verticals))
    
    del verticals[-2]
    del verticals[-1]
# end=time.time()
# print(str(start-end))
horizontals.sort(key=len)
horizontals.reverse()
slideCount=0
slides=[]
print("HORIZONTALS")
offset=1
print(horizontals[5])

for n in range(len(horizontals)-20) :       
    slideCount=slideCount+1
    slides.append(horizontals[n][0])
    

with open("fmlOutput.out",'w') as f:
    f.write(str(slideCount)+"\n")
    for i in slides:
        if type(i)==type((1,1)):
            f.write(str(i[0])+" "+str(i[1])+"\n")