
msg = input("Would you like to Continue?")
if msg == "no" or msg == 'n':
    print("Exiting")
elif msg == "yes" or msg == 'y':
    print("Continuing...")
    print("Complete!")
else:
    print("Please try again and respond with yes or no")