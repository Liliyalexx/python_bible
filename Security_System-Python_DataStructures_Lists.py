known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred","Georgia", "Harry" ]
print(len(known_users))
while True:
  print("Hi! My name is Travis")
  name = input("What is your name?: ").strip().capitalize()
  if name in known_users:
    print("Hello {}!".format(name))
    remove = input("Would you like to be removed from system(y/n?: ")

    if remove =="y" or remove =="Y":
  else:
      print("Name is not recognized!")
  

