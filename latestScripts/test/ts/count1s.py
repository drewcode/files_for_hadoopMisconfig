data = open('clusternumbers.txt','r').read().split('\n')

#print(breakup)

cnt0 = 0
cnt1 = 0


for x in data:
	if x == '0':
		cnt0 += 1
	elif x == '1':
		cnt1 += 1

print(cnt0)
print(cnt1)