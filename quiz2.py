print ('Hello, welcome to my quiz!!!')
print ()

#the following print the question and the choices
print ("What is Linux")
print ("A. A programm to edit videos")
print ("B. An instruction set for Intel Processors")
print ("C. An operating system")

#this assigns the variables loss1, point1 to the number 0 and the variable ans1 to whatever wil be inputted from the keyboard
point1 = 0
loss1 = 0
ans1 = input()

#this tells the program that if the answer is what is correct, to print Correct and assign the variable point1 to the number 1
if ans1=="C" or ans1=="c":
    print ("Correct")
    point1 = 1
#this tells the program that if the answer isn't what is correct, to print Wrong and assign the variable loss1 to the number 1
else:
    print ("Wrong")
    loss1 = 1
print()

#the following print the question and the choices
print ("What is binary code?")
print ("A. An algorithm for Maths")
print ("B. A code a processor can understand, which is made up of 1 and 0")
print ("C. A code used for hacking into computers")

#this assigns the variables loss2, point2 to the number 0 and the variable ans2 to whatever wil be inputted from the keyboard
point2 = 0
loss2 = 0
ans2 = input()

#this tells the program that if the answer is what is correct, to print Correct and assign the variable point2 to the number 1
if ans2=="B" or ans2=="b":
    print ("Correct")
    point2 = 1

#this tells the program that if the answer isn't what is correct, to print Wrong and assign the variable loss2 to the number 1
else:
    print ("Wrong")
    loss2 = 1
    
print ()

#this prints out the final score, the number of correct answers, as well as the number of the wrong ones
print ("Your score is:", point1 + point2)
print ("Correct answers:", point1 + point2)
print ("Incorrect answers:", loss1 + loss2)

#this prints the string Are you done? and assigns the variable ans3 to whatever is inputted from the keyboard
print ("Are you done?")
ans3 = input()

#this tells the program that if the user inputs the word Yes, to print the following statement and close itself
if ans3=="Yes" or ans3=="yes":
    print ("OK,this is the end")
    exit()

    
    
        
        
