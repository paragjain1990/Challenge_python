from itertools import groupby
import sys


data = open(sys.argv[1],"r")
shopList=[]
for line in data:

    line = line.replace(' ', '')
    line =line.replace('\n','')
    line= line.replace('\"','')
    shopDetails=line.split(',')
    shopDetails[0] =int(shopDetails[0])
    shopDetails[1]=float(shopDetails[1])
    shopList.append(shopDetails)
#print shopList
listOfItems=[sys.argv[2],sys.argv[3]]

shopNumbers=[]
for item in listOfItems:
    for shop in shopList:
        if item in shop:
            shopNumbers.append(shop)
shopNumbers.sort()
#print shopNumbers

dict1={}
# {1,{[1, 4.0, 'teddy_bear'], [1, 8.0, 'baby_powder']}}
for key, group in groupby(shopNumbers, lambda x: x[0]):
    listOfThings = ([thing[1] for thing in group])
    #print key,len(listOfThings)
    if len(listOfThings)==len(listOfItems):
        dict1[key]=sum(listOfThings)

#print dict1
print "Final output"
print 'Shop_no','\t', 'Price'
if len(dict1) >0:
    key, value = min(dict1.iteritems(), key=lambda x:x[1])
    print key,'\t' ,value
else:
    print "None"