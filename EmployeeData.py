t("***********ENQUIRY SYSTEM*************")


l=[]

def view_list():
          for i in l:
                       print(i[0], i[1], i[2])

def add_data():
           while True:
                 x=input("\n enter your name,DOB,Gmail----->").split(",")
                 l.append(x)
                 y=input("Do you wish to add more ? yes/no----->")
                 if y=='yes':
                        pass
                 else : 
                       break

def search_data():
            name=input("\n enter the name to search   ")
            for i in l:
                  if name==i[0]:

                       print(" name Found!!! :)") 
                       print(i[0],i[1],i[2])
                       break
            else :
                  print(" sorry name not found :( !!!!!!")
def end():
            print("\n Thank you!!!! ")
            exit()

while True:
    print("___________________________")
    print("                            ")
    print("Options are given please choose any :")
    print("\n1.Add data")
    print("2.view data")
    print("3.search data")
    print("4.exit")
    ch=input("\nenter the options   ")
    if ch=='1':
           add_data()
    elif ch=='2':
            view_list()
    elif  ch=='3':
             search_data()
    elif  ch=='4':
              end()

    else:
          print("wrong input")
           
