students = ["Mukesh", "Chirag", "Kiran"]

while True:
   print("\nStudent Management System")
   print("=========================")
   print("0. Exit")
   print("1. Print all students")
   print("2. Add a new student")
   print("3. Delete a student")
   while True:
      choice = input("\nEnter your choice: ")
      try:
         choice = int(choice)
      except:
         print(f"Invalid value {choice}")
         continue
      break
   if choice == 0:  # Exit
      break

   elif choice == 1:  # Print all students
      print("\nStudents in our records:")
      print("=======================:")
      for s in students:
         print(s)

   elif choice == 2:  # Add a new Student
      s = input("Enter new student name: ")
      students.append(s)
      print(f"\nNew student {s} added")

   elif choice == 3:  # Delete a student
      s = input("Enter the student name to delete: ")
      if s in students:
         students.remove(s)
         print(f"Student {s} removed from the list")
      else:
         print(f"Student {s} not in the list")



   else:
      print("\nInvalid choice. Enter a value between 0 and 2")

print("\nGood BYE")
