# -*- coding: utf-8 -*-
"""Prathamesh_Satpute_32_DBDA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/103PLXZdK8sKt2uJMPwQ7HBEpPmHOPQ9q

Q.1) Convert given hrs & mins in second
"""

a=int(input("enter the hours :"))
min=(a*60)
print("total minetus  :",min)

"""Q.4) Write a code to accept a number & print
in words
"""

a= int(input("enter the value :"))
if (a==1):
  print("One")
elif (a==2):
  print("Two")
else:
  print("Three")

"""Q.9) Accept String & print only alternate
characters on a string.
Ex: this i s a _ test
"""

s=input("enter the string :")
a=s[1::2]
print("Alternate character of string :",a)

"""Q.7) Convert Paise in Rupees &
Paises

"""

a=int(input("enter the value in paise :"))
r=(a%100)
q=(a//100)
print("Rupees :",q)
print("Paise :",r)

"""Q.5) Create class"""

class Maths:
  def __init__(self):
    self.a=int(input("Enter first number :"))
    self.b=int(input("Enter second number :"))
  def Add(self):
    self.Add=(self.a + self.b)
    print("Additon is : ",self.Add)
  def Div(self):
    self.Div=(self.a/self.b)
    print("Division is : ",self.Div)
  def Sub(self):
    self.Sub=(self.a - self.b)
    print("Subtraction is : ",self.Sub)
  def Mul(self):
    self.Mul=(self.a * self.b)
    print("Multiplication is : ",self.Mul)

m=Maths()

m.Add()

m.Div()

m.Sub()

m.Mul()

"""Q.10) Create menu driven code for
1) Accept 2 numbers
2) Add
3) Sub
4) Mul
5) Div
"""

a=int(input("enter the 1 number :"))
b=int(input("enter the  number :"))
print("Enter the choice : 1 Add 2 Sub 3 Multiplication 4 Division")
c=int(input("enter choice"))
if c ==1:
  z=a+b
  print(z)
elif c==2:
  q=(a-b)
  print(q)
elif c==3:
  w=(a*b)
  print(w)
else:
  s=(a/b)
  print(s)

