# get user email address
email = input("Enter you email:").strip()

# slice out user name
user = email[:email.index("@")]
# slice domain name
domain = email[email.index("@")+1:]
# format message
output = "Your username is {} and your domain us {}".format(user, domain)
# display output message
print (output)