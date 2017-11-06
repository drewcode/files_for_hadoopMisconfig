data = open('taskfile.txt','r').read().split('\n')
breakup = [x.split(',') for x in data if data]
#print(breakup)

cnt0 = 0
cnt1 = 0
cnt2 = 0


for x in breakup:
	if len(x) == 5:
		if x[4] == '0':
			cnt0 += 1
		elif x[4] == '1':
			cnt1 += 1
		elif x[4] == '2':
			cnt2 += 1

print(cnt0)
print(cnt1)
print(cnt2)