a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
choice = input("Enter your preferred operator:\n"
               "1.Addition \n"
               "2.Subtraction \n"
               "3.Multipliction \n"
               "4.Division \n")
match choice:
case "1" : 
    print(f"Result is {a+b}")
case "2" : 
    print(f"Result is {a-b}")
case "3" :
    print(f"Result is {a*b}")
case "4" : 
    if b==0:
      print("Cannot divide by zero")
else:
  print(f"Result is {a/b}")
case_ : 
    print("Entered invalid operation")
