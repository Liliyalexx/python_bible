known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred","Georgia", "Harry" ]
# print(len(known_users))
while True:
  print("Hi! My name is Travis")
  name = input("What is your name?: ").strip().capitalize()
  if name in known_users:
    print("Hello {}!".format(name))
    remove = input("Would you like to be removed from system(y/n?): ").strip().lower()

    if remove =="y":
      #  print(known_users)
      known_users.remove(name)
      #  print(known_users)
    elif remove =="n":
        print("No problem, I didn't want you to leave anyway!")
    
  else:
    print("Hmmm I don't think I have met you yet {}".format(name))
    add_me= input("Would you like to be added to the list(y/n?): ").strip().lower()
    if add_me == "y":
      #  print(known_users)
       known_users.append(name)
      #  print(known_users)
    elif add_me =="n":
        print("No worries, see you around!")
