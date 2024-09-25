def recursiveEVEN(a,b):
   a=int(a)
   b=int(b)
   if a<10 or b<10:
       return a*b
   if a>b:
      c=int(len(str(a)))
      d=int(c/2)
      #c= c-d
      #get odd n digited numbers say 134=> 13 and 4 for the logic to work, here switch new c and d; we haven't changed c
      d=c-d
      c=c-d
   else:
      c=int(len(str(b)))
      d=int(c/2)
      d=c-d
      c=c-d
   a=str(a)  
   b=str(b)
#what if length of numbers aren't same? gives index error in num1,2,3,4 part
   append=len(a)-len(b)
   
   if append<0:      
       a="0"*abs(append)+a    
   elif append>0:
       b="0"*abs(append)+b
   num1=a[0:d]#bigger
   num2=a[d:c+d]   
   num3=b[0:d]#bigger
   num4=b[d:c+d]
    
   ac=recursiveEVEN(num1,num3)
   sumAB=int(num1)+int(num2)
   sumCD=int(num3)+int(num4)
   middle=recursiveEVEN(sumAB,sumCD)
   bd=recursiveEVEN(num2,num4)
   middle=int(middle)-int(ac)-int(bd)

   return(ac*10**(c+d) + middle*10**d + bd)

    
input1=int(input("enter value 1 "))
input2=int(input("enter value 2 "))
x=recursiveEVEN(input1,input2)
print(x)