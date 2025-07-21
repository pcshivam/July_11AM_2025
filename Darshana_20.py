num = 0

for i in range(1,16):
  num = num + i

print(num)


for i in range(0,5):
  for j in range(i+1):
    print("*",end=" ")
  print()
for k in range(5,1,-1):
  for l in range(k-1):
    print("*",end=" ")
  print()