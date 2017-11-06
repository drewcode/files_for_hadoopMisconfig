import csv
from sklearn.neighbors import KNeighborsClassifier

data = csv.reader(open('finalfile.csv', 'r'), delimiter=",")

size = len(open('finalfile.csv', 'r').read().split("\n"))
#print(open('finalfile.csv','r').read().split('\n'))
def init_list_of_objects(size):
    list_of_objects = list()
    for i in range(0,size):
        list_of_objects.append( list() ) #different object reference each time
    return list_of_objects

column = init_list_of_objects(size)
c = []


first = True
features = []
i = 0

for row in data:
	if row:
		if(first) :
			features.append(row[0])
			features.append(row[1])
			features.append(row[2])
			features.append(row[3])
			features.append(row[4])
			features.append(row[5])
			features.append(row[6])
			features.append(row[7])
			features.append(row[8])
			features.append(row[9])
			features.append(row[10])
			features.append(row[11])
			features.append(row[12])
			first = False
		else :
			column[i].append(int(row[0]))
			column[i].append(int(row[1]))
			column[i].append(int(row[2]))
			column[i].append(int(row[3]))
			column[i].append(float(row[4]))
			column[i].append(int(row[5]))
			column[i].append(int(row[6]))
			column[i].append(int(row[7]))
			column[i].append(int(row[8]))
			column[i].append(int(row[9]))
			column[i].append(int(row[10]))
			column[i].append(int(row[11]))


			c.append(int(row[12]))	    
			i = i + 1


d = []
for x in range(size-1) :
	d.append(column[x])

X = d
y = c


knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(X, y)

asd = open("outputs.txt", "w")

while True :
	a,b,c,d,e,f,g,h,i,j,k,l = input().split(",")
	if a == 'q' :
		break

	ans = knn.predict([[a,b,c,d,e,f,g,h,i,j,k,l]])
	if ans[0] == 1 :
		print('fine')
		asd.write("1" + "\n")
	else : 
		print('misconfiged')
		asd.write("0" + "\n")

asd.close()