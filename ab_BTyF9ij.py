
l=[]
for i in range(1,7):
	l.append(input("enter the value:"))
file=open('ab.csv','w')

file.write(str(l[0])+","+str(l[1])+","+str(l[2])+","+str(l[3])+","+str(l[4])+","+str(l[5]))
file.close()

	

