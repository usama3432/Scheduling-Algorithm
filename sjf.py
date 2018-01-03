#!/usr/bin/python
pro=[]
total=int(raw_input("Enter Count:"))

for index in xrange(total):
	pro.append([])
	pro[index].append(raw_input("Enter P.Name:"))
	pro[index].append(int(raw_input("A.T:")))
	pro[index].append(int(raw_input("B.T:")))
		

pro.sort(key=lambda pro:pro[1])

import Queue
que=Queue
que=que.Queue()
tb=0
ind=1;
a=0

result=[]
que.put(pro[0])
while not que.empty():
	if ind<total:
		while ind <total:
			if pro[ind][1]<=tb:	
				que.put(pro[ind])
				ind+=1
			else:
				break
	new=0
	run=[]
	while not que.empty():
		run.append([])
		run[new].append(que.get())
		new+=1
	i=0
	for i in xrange(new-1):
		j=i
		min=run[i]
		swap=i
		for j in xrange(new-1):
			if min[0][2]>run[j][2]:
				swap=j
				min=run[j]
		run[swap]=run[i]
		run[i]=min
			

	result.append([])
	result[a].append(run[0])
	a+=1
	tb+=5
	#result[a-1][2]
	index=1
	for index in xrange(new-1) :
		que.put(run[index])

		
print result

