import SendEmail
import time

#me = input("What is your email address?")
#key = input("What is your email password?")
who = input("Whose birthday is coming up?")
you = input("And what is their email?")
#sub = input("What is your message's subject line?")
freq = input("How many emails should they get an hour? (0.0417-60)")
Prep = True
while Prep == True:



SendEmail.SendIt(me, key, you, sub, msg)