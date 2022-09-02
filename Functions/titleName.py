def format_name(fname, lname):
  """Take a first and last name and format it to return the title case vesion of the name."""
  if fname =='' or lname =='':
    return print("You have missed one of the two names 😕😕")
  else:
    fname = fname.title()
    lname = lname.title()
    print(f"{fname} {lname}")
  # return fname +' '+lname

f = input('what is your first name? ')
l = input('what is your last name? ')

format_name(f,l)