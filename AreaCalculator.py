print(("-" * 30) + "\nArea Calculator\n" + ("-" * 30))

print("\n1 - Square\n2 - Rectangle\n3 - Circle\n")
choice = input("Your choice: ")

if choice == "1":
    side = int(input("A side: "))
    print("Area of square is: {}".format(side ** 2))

elif choice == "2":
    aside = int(input("A side: "))
    bside = int(input("B side: "))
    print("Area of rectangle is: {}".format(aside * bside))

elif choice == "3":
    r = int(input("Radius: "))
    pi = 3.14159
    print("Area of circle is: {}".format((r ** 2) * pi))

else:
    print("Good bye...")
