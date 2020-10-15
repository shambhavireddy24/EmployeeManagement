class Emp:
    def __init__(self,name,gmail,empno):
        self.name=name
        self.gmail=gmail
        self.empno=empno
    def disp(self):
        print("Employee name is ",self.name)
        print("Employee mail is ",self.gmail)
        print("Employee number is ",self.empno)

def main():
    print("***********ENQUIRY SYSTEM*************")
    l=[]
    cont=1
    counter=0
    while cont == 1:
        print(" 1 add record")
        print(" 2 view list")
        print(" 3 for search")
        print(" 4 for close")
        print("enter your choice")
        c=int(input())
        if c == 1:
            print("Enter name: ")
            name=input()
            print("Enter gmail: ")
            gmail=input()
            print("Enter employee number: ")
            empno=int(input())
            l.append(Emp(name,gmail,empno))
            counter=counter+1
            print("Do you wish to continue? (1/0): ")
            cont=int(input())
        elif c == 2:
            print("view list: ")
            for empno in l:
                    print( empno.name,empno.gmail,empno.empno)
                    
            
        elif c==3:
            print("Enter employee number you wish to search: ")
            eno=int(input())
            i=0
            while i<counter:
                if eno==l[i].empno:
                    l[i].disp()
                    i=i+1
                    print("found!!!!!!")
                    break
                else:
                    print("not found.........:(")
                    break
        elif c==4:
            break
main()
