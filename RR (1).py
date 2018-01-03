#!/usr/bin/python
p=[]
total=int(raw_input("Enter a count of process :"))
time_slice=int(raw_input("Time Slice"))
for index in xrange(int(total)):
	p.append([])
	p[index].append(raw_input("Process:"))
	p[index].append(int(raw_input("A.T:")))
        p[index].append(int(raw_input("B.T:")))

run=[]
p.sort(key=lambda p:p[1])
tb=0
import Queue
ready=Queue
ready=ready.Queue()
arr=0
ready.put(p[arr])
arr+=1
while not ready.empty():
	run=ready.get()
	if run[2]>=time_slice:
		run[2]=run[2]-time_slice
		print run
		tb+=time_slice
		if arr<=total:
			while arr<total:
				if p[arr][1]<=tb:	
					ready.put(p[arr])
				if arr+1==total:
					arr+=1
					break
				arr+=1
		if run[2]!=0:
			ready.put(run)
	else:
		print run
		tb+=run[2]
		if arr<=total:
			while arr<total:
				if p[arr][1]<=tb:
					ready.put(p[arr])
				if arr+1==total:
					arr+=1
					break
				arr+=1
						
