import csv
import pyperclip
from write_to_file import write
from read_from_file import read
from encrypt import encrypt
from decrypt import decrypt
from decorators import input_

print('1. Save' +
      '\t\t2. Update' +
      '\n3. Remove' +
      '\t4. Copy')


option = input()

if option == '1':
    # save
    title = input_('Enter title: ')
    for row in read('passwords.csv'):
        if row[0] == title:
            print('title already exists!')
            break
    else:
        url = input_('Enter url: ')
        username = input_('Enter username: ')
        password = encrypt(input_('Enter key: '), input_('Enter password: '))

        write('passwords.csv', 'a+', [[title, url, username, password]])


elif option == '2':
    # update
    title = input('Enter title: ')
    file_content = read('passwords.csv')
    for row in file_content:
        if row[0] == title:
            change_title = input('Wanna change title?(y/n) ')
            if change_title == 'y':
                row[0] = input('Enter new title: ')
            change_url = input('Wanna change url?(y/n) ')
            if change_url == 'y':
                row[1] = input('Enter new url: ')
            change_username = input('Wanna change username?(y/n) ')
            if change_username == 'y':
                row[2] = input('Enter new username: ')
            change_password = input('Wanna change password?(y/n) ')
            if change_password == 'y':
                row[3] = password = encrypt(
                    input('Enter key: '), input('Enter new password: '))
            if 'y' in (change_title, change_url, change_username, change_password):
                write('passwords.csv', 'w', file_content)
                print('Changes saved successfully!')
            break


elif option == '3':
    # remove
    title = input('Enter title: ')
    file_content = read('passwords.csv')
    for row in file_content:
        if row[0] == title:
            file_content.remove(row)
            write('passwords.csv', 'w', file_content)
            break
    else:
        print("title doesn't exist!")


elif option == '4':
    # copy
    title = input('Enter title: ')
    for row in read('passwords.csv'):
        if row[0] == title:
            pyperclip.copy(row[2])
            print('username copied successfully!')
            input()
            pyperclip.copy(decrypt(input('Enter key: '), row[3]))
            print('password copied successfully!')
            break
    else:
        print("title doesn't exist!")


else:
    # invalid
    print('invalid input!')
