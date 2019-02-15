print ("Hello!!!This is my quiz")
print ()
print ("Ok, let's begin")
print()

point = 0

print ("Who was the CEO of Apple?")
ans = input()
if ans=="Steve Jobs" or ans=="steve jobs":
    print ("Correct!!")
    point = 1
else:
    print ("Wrong!")
    
print ()

print ("What is the command to show text in Python?")
ans2 = input()
point2 = 0
if ans2=="print":
    print ("Well Done!!")
    point2 = 1
else:
    print ("Noo, there goes your opportunity!!")
    
print ()

print ("What is the central component of a computer?")
ans3 = input()
point3 = 0
if ans3=="Processor" or ans3=="CPU" or ans3=="cpu" or ans=="processor":
    print ("Correct!!")
    point3 = 1
else:
    print ("Wrong:(")
    
print()

print ("Your score is:")
print (point + point2 + point3)
print()
print("Thanks for taking my quiz!!!")

