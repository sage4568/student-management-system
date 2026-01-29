import csv
rec_fields=('roll', 'name', 'age', 'email', 'phone')
sms_database='student.csv'
def show_menu():
    print('..............................')
    print('welcome to school managment system')
    print('....................................')
    print("1. add new student")
    print("2. view student")
    print("3. search student")
    print("4. update student")
    print("5. delete student")
    print("6. quit")
def create_record():
    print("......................")
    print("add student information")
    print("............................")
    global rec_fields
    global sms_database
    stud_data=[]
    for field in rec_fields:
        value=input(field +":")
        stud_data.append(value)

    with open(sms_database, "a", encoding="utf-8") as f:
        writer= csv.writer(f)
        writer.writerows([stud_data])
    print("data saved succesfully")
    input("press any key to continue")
    return
def display_student():
    global rec_fields
    global sms_database
    print("......student records.........")
    with open(sms_database, "r", encoding="utf-8") as f:
        reader=csv.reader(f)
        for k in rec_fields:
            print(k, end='\t |')
        print("\n......................................................")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("press any key to continou")



def search_student():
    global rec_fields
    global sms_database
    print("............. search student............")
    roll=input("enter roll.no. to search: ")
    with open(sms_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    print("..........student found..........")
                    print("roll:",row[0])
                    print("name:",row[1])
                    print("age:",row[2])
                    print("email:",row[3])
                    print("phone:",row[4])
                    break
            else:
                print("roll no. not found in our database")
            input("press any key to continue")
def update_student():
    global rec_fields
    global sms_database
    print("..........update_sudent.........")
    roll=input("enterbroll no. to update: ")
    idx_student=None
    update_rec=[]
    with open (sms_database, "r", encoding="utf-8") as f:
        reader=csv.reader(f)
        counter=0
        for row in reader:
            if len(row)>0:
                idx_student=counter
                print("student found: at index", idx_student)
                stud_data=[]
                for field in rec_fields:
                    value=input(field + ":")
                    stud_data.append(value)
                update_rec.append(stud_data)
            else:
                update_rec.append(row)
            counter+=1
    if idx_student is not None:
        with open (sms_database, "w", encoding="utf-8") as f:
            writer=csv.writer(f)
            writer.writerow(update_rec)
    else:
        print("roll no. not found in our database")
    input("press any key to continou")


def delete_student():
    global rec_fields
    global sms_database
    print("..........delete_sudent.........")
    roll=input("enterbroll no. to delete: ")
    stud_locate=False
    update_rec=[]
    with open (sms_database, "r", encoding="utf-8") as f:
        reader=csv.reader(f)
        counter=0
        for row in reader:
            if len(row)>0:
                if roll !=row[0]:
                    update_rec.append(row)
                    counter+=1
            else:
                stud_locate=True
    if stud_locate is True:
        with open (sms_database,"w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(update_rec)
        print("roll no.", roll, "deleted successfully")
    else:
        print("roll no. is not found in our database")
    input("press any key to continue")
while True:
    show_menu()
    choose = input("enter your choose: ")
    if choose == "1":
        create_record()
    if choose == "2":
        display_student()
    if choose == "3":
        search_student()
    if choose == "4":
        update_student()
    if choose == "5":
        delete_student()
    else:
        break

print(".........................")
print("T H A N K  Y O U")
print(".........................")
