import math

f=open("dt-data.txt")
f.readline()
f.readline()
data1=[]
n=0
for i in f:
	data1.append(i.split(','))
	n+=1
n+=1
f.close()

attr=["Size", "Occupied", "Price", "Music", "Location", "VIP", "Favorite Beer"]
attrset1=attr.copy()
# print(attrset)
attrOptions=[["Large", "Medium", "Small"],["High", "Moderate", "Low"],["Expensive", "Normal", "Cheap"],["Loud", "Quiet"],
			["Talpiot", "City-Center", "Mahane-Yehuda", "Ein-Karem", "German-Colony"],["Yes", "No"],["Yes", "No"]]
output=[[""]]
def findRoot(data,attrset,deep,location):
 	if len(attrset)==1:
 		return
 	minE=1
 	selectAttr=""
 	selectAttCount=[]
 	for att in attrset:
 		attCount= [[0 for col in range(3)] for row in range(len(attrOptions[attr.index(att)]))]
 		total=0
 		for selectData in data:
 			
 			for i in range(len(attrOptions[attr.index(att)])):
 				
 				if attrOptions[attr.index(att)][i] in selectData[attr.index(att)]:
 					attCount[i][0]+=1
 					total+=1
 					if "Yes" in selectData[len(attr)]:
 						attCount[i][1]+=1
 					else:
 						attCount[i][2]+=1
 					continue
 		if att==attrset[0]:
 			selectAttCount=attCount
 		entropy=0
 		# print(total)
 		# print(att+" ")
 		# print(attCount)
 		for i in range(len(attrOptions[attr.index(att)])):
 			# print(entropy)
 			if attCount[i][0]==0:
 				continue
 			# print(att)
 			# print(attCount[i])
 			tmp1=attCount[i][1]/attCount[i][0]
 			tmp2=attCount[i][2]/attCount[i][0]
 			# print(tmp1)
 			# print(tmp2)
 			if tmp1==0:
 				entropy+=(attCount[i][0]/total)*((attCount[i][2]/attCount[i][0])*math.log(attCount[i][0]/attCount[i][2],2))
 				continue
 			if tmp2==0:
 				entropy+=(attCount[i][0]/total)*((attCount[i][1]/attCount[i][0])*math.log(attCount[i][0]/attCount[i][1],2))
 				continue
 					


 			entropy+=(attCount[i][0]/total)*((attCount[i][1]/attCount[i][0])*math.log(attCount[i][0]/attCount[i][1],2)+(attCount[i][2]/attCount[i][0])*math.log(attCount[i][0]/attCount[i][2],2))
 		
 		if entropy<minE:
 			minE=entropy
 			selectAttr=att
 			selectAttCount=attCount
 		if selectAttr=="":
 			selectAttr=attrset[0]
 		# print(att)
 	# print(minE)
 	# print(selectAttr+" ")

 	# output[deep].append(selectAttr)
 	output[deep][location]=selectAttr
 	# output.append(["" for i in range(len(selectAttCount))])
 	output.append(["" for i in range(len(selectAttCount))])
 	# print(attrset)
 	nextset=attrset.copy()
 	nextset.remove(selectAttr)
 	# print(nextset)
 	
 	lo=0
 	for i in range(len(attrOptions[attr.index(selectAttr)])):
 		nextdata=[]
 		if selectAttCount[i][0]==0:
 			# print(attrOptions[attr.index(selectAttr)][i]+" empty ")
 			output[deep+1][i]="      "
 			continue
 		if selectAttCount[i][1]==0:
 			# print(attrOptions[attr.index(selectAttr)][i]+" no ")
 			output[deep+1][i]="No"
 			continue
 		if selectAttCount[i][2]==0:
 			# print(attrOptions[attr.index(selectAttr)][i]+" yes ")
 			output[deep+1][i]="Yes"
 			continue
 		for selectData in data:
 			if attrOptions[attr.index(selectAttr)][i] in selectData[attr.index(selectAttr)]:
 				nextdata.append(selectData)

 		findRoot(nextdata,nextset,deep+1,i)

	

findRoot(data1,attrset1,0,0)
for i in output:
	print(i)


 				 				
			