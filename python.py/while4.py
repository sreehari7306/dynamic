name=int(input("enther a number:"))
d=(1:"one",2:"two,3:three,4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine")
i=0
a=""
while num>0:
      i=num%10
      num=num//10
      a=d[i]+""+a
   print(a)