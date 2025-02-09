#CS 161 - Python Week 5 Homework Assignment
#Jackson Grant

#1

div5 = int(input('Enter a number: '))
if(div5 % 5 == 0):
    print(f'The number "{div5}" is divisible by 5')
else:
    print(f'The number "{div5}" is not divisible by 5')
    
#2.1

state1 = (input('Enter a US state: ')).lower()

if(state1 == 'california'):
    print("Sacramento")
elif(state1 == 'texas'):
    print("Austin")
elif(state1 == 'florida'):
    print("Tallahassee")
elif(state1 == 'new york'):
    print("Albany")
elif(state1 == 'illinois'):
    print("Springfield")
elif(state1 == 'washington'):
    print("Olympia")
else:
    print("Sorry I don't know that capital")
    
#2.2

UsStateCapitals = {
    'alabama': 'Montgomery',
    'alaska': 'Juneau',
    'arizona': 'Phoenix',
    'arkansas': 'Little Rock',
    'california': 'Sacramento',
    'colorado': 'Denver',
    'connecticut': 'Hartford',
    'delaware': 'Dover',
    'florida': 'Tallahassee',
    'georgia': 'Atlanta',
    'hawaii': 'Honolulu',
    'idaho': 'Boise',
    'illinois': 'Springfield',
    'indiana': 'Indianapolis',
    'iowa': 'Des Moines',
    'kansas': 'Topeka',
    'kentucky': 'Frankfort',
    'louisiana': 'Baton Rouge',
    'maine': 'Augusta',
    'maryland': 'Annapolis',
    'massachusetts': 'Boston',
    'michigan': 'Lansing',
    'minnesota': 'St. Paul',
    'mississippi': 'Jackson',
    'missouri': 'Jefferson City',
    'montana': 'Helena',
    'nebraska': 'Lincoln',
    'nevada': 'Carson City',
    'new hampshire': 'Concord',
    'new jersey': 'Trenton',
    'new mexico': 'Santa Fe',
    'new york': 'Albany',
    'north carolina': 'Raleigh',
    'north dakota': 'Bismarck',
    'ohio': 'Columbus',
    'oklahoma': 'Oklahoma City',
    'oregon': 'Salem',
    'pennsylvania': 'Harrisburg',
    'rhode island': 'Providence',
    'south carolina': 'Columbia',
    'south dakota': 'Pierre',
    'tennessee': 'Nashville',
    'texas': 'Austin',
    'utah': 'Salt Lake City',
    'vermont': 'Montpelier',
    'virginia': 'Richmond',
    'washington': 'Olympia',
    'west virginia': 'Charleston',
    'wisconsin': 'Madison',
    'wyoming': 'Cheyenne'
}

state2 = (input("Enter a US state to find it's capital: ")).lower()
capital = UsStateCapitals.get(state2)

if(capital):
    print(f"The captital of {state2.title()} is {capital}")
else:
    print(f"{state2.title()} is not a US state.")
    
#2.2
#I learned about .title doing this one seems useful for making things look nice
    
state3 = (input("Enter a US state to find it's capital: ")).lower()

match UsStateCapitals.get(state3):
    case None:
        print(f"{state3.title()} is not a US state.")
    case capital:
        print(f"The captital of {state3.title()} is {capital}")
        
#4

def PoolPrice(age):
    """
    calculates the price of admission for pool access based of your age bracket.
    
    takes the users age(int) as a parameter
    
    returns a number based on
        - Free if under 2
        - $3 if 2-11
        - $6 if 11-60
        - $4 if over 60
    """
    if(age<2):
        return 0
    elif(age<=11):
        return 3
    elif(age<=60):
        return 6
    elif(age>60):
        return 4
UserAge = int(input('Enter Your age: '))
print(f'The price of admission to the pool is ${PoolPrice(UserAge)} for your age group.')

#2

import requests

page_content = (requests.get('https://coccbobcat.com')).text
times160 = page_content.count('160')
print(f'The substring "160" appears {times160} times in the HTML source of http://coccbobcat.com.')
print('Process finished with exit code 0')

#3

import psutil

RunningProcesses = len(psutil.pids())
print(f'Number of running processes: {RunningProcesses}')
print('Process finished with exit code 0')




