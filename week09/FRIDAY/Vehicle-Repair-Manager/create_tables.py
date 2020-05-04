import sqlite3


def create_base_user_table():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    delete_table_query = 'DROP TABLE IF EXISTS BaseUser'
    create_table_query = '''
              CREATE TABLE BaseUser (
                    id INTEGER NOT NULL PRIMARY KEY,
                    user_name VARCHAR(30),
                    email VARCHAR(30),
                    phone_number INTEGER,
                    address VARCHAR(100)
               )
    '''
    cursor.execute(delete_table_query)
    cursor.execute(create_table_query)
    connection.commit()
    connection.close()


def create_client_table():
    # connection = sqlite3.connect('vehicle_management.db')
    # cursor = connection.cursor()
    # delete_table_query = 'DROP TABLE IF EXISTS Client'
    # create_table_query = '''
    #           CREATE TABLE Client (
    #                 base_id INTEGER NOT NULL,
    #                 FOREIGN KEY(base_id) REFERENCES BaseUser(id)
    #            )
    # '''
    # cursor.execute(delete_table_query)
    # cursor.execute(create_table_query)
    # connection.commit()
    # connection.close()
    pass


def create_mechanic_table():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    delete_table_query = 'DROP TABLE IF EXISTS Mechanic'
    create_table_query = '''
              CREATE TABLE Mechanic (
                    FOREIGN KEY(base_id) REFERENCES BaseUser(id),
                    title VARCHAR(20)
               )
    '''
    cursor.execute(delete_table_query)
    cursor.execute(create_table_query)
    connection.commit()
    connection.close()


def create_vehicle_table():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    delete_table_query = 'DROP TABLE IF EXISTS Vehicle'
    create_table_query = '''
              CREATE TABLE Vehicle (
                    id INTEGER PRIMARY KEY,
                    category VARCHAR(50),
                    make VARCHAR(20),
                    model VARCHAR(20),
                    register_number VARCHAR(20),
                    gear_box VARCHAR(20),
                    FOREIGN KEY(owner) REFERENCES Client(base_id)
               )
    '''
    cursor.execute(delete_table_query)
    cursor.execute(create_table_query)
    connection.commit()
    connection.close()



def create_repair_hour_table():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    delete_table_query = 'DROP TABLE IF EXISTS RepairHour'
    create_table_query = '''
              CREATE TABLE RepairHour (
                    id INTEGER PRIMARY KEY,
                    date VARCHAR(50),
                    start_hour VARCHAR(20),
                    FOREIGN KEY(vehicle) REFERENCES Vehicle(id),
                    bill REAL,
                    FOREIGN KEY(mechanic_service) REFERENCES MechanicService(id) 
               )
    '''
    cursor.execute(delete_table_query)
    cursor.execute(create_table_query)
    connection.commit()
    connection.close()


def create_mechanic_service_table():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    delete_table_query = 'DROP TABLE IF EXISTS MechanicService'
    create_table_query = '''
              CREATE TABLE MechanicService (
                    id INTEGER PRIMARY KEY,
                    FOREIGN KEY(mechanic_id) REFERENCES Mechanic(base_id),
                    FOREIGN KEY(service_id) REFERENCES Service(id)
               )
    '''
    cursor.execute(delete_table_query)
    cursor.execute(create_table_query)
    connection.commit()
    connection.close()


def create_service_table():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    delete_table_query = 'DROP TABLE IF EXISTS Service'
    create_table_query = '''
              CREATE TABLE Service (
                    id INTEGER PRIMARY KEY,
                    name VARCHAR(50)
               )
    '''
    cursor.execute(delete_table_query)
    cursor.execute(create_table_query)
    connection.commit()
    connection.close()


def create_all_tables_in_correct_order():
    create_base_user_table()
    create_client_table()
    create_mechanic_table()
    create_vehicle_table()
    create_service_table()
    create_mechanic_service_table()
    create_repair_hour_table()


create_all_tables_in_correct_order()
