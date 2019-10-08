#Yue CHEN yc3644

import re

#myfile = open('population_by_state.tsv', 'r')

with open('population_by_state.tsv', 'r') as tsv:
    myfile=[line.strip().split('\n') for line in tsv]
print(myfile)

p1 = re.compile('[^Mi]')   #to match with any phrases starting with Mi
m1 = p1.match(myfile)
print(m1)

p2 = re.compile('[^New\n.*]') # to match anything starting with New and a space and random content after
m2 = p2.match(myfile)
print(m2)

#integrate all the elements into one string
