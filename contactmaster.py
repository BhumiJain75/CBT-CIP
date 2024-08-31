# Welcome to contact book

contact={}

def display_contact():
  print("Name\t\t\t   Contact number")
  for key in contact:
    print("{}\t\t{}".format(key,contact.get(key)))

while True:
 choice=int(input("1. Add new contact \n 2. Search Contact \n 3. Display Contact \n 4. Edit Contact \n 5. Delete Contact \n 6. Exit \n Enter your Choice:"))
 if choice==1:
  name=input("Enter name: ")
  phone_no=int(input("Enter phone no: "))
  contact[name]=phone_no
 elif choice==2:
   search_name=input("Enter name: ")
   if search_name in contact:
     print(search_name, "'s contact number is ", contact[search_name])
   else:
    print("Name is not found in contact book")
 elif choice==3:
  if not contact:
   print("empty contact book ")
  else:
    display_contact()
 elif choice==4:
   edit_contact=input("Enter contact name to be edited: ")
   if edit_contact in contact:
     phone_no=input("enter phone no: ")
     contact[edit_contact]=phone_no
     print("Contact edited ")
     display_contact()
   else:
     print("Name is not found in contact book")
 elif choice==5:
   del_contact=input("Enter the contact name to be deleted: ")
   if del_contact in contact:
     confirm=input("Do you want to delete this contact yes or no?")
     if confirm=="yes" or confirm=="Yes":
       contact.pop(del_contact)
       display_contact()
     else:
         print("Name is not found in contact book")
 else:
    break  
         