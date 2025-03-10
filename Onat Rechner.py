def add(a,b):
  print(a+b)
def sub(a,b):
  print (a-b)
def mul(a,b):
  print(a*b)
def div(a,b):
  print(a/b)

lst=[1,2,3,4]

chc=input("bir işlem seçin (1/2/3/4):")
a=int(input("sayı giriniz:"))
b=int(input("sayı giriniz:"))
  
  
 
if chc == "1":
   add (a,b)
elif chc == "2":
  sub (a,b)
elif chc == "3":
  mul (a,b)
elif chc == "4":
  div (a,b)
else:
  print("fehler!")
 
 
 

  
  
  
  