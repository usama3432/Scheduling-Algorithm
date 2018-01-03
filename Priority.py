#!/usr/bin/python
pro=[]
total=raw_input("Enter a count of process :")
b_t=0
for index in xrange(int(total)):
	pro.append([])
	pro[index].append(raw_input("Process:"))
	pro[index].append(int(raw_input("A.T:")))
	pro[index].append(int(raw_input("Priority:")))
        pro[index].append(int(raw_input("B.T:")))
	b_t+=pro[index][3]
pro.sort(key=lambda pro:pro[1])
pro.sort(key=lambda pro:pro[2])
index=0
print "pro\tA.T\tPriority\tB.T\n"
for index in xrange(int(total)):
	print pro[index][0],'\t',pro[index][1],'\t',pro[index][2],'\t',pro[index][3],'\n'
print "Burst_time : ",b_t
