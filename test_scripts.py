arr = [1,2,3,4,5,6,7]

sum = 0
mul = 1

for i in arr:
    sum += i
for i in arr:
    mul *= i

print('Sum = {}'.format(sum))
print('Mul = {}'.format(mul))
