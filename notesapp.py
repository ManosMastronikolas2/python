print("----NOTES APP----\n")



while 1:
    print("new(New note)")
    print("read(Read your notes)")
    print("exit\n")
    uin = input()
    if uin == "new" or uin == "NEW":
            f = open("ToDos.txt", "a")
            print("Add Note: ")
            note = input()
            print("Add Date: ")
            date = input()
            print("Add Hour: ")
            hour = input()
            f.write(str(date))
            f.write(" ")
            f.write(str(hour))
            f.write(" ")
            f.write(str(note))
            f.write('\n')
    elif uin == "exit" or uin == "EXIT":
        exit()
        f.close()
    elif uin == "read" or uin == "READ":
       f = open("ToDos.txt", "r")
       print(f.read())

        
       
       
    
    



























    
    
