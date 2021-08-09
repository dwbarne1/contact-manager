import os, json
from difflib import get_close_matches

try:
    with open('contacts.json', 'r') as file:
        contacts = json.load(file)
except IOError or FileNotFoundError:
    print('Error when loading contacts')

print('Loading Contacts...')

for x in contacts:
    print('{:12}'.format(x), ' - ', contacts[x])

print('Data Loaded. Press Enter to continue...')
input()

i = True
while i == True:
    print('\n\t\tManage Contacts')
    contactName = input('Enter contact name to search list: ')
    searchResults = get_close_matches(contactName, contacts, n=3, cutoff=0.6)

    if contactName in contacts:
        print('\nContact Found:')
        print('Edit Contact')
        print(contactName, ' : ', contacts[contactName])
    elif len(searchResults) > 1:
        print('\nContacts Found:')
        for s in searchResults:
            print(s, ' : ', contacts[s])
    else:
        print('\nContact Not Found')
        print('Add New Contact\n')

    phoneNumber = input(f'Enter {contactName}\'s phone number (###)###-#### or enter for no change: ')
    if len(phoneNumber) == 13:
        contacts[contactName] = phoneNumber

    os.system('cls')

    exit = input('Enter E to exit or press Enter to continue...')
    if(exit == 'E'):
        i = False

try:
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file)
except IOError or FileNotFoundError:
    print('Error when dumping contacts')
