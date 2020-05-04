from setup_database import create_user_table
from queries import *


def execute_help_command():
    print('''
#############
###Options###
#############

1. `add` - insert new business card
2. `list` - list all business cards
3. `delete` - delete a certain business card (`ID` is required)
4. `get` - display full information for a certain business card (`ID` is required)
5. `help` - list all available options
''')


def execute_add_command():
    user_name = input('Enter user name: ')
    email = input('Enter email: ')
    age = input('Enter age: ')
    phone = input('Enter phone: ')
    additional_info = input('Enter additional_info (optional): ')
    values = (user_name, email, age, phone, additional_info)
    query_for_adding_values_to_table(values)


def execute_list_command():
    table = query_for_reading_all_rows_in_table()
    for row in table:
        print('{id}. ID: {id}, Email: {email}, Full name: {name}'.format(id=row[0], email=row[1], name=row[2]))


def print_contact_info(row):
    print('###############')
    print('Id: {id}'.format(id=row[0][0]))
    print('Full name: {name}'.format(name=row[0][1]))
    print('Email: {email}'.format(email=row[0][2]))
    print('Age: {age}'.format(age=row[0][3]))
    print('Phone: {phone}'.format(phone=row[0][4]))
    print('Additional info: {info}'.format(info=row[0][5]))
    print('###############')


def execute_get_command():
    id = input('Enter id: ')
    row = query_for_selecting_row_by_id_in_table(id)
    print('Contact info:')
    print()
    print_contact_info(row)


def execute_delete_command():
    id = input('Enter id: ')
    row = query_for_selecting_row_by_id_in_table(id)
    query_for_deleting_row_by_id_in_table(id)
    print()
    print('Following contact is deleted successfully:')
    print()
    print('###############')
    print_contact_info(row)
    print('###############')


def execute_command(command):
    if command == 'help':
        execute_help_command()
    elif command == 'add':
        execute_add_command()
    elif command == 'list':
        execute_list_command()
    elif command == 'get':
        execute_get_command()
    elif command == 'delete':
        execute_delete_command()
    else:
        pass


def main():
    create_user_table()
    print('Hello! This is your business card catalog.')
    print('What would you like? (enter "help" to list all available options)')
    command = input('>>>Enter command: ')
    while command != 'exit':
        execute_command(command)
        command = input('>>>Enter command: ')


if __name__ == '__main__':
    main()
