import sqlite3
import csv


def delete_data():
    '''
    connects to the customers databse and deletes the data. the chnages are commited and conenction is closed.
    a message prints that this was successful.
    :return: nothing
    '''
    conn = sqlite3.connect('customers.sqlite')
    c = conn.cursor()
    query = """DELETE FROM Customer;"""
    c.execute(query)
    conn.commit()
    conn.close()
    print("All old rows were deleted.")


def add_data():
    '''
    first creates an empty list to hold the data in
    opens the file and also connects to database
    adds a zip column as that column is not there intially
    closes the database for now

    the very first row in the csv file is removed, and in a for lopp, the rest of the data is added to the empty list created
    the databse is opened again
    values fro mthe list are assigned variable
    an SQl f-string query is created to add in all od this data and is executed.
    the data is commited and the database is closed.

    A variable to keep track of the number of rows inserted is created
    A query selects the COUNT from customers and is assigned to the COUNT value returned
    formatting and f-atrings are used to print out how many rows were inserted

    :return: nothing
    '''
    try:
        row_list = []
        with open("customers.csv", "r", newline="") as file:
            reader = csv.reader(file)
            conn = sqlite3.connect("customers.sqlite")
            c = conn.cursor()
            query = """ALTER TABLE Customer ADD COLUMN zip TEXT;"""
            c.execute(query)
            conn.commit()
            conn.close()
            for row in reader:
                row_list.append(row)

            row_list.pop(0)
            for row in row_list:
                conn = sqlite3.connect('customers.sqlite')
                c = conn.cursor()
                first_name = row[0]
                last_name = row[1]
                business_name = row[2]
                address = row[3]
                city = row[4]
                state = row[5]
                zip = row[6]
                query = f"""INSERT INTO Customer (firstName,lastName,companyName,address,city,state, zip) VALUES ('{first_name}', '{last_name}', '{business_name}', '{address}', '{city}', '{state}', '{zip}');"""
                c.execute(query)
                conn.commit()
                conn.close()
            num_rows = 0
            conn = sqlite3.connect('customers.sqlite')
            c = conn.cursor()
            query = """SELECT COUNT (*) FROM Customer;"""
            c.execute(query)
            num_rows = c.fetchall()
            print(f"{num_rows[0][0]} rows were inserted.")
    except ValueError as e:
        print(e)


def main():
    '''
    function that deletes the data is called, followed by thr function to add data from the CSV file.
    :return: nothing
    '''
    delete_data()
    add_data()

if __name__ == '__main__':
    main()