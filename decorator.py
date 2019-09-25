d ={}
flag =0
def check(func):
    def wrapper():
        if(flag==0):
            func()
        else:
            print("already log in")

    return wrapper

def checker(func):
    def wrapper():
        if(flag==1):
            func()
        else:
            print("sorry.plz log in")
    return wrapper
@check
def login():
    global flag
    u=input("username:")
    p=input("password:")
    if(u==p):
        print("log in")
        flag=1


    #return check
@checker
def add():
    limit=int(input("enter the limit"))
    for i in range(limit):
        x={'id:':int(input("Id:")),
           'name:':input("student name:"),
           'mark1':int(input("mark1:")),
           'mark2':int(input("mark2:"))}
        d[i] =x
    display()

def display():
    for keys, value in d.items():
        for key in value:
            print (key ,":",value[key])


while(True):
    print("1.Login \n2.Create student db \n3.update student db \n4.Insert to databse \n5.Delete database \n6.Exit ")
    choice=int(input("Enter your choice:"))
    if(choice==1):
        login()
    elif(choice==2):
        add()
    # elif (choice == 3):
    #     update()
    # elif (choice == 4):
    #     insert()
    # elif (choice == 5):
    #     delete()
    elif (choice == 6):
        print("exiting")
        exit()