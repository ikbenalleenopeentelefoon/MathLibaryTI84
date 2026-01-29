import math

type = "Toets enter om uit de programma gaan"
print("A is voor Coördinanten berekenen")
print("B is voor pytaghoras")
Keuze = input("wat wil je berekenen ")

if Keuze == "A" or Keuze == "a":
 print("welkom bij de discriminant rekenaar ")
 A = float(input("wat is jouw A "))
 B = float(input("wat is jouw B "))
 C = float(input("wat is jouw C "))
 D = B ** 2 - 4 * A * C
 print(str(D) + " Dit is jouw discrimannt")
 if D >= 0:
   X1 = ((-B + math.sqrt(D)) / 2)*A
   print("Hier is jouw X1 " + str(X1))
   X2 = ((-B - math.sqrt(D)) / 2)*A
   print("Hier is jouw X2 " + str(X2))
   Y1 = (A * X1 ** 2) + B * X1 + C
   Y2 = (A * X2 ** 2) + B * X2 + C
   print(Y1)
   print(Y2)
   print("De eerste coordinaat is " + "(" + str(Y1) + "," + str(X1) + ")")
   print("De eerste coordinaat is " + "(" + str(Y2) + "," + str(X2) + ")")
   exit = input(type)
 else:
   print("Geen X want D < 0")
   exit = input(type)
  


if Keuze == "B" or Keuze == "b":
 Zijde = input("Kies jouw zijde die je wilt berekenen A,B,C ")

 if Zijde == "C":
  A = int(input("wat is jouw A "))
  B = int(input("wat is jouw B "))
  A2 = A ** 2
  B2 = B ** 2
  C2 = int(A2+B2)
  print(str(C2)  + " Dit is in ^2")
  C = math.sqrt(C2)
  print(str(C) + " hier is jouw resultaat")

 if Zijde == "B":
  A = int(input("wat is jouw A "))
  C = int(input("wat is jouw C "))
  A2 = A ** 2
  C2 = C ** 2
  B2 = int(C2-A2)
  print(str(B2)  + " Dit is in ^2")
  B = math.sqrt(B2)
  print(str(B) + " hier is jouw resultaat")

 if Zijde == "A":
  B = int(input("wat is jouw B "))
  C = int(input("wat is jouw C "))
  B2 = B ** 2
  C2 = C ** 2
  A2 = int(C2-B2)
  print(str(A2)  + " Dit is in wortel")
  A = math.sqrt(A2)
  print(str(A) + " hier is jouw resultaat")