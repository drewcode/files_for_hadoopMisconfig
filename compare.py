f1 = open("clusternumbers.txt", "r")
f2 = open("outputs.txt", "r")

f1s = f1.read().split("\n")
f2s = f2.read().split("\n")

counter = 0

#1 is dominant cluster in clustered data and 
#0 is dominant cluster in predicted outputs and in training data cluster numbers

for i in range(1600):
	if int(f1s[i]) is not int(f2s[i]):
		counter = counter + 1

print(str((counter/1600)))
