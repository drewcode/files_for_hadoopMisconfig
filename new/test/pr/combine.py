
f1 = open("paramfile.txt", "r")
f2 = open("taskfile.txt", "r")

ff = open("finalfile.csv", "w")

metrics1 = ['max-mb','res-mb','max-vcores','cpu-vcores','vmem:pmem','cpu-limit']
metrics2 = ['CPU_MILLISECONDS','PHYSICAL_MEMORY_BYTES','VIRTUAL_MEMORY_BYTES','COMMITTED_HEAP_BYTES','elapsedTime']
for s in metrics1:
    ff.write(s + ',')
for s in metrics2:
    ff.write(s + ',')
ff.write("\n")


paramstring = f1.read()
paramlist = paramstring.split("\n")

taskstring = f2.read()
tasklist = taskstring.split("\n")

print(len(tasklist))


for i in range(len(tasklist)) :
	#i = int(j / 50)
	# print (str(i) + " " + str(j))
	ff.write (paramlist[i] + tasklist[i] + "\n")

f1.close()
f2.close()
ff.close()