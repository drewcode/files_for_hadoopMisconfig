
f1 = open("paramfile.txt", "r")
f2 = open("taskfile.txt", "r")

ff = open("finalfile.csv", "w")

metrics1 = ['max-mb','res-mb','max-vcores','cpu-vcores','vmem:pmem','cpu-limit']
metrics2 = ['CPU_MILLISECONDS','PHYSICAL_MEMORY_BYTES','VIRTUAL_MEMORY_BYTES','COMMITTED_HEAP_BYTES']
for s in metrics1:
    ff.write(s + ',')
for s in metrics2:
    ff.write(s + ',')
ff.write("\n")



paramstring = f1.read()
paramlist = paramstring.split("\n")

taskstring = f2.read()
tasklist = taskstring.split("\n")

for j in range(1600) :
	i = int(j / 50)
	# print (str(i) + " " + str(j))
	ff.write (paramlist[i] + tasklist[j] + "\n")

f1.close()
f2.close()
ff.close()