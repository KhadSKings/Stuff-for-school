#Creating a coffee program that a user will 
# be able to interact with.
# 23 Sep 2026
# Version 1

# TODO: record an input (Store the answer)
# check for valid answer (input checker)
# Ask questions and respond

#Ask the user whether they like coffee or not
like_coffee = input("Do you like coffee? ")
print(like_coffee) #checking the input is stored
print(f"Your answer was '{like_coffee}'.")

#Check the unput and respond, make sure like_coffee == is added after "or"
if like_coffee == "Yes" or like_coffee == "yes" or like_coffee == "y" or like_coffee =="Y" or like_coffee == "Yes Daddy":
 print("That is great! I like coffee too:)")
else:
  print("You are missing out! It's lowkey GAAAAAAAAAAASSSS")