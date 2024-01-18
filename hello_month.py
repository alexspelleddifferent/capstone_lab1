from datetime import datetime

today = datetime.now()
today_month=today.strftime('%B')
#get month

name=input("What is your name? ")
month=input(f'Hello {name}, what month were you born? ')
#get input

print(f'Welcome {name}, your name is {len(name)} characters long')

#check bday month
if month==today_month:
    print(f'Happy birthday month!')