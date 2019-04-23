l=[]
start = input("Input starting point: ")
print()
end = input("Input end: ")
print()
divisible = input("Input number that it must be fully divisible with: ")
print()
not_divisible = input("Input number that it must not be fully divisible with: ")
print()

for i in range(int(start), int(end)):
    if (i%int(divisible)==0) and (i%int(not_divisible)!=0):
        print(i)
