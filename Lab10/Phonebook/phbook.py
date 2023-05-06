import psycopg2, os
from config import database, host, password, user
running = True
def main():
    conn = None
    sql = ''
    
    try:

        conn = psycopg2.connect(
            host = host,
            database = database,
            user = user,
            password = password)

    
        conn.autocommit = True

       
        cur = conn.cursor()

       
        cur.execute("""
            CREATE TABLE IF NOT EXISTS phone_book (
                contact_name text,
                contact_number NUMERIC(20) PRIMARY KEY
            )
        """)
        
        command = input("Choose:\n        M - My contacts list\n        I - Insert New Contact\n        CSV - Upload data from CSV file\n        C(1|2) - Change Contact Name(1) or Number(2)\n        S(1|2) - Search Contact Name(1) or Number(2)\n        D(1|2) - Delete Contact Name(1) or Number(2)\n        0 - Quite program\n MY CHOICE: ")
        
        if command == 'M':
            cur.execute("""SELECT * FROM phone_book""")
            for contact in cur:
                print(contact)
        # Insert 
        if command == 'I':
            sql = """INSERT INTO phone_book(contact_name, contact_number)
                     VALUES(%s,%s);"""
            name = input("Enter Contact Name: \n")
            number = input("Enter Contact Number: \n")
            cur.execute(f"""SELECT EXISTS (SELECT * FROM phone_book WHERE contact_number = {number})""")
            if not cur.fetchone()[0]:
                cur.execute(sql,(name, number))
                print("Your Contact Saved Successfully!\n")
            else:
                print("Such contact with same number already exists.")
            
        
        if command == "CSV":
            path = input("Enter full path to 'csv' file:")
            if os.path.exists(f'{path}'):
                cur.execute(f"""
                            COPY phone_book(contact_name, contact_number)
                            FROM '{path}'
                            DELIMITER ','
                            CSV HEADER
                            """)
                print("CSV file was successfully uploaded!\n")
            else:
                print("Incorrect path!")
            
      

        # Update
        elif command == 'C1':
            change = input("Change: ")
            #check the name
            cur.execute(f"""SELECT EXISTS (SELECT * FROM phone_book WHERE contact_name = '{change}')""")
            if cur.fetchone()[0]:
                to = input("To: ")
                cur.execute(f"""UPDATE phone_book
                SET contact_name = '{to}' 
                WHERE contact_name = '{change}';""")
                print("Your Updating Saved Successfully!\n")
            else:
                print("there is no such contact in the database.")

        elif command == 'C2':
            change = input("Name: ")
            #checking
            cur.execute(f"""SELECT EXISTS (SELECT * FROM phone_book WHERE contact_name = '{change}')""")
            if cur.fetchone()[0]:
                to = input("New Number: ")
                cur.execute(f"""UPDATE phone_book
                SET contact_number = {to} 
                WHERE contact_name = '{change}';""")
                print("Your Updating Saved Successfully!\n")
            else:
                print("there is no such contact in the database.")

        
        elif command == 'S1':
            n = input("Contact Name: ")
            cur.execute(f"""SELECT * FROM phone_book WHERE contact_name = '{n}';""")
            print(f"{n}'s Contact Number:", cur.fetchone()[1])

        elif command == 'S2':
            n = input("Contact Number: ")
            cur.execute(f"""SELECT * FROM phone_book WHERE contact_number = {n};""")
            print(f"It's {cur.fetchone()[0]}'s Contact Number")
        elif command == 'D1':
            n = input("Contact Name: ")
            cur.execute(f"""DELETE FROM phone_book WHERE contact_name = '{n}'""")
            print("Removing Succesfully Finished!")
        elif command == 'D2':
            n = input("Contact Number: ")
            cur.execute(f"""DELETE FROM phone_book WHERE contact_number = {n}""")
            print("Removing Succesfully Finished!")
        elif command == '0':
            global running
            running = False

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
           


if __name__ == '__main__':
        while running:
            main()