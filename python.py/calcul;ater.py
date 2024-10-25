def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
while True:
    print("""1,addition
          2,subtractions
          3,multiplication
          4,division
          5,exit""")
    choice=int(input("enther first your choice :"))
    if choice==1:
        no1=int(input("enther first your choice:"))
        no2=int(input("enther seccond your choice :"))
        res=add(no1,no2)
        print(res)
        
    elif choice==2:
        no1=int(input("enther first your choice :"))
        no2=int(input("enther seccond your choice :"))
        res=sub(no1,no2)
        print(res)
        
    elif choice==3:
        no1=int(input("enther first your choice:"))
        no2=int(input("enther seccond your choice:"))
        res=mul(no1,no2)
        print(res)
        
    elif choice==4:
        no1=int(input("enther first your choice:"))
        no2=int(input("enther seccond your choice:"))
        res=div(no1,no2)
        print(res)
         
    elif choice==5:
        break
    
    1,addition
#           2,subtraction
#           3,multiplication
#           4,division
#           5,exit
# enther first your choice :5

    
        
        
        
        
