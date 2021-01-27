x = [1,6,8,9,4,2,0]

print(sorted(x))
print(sorted(range(len(x)), key=lambda i: -x[i]))
