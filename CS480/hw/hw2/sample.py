apple = 2
pear = 3 < 2
if (3 > 2): apple = 5; print apple, pear
for i in range(apple):  apple = apple + 1; print apple
print i, apple
banana = 3 if apple > 2 else 7
carrot = 13 if (True if banana > apple else False) else 11
print apple, banana, carrot

doughnut = -7+5+12
if 1 < banana < apple < 7 < 16+9:
	doughnut = doughnut + (9 if carrot >= 12 or -3 <= 6 else 5)
	if carrot < 100 and pear:
		carrot = doughnut - 1
print carrot, doughnut

print 3 < apple > 2,  -apple <> banana -8

sum_0 = 0
sum_1 = 0
for i in range(-3 + 6 if not pear else 0):
	sum_0 = sum_0 + i
	sum_1 = sum_1 + i if i != apple or not pear else -sum_1
	for i in range(sum_1):
		for sum_1 in range(sum_0):            
			sum0 = sum_0 + sum_1
	print sum_0, sum_1 if not pear and apple < 30 else i + sum_1
	pear = not pear
