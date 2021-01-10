#Ex 2 on db
import sqlite3, time, re

class Member:
    def __init__(self):
        pass
    def fast_query(self):
        while True:
            menu = input('''
            1-) Show data for existing DataBase
            2-) Create A database, show its contens
            3-) Exit Tool 
            ''')
            if menu == "1":
                print("ok.......")
                time.sleep(2)
                while True:
                    rex = (r"([A-Z]:\\)([A-z]+\\?)([A-z]+).db")
                    absulte = input("Enter database absolute path:=> ")
                    if absulte == "":
                        print("No value given")

                    elif re.search(rex, absulte):
                            print("ok.... Hold on!!")
                            time.sleep(2)
                            #Connect the database and show the files
                            try:
                                db = sqlite3.connect(absulte)
                                cr = db.cursor()
                                #Show with for loop
                                cr.execute("select * from user")
                                results = cr.fetchall()
                                print("Showing Data........")
                                for row in results:
                                    time.sleep(1)
                                    print(f"User_ID => {row[0]}, ", end=" ")
                                    print(f"UserName => {row[1]}")
                            except sqlite3.Error as error:
                                print(f"Error from dataBase ( '{error}')")
                                print("make sure every thing is right.......")
                            finally:
                                if (db):
                                    db.close()
                                    print("DataBase Closed............")
                                    print("Bye friend!!")
                                    break

                    else:
                        print("Enter  a valid absulote path, try again")
                        print(r"EXAMPLE {C:\python\file.db}")


            elif menu == "2":
                print("Ok.......")
                time.sleep(1)
                while True:
                    #Check absulute path
                    rex = (r"([A-Z]:\\)([A-z]+\\?)([A-z]+).db")
                    abslute0 = input("Enter your path you wanna save database in:# ")

                    if abslute0 == "":
                        print("No value given")

                    elif re.search(rex, abslute0):
                        print("Ok....... Hold on!!")
                        #Ceate DataBase
                        try:
                            db = sqlite3.connect(abslute0)
                            cr1 = db.cursor()
                            cr1.execute("create table if not exists Users(User_ID INTEGER, name TEXT)")
                            cr1.execute("create table if not exists Sports(Sport_ID INTEGER,  SportName TEXT)")
                            users = ["Osama", "Ahmed", "Ibrahim", "Asmaa", "Ibrahim", "Sayed", "Elzero", "Baloot"]
                            sports = ["Football", "Basketball", "Baseball", "Tennis", "Golf", "Skiing", "swimming",
                                      "WieghtLefting"]

                            for key, name in enumerate(users):
                                cr1.execute(f"INSERT INTO Users(User_ID, name) values({key + 1}, '{name}')")

                            for key1, sport in enumerate(sports):
                                cr1.execute(f"insert into Sports(Sport_ID, SportName) values({key1 + 1}, '{sport}')")
                            db.commit()

                            # Data base finished now show it
                            while True:
                                show = input("DataBase Created You wanna show it [y/n]")
                                if show == "n" or show == "N":
                                    print(f"Done!! DataBase saved in  %{abslute0}%")
                                    print("Ok, bye friend!!!")

                                    break
                                elif show == "y" or show == "Y":
                                    print("ok...... just Hold on!!")
                                    cr1.execute("select * from Users")
                                    results = cr1.fetchall()
                                    print("Showing Data........")
                                    for row in results:
                                        time.sleep(1)
                                        print(f"User_ID => {row[0]}, ", end=" ")
                                        print(f"UserName => {row[1]}")

                                    print("=" * 50)
                                    cr1.execute("select * from Sports")
                                    result = cr1.fetchall()
                                    print("Showing Data........")
                                    for row1 in result:
                                        time.sleep(1)
                                        print(f"User_ID => {row1[0]}, ", end=" ")
                                        print(f" SportName => {row1[1]}")
                                    break
                                else:
                                    print("NO value given, Try again")


                        except sqlite3.Error as error2:
                            print(f"Error from dataBase ( '{error2}')")
                            print("make sure every thing is right.......")
                        finally:
                            if (db):
                                db.close()
                                print("DataBase Closed")
                                break
                            print("Bye ya MAO!!")

                    else:
                        print("Enter  a valid absulote path, try again")
                        print(r"EXAMPLE {C:\python\file.db}")

            elif menu == "3":
                print("Bye!!")
                exit()
            else:
                print("Invalid option, Try again")

databases = Member()
print(databases.fast_query())



#Advanced Database Example

db = sqlite3.connect("I:\osama.db")
cr = db.cursor()
def commit_and_close():
    db.commit()
    db.close()
    print("Connection Terminated")

uid = 1

input_messege = '''
What Do You wanna do?
"s" => Show a skill
"a" => add a new skill
"d" => Delete a skill
"u" => Update a skill
"q" = > quit the system
Choose Option\n

'''
menu = input(input_messege).strip().lower()
command_list = ["s", "a", "d", "u", "q"]
#Define functions
def show_skills():
    cr.execute(f"select * from skills where user_id = '{uid}'")
    results = cr.fetchall()
    if len(results) == 0:
        print(f"You have no skills")

    else:
        print(f"You have {len(results)} skills")
        print("Showing Data......")
        for row in results:
            print(f" skill name => {row[0]}, ", end=" ")
            print(f"progress {row[1]}")



def add_skill():
    sk = input("Enter your Skill Name:# ").strip().capitalize()
    prog = input("Enter your progress:# ").strip()
    cr.execute(f"insert into SKILLS(name, progress, user_id) values('{sk}', '{prog}', '{uid}')") #Notice foramtters can be used in SQL Injection
    print("Done.....")

def delete_skill():
    sk = input("Enter your Skill Name:# ").strip().capitalize()
    cr.execute(f"delete from skills where name = '{sk}' and user_id = '{uid}'")  # Notice foramtters can be used in SQL Injection
    print("Done.....")
def update_skill():
    sk = input("Enter skill you wanna modify its progress:# ").strip().capitalize()
    cr.execute(f"select name from skills where name = '{sk}' and user_id = '{uid}' ")
    results = cr.fetchone()
    if results == None:
        prog = input("Enter your progress:# ").strip()
        cr.execute(
            f"insert into SKILLS(name, progress, user_id) values('{sk}', '{prog}', '{uid}')")  # Notice foramtters can be used in SQL Injection
        print("Done......")

        # cr.execute(f"update skills set progress = '{prog}' where name = '{sk}' and user_id = '{uid}'")

    elif results != None:
        print("Skill already in DB, try with another name")
        check = input("You wanna modify progress for this progress[y/n]")
        cr.execute(f"select name from skills where name = '{sk}' and user_id = '{uid}' ")

        if check == "y":
            prog = input("Enter your new progress:# ").strip()
            cr.execute(f"update skills set progress = '{prog}' where name = '{sk}' and user_id = '{uid}'")

        else:
            exit()


if menu in command_list:
    print(f"Ok command {menu} found")
    if menu == "s":
        show_skills()
        commit_and_close()
    elif menu == "a":
        add_skill()
        commit_and_close()
    elif menu == "d":
        delete_skill()
        commit_and_close()
    elif menu == "u":
        update_skill()
        commit_and_close()
    else:
        print("App Is closed")
        commit_and_close()
else:
    print(f"Sorry This \"{menu}\"  command not found")