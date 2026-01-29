import math

type = "Toets enter om uit de programma gaan"
print("1 is voor Coördinanten berekenen")
print("2 is voor pytaghoras")
Keuze = input("wat wil je berekenen ")

if Keuze == "1":
 print("welkom bij de discriminant rekenaar ")
 A = float(input("wat is jouw A "))
 B = float(input("wat is jouw B "))
 C = float(input("wat is jouw C "))
 D = B ** 2 - 4 * A * C
 print(str(D) + " Dit is jouw discrimannt")
 if D >= 0:
   X1 = ((-B + math.sqrt(D)) / (2*A))
   print("Hier is jouw X1 " + str(X1))
   if D > 0:
     X2 = ((-B - math.sqrt(D)) / (2*A))
     print("Hier is jouw X2 " + str(X2))
   Y1 = (A * X1 ** 2) + B * X1 + C
   Y2 = (A * X2 ** 2) + B * X2 + C
   print(Y1)
   print(Y2)
   print("De eerste coordinaat is " + "(" + str(round(Y1, 2)) + "," + str(round(X1, 2)) + ")")
   if D > 0:
    print("De tweede coordinaat is " + "(" + str(round(Y2, 2)) + "," + str(round(X2, 2)) + ")")
   exit = input(type)
 else:
   print("Geen X want D < 0")
   exit = input(type)

if Keuze == "2":
 Zijde = input("Kies jouw zijde die je wilt berekenen A,B,C (1,2,3)")

 if Zijde == "C" or Zijde == "c" or Zijde == "3":
  A = int(input("wat is jouw A "))
  B = int(input("wat is jouw B "))
  A2 = A ** 2
  B2 = B ** 2
  C2 = int(A2+B2)
  print(str(C2)  + " Dit is in ^2")
  C = math.sqrt(C2)
  print(str(C) + " hier is jouw resultaat")
  exit = input(type)

 if Zijde == "B" or Zijde == "b" or Zijde == "2":
  A = int(input("wat is jouw A "))
  C = int(input("wat is jouw C "))
  A2 = A ** 2
  C2 = C ** 2
  B2 = int(C2-A2)
  print(str(B2)  + " Dit is in ^2")
  B = math.sqrt(B2)
  print(str(B) + " hier is jouw resultaat")
  exit = input(type)

 if Zijde == "A" or Zijde == "a" or Zijde == "1":
  B = int(input("wat is jouw B "))
  C = int(input("wat is jouw C "))
  B2 = B ** 2
  C2 = C ** 2
  A2 = int(C2-B2)
  print(str(A2)  + " Dit is in wortel")
  A = math.sqrt(A2)
  print(str(A) + " hier is jouw resultaat")
  exit = input(type)