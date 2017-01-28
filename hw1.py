f=open("dt-data.txt")
f.readline()
f.readline()
data=[]
n=0
for i in f:
	data.append(i.split(','))
	n+=1
n+=1
f.close()
print(data)
attr=["Size", "Occupied", "Price", "Music", "Location", "VIP", "Favorite Beer"]
 def findRoot():
 	if attr=={}:
 		return
 	minE=1
 	options=[]
 	for i in range(len(attr)):
 		for selectData in data:
 			if selectData[i] not in options:
 				options.append(selectData[i])
