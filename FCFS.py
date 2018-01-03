#!/usr/bin/python
pro=[]
tb=0
total=raw_input("Enter total number of processes:")

for i in xrange(int(total)):
	pro.append([])
	pro[i].append(raw_input("Enter Name of process:"))
	pro[i].append(int(raw_input("Arrival Time:")))
	pro[i].append(int(raw_input("burst time:")))
	tb=tb+a[i][2]

pro.sort(key= lambda pro:pro[1])
print 'PName\tA. Time\tB.Time'

for i in xrange(int(total)):
	print pro[i][0] ,'\t',pro[i][1],'\t',pro[i][2]

print "Total Time : ",t
