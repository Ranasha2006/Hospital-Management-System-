import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="HOSPITAL"
)

cursor=conn.cursor()

def create_doctor(DOCTOR_ID,FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUMBER,SPECIALIZATION,QUALIFICATION,REGISTRATION_NUMBER):
    query="INSERT INTO DOCTOR(DOCTOR_ID,FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUMBER,SPECIALIZATION,QUALIFICATION,REGISTRATION_NUMBER)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    
    cursor.execute(query,(DOCTOR_ID,FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUMBER,SPECIALIZATION,QUALIFICATION,REGISTRATION_NUMBER))

    conn.commit()
    print("Doctor created successsfully")

def read_doctor():
    cursor.execute("SELECT * FROM DOCTOR")
    for(DOCTOR_ID,FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUMBER,SPECIALIZATION,QUALIFICATION,REGISTRATION_NUMBER)in cursor.fetchall():
        print(f"DOCTOR_ID:{DOCTOR_ID},FIRST_NAME:{FIRST_NAME},EMAIL:{EMAIL},PHONE_NUMBER:{PHONE_NUMBER},SPECILIZATION:{SPECIALIZATION},QUALIFICATION:{QUALIFICATION},REGISTRATION_NUMBER:{REGISTRATION_NUMBER}")

def update_doctor(DOCTOR_ID,FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUMBER,SPECIALIZATION,QUALIFICATION,REGISTRATION_NUMBER):
     query="UPDATE DOCTOR SET FIRST_NAME=%s,LAST_NAME=%s,EMAIL=%s,PHONE_NUMBER=%s,SPECIALIZATION=%s,QUALIFICATION=%s,REGISTRATION_NUMBER=%s WHERE DOCTOR_ID=%s"
                  
     cursor.execute(query,(FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUMBER,SPECIALIZATION,QUALIFICATION,REGISTRATION_NUMBER,DOCTOR_ID))
     conn.commit()
     print("doctor updated succesfully")

def delete_doctor(DOCTOR_ID):
    query="DELETE FROM DOCTOR WHERE DOCTOR_ID=%s"
    cursor.execute(query,(DOCTOR_ID,))
    conn.commit()
    print("Doctor deleted successfully")


def create_patient(PATIENT_ID,FULL_NAME,DOB,GENDER,PHONE_NUMBER,ADDRESS,BLOOD_TYPE):
    query="INSERT INTO PATIENT (PATIENT_ID,FULL_NAME,DOB,GENDER,PHONE_NUMBER,ADDRESS,BLOOD_TYPE)VALUES(%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(PATIENT_ID,FULL_NAME,DOB,GENDER,PHONE_NUMBER,ADDRESS,BLOOD_TYPE))
    conn.commit()
    print("Patient created successfully")

def read_patient():
    cursor.execute("SELECT * FROM PATIENT")
    for(PATIENT_ID,FULL_NAME,DOB,GENDER,PHONE_NUMBER,ADDRESS,BLOOD_TYPE) in cursor.fetchall():
        print(f"PATIENT_ID:{PATIENT_ID},FULL_NAME:{FULL_NAME},DOB:{DOB},GENDER:{GENDER},PHONE_NUMBER:{PHONE_NUMBER},ADDRESS:{ADDRESS},BLOOD_TYPE:{BLOOD_TYPE}")

def update_patient(PATIENT_ID,FULL_NAME,DOB,GENDER,PHONE_NUMBER,ADDRESS,BLOOD_TYPE):
    query="UPDATE PATIENT SET FULL_NAME=%s,DOB=%s,GENDER=%s,PHONE_NUMBER=%s,ADDRESS=%s,BLOOD_TYPE=%s WHERE PATIENT_ID=%s"
    cursor.execute(query(FULL_NAME,DOB,GENDER,PHONE_NUMBER,ADDRESS,BLOOD_TYPE))
    conn.commit()
    print("Patient updated successfully")

def delete_patient(PATIENT_ID):
    query="DELETE FROM PATIENT WHERE PATIENT_ID=%s"
    cursor.execute(query,(PATIENT_ID,))
    conn.commit()
    print("Patient deleted successfully")

    
def create_appointment(APPOINTMENT_ID,DOCTOR_ID,PATIENT_ID,APPOINTMENT_DATE,APPOINTMENT_TIME,REASON,STATUS):
    query="INSERT INTO APPOINTMENT(APPOINTMENT_ID,DOCTOR_ID,PATIENT_ID,APPOINTMENT_DATE,APPOINTMENT_TIME,REASON,STATUS)VALUES(%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(APPOINTMENT_ID,DOCTOR_ID,PATIENT_ID,APPOINTMENT_DATE,APPOINTMENT_TIME,REASON,STATUS))
    conn.commit()
    print("Appointment created successfully")

def read_appointment():
    cursor.execute("SELECT * FROM APPOINTMENT")
    for(APPOINTMENT_ID,DOCTOR_ID,PATIENT_ID,APPOINTMENT_DATE,APPOINTMENT_TIME,REASON,STATUS)in cursor.fetchall():
        print(f"APPOINTMENT_ID:{APPOINTMENT_ID},DOCTOR_ID:{DOCTOR_ID},PATIENT_ID:{PATIENT_ID},APPOINTMENT_DATE:{APPOINTMENT_DATE},APPOINTMENT_TIME:{APPOINTMENT_TIME},REASON:{REASON},STATUS:{STATUS}")

def update_appointment(APPOINTMENT_ID,DOCTOR_ID,PATIENT_ID,APPOINTMENT_DATE,APPOINTMENT_TIME,REASON,STATUS):
    query="UPDATE APPOINTMENT SET DOCTOR_ID=%s,PATIENT_ID=%s,APPOINTMENT_DATE=%s,APPOINTMENT_TIME=%s,REASON=%S,STATUS=%s WHERE APPOINTMENT_ID=%s"
    
    cursor.execute(query,(DOCTOR_ID,PATIENT_ID,APPOINTMENT_DATE,APPOINTMENT_TIME,REASON,STATUS,APPOINTMENT_ID))
    conn.commit()
    print("Appointment updated successfully")
    
def delete_appointment(APPOINTMENT_ID):
    query="DELETE FROM APPOINTMENT WHERE APPOINTMENT_ID=%s"
    cursor.execute(query,(APPOINTMENT_ID,))
    conn.commit()
    print("Appointment deleted successfully")    
    
    
    

    
                   
def main():
    while True:
        print("\n--- CRUD Menu ---")
        print("1. Create DOCTOR")
        print("2. Read DOCTOR")
        print("3. Update DOCTOR")
        print("4. Delete DOCTOR")
        print("5. Create patient")
        print("6. Read patient")
        print("7. Update patient")
        print("8. Delete patient")
        print("9. Create Appointment")
        print("10.Read Appointment")
        print("11.Update appointment")
        print("12.Delete appointment")
        print("13.Exit")
        
        choice = input("Enter choice: ")


        if choice == "1":
            DOCTOR_ID=int(input("Enter the id"))
            FIRST_NAME = input("Enter First name: ")
            LAST_NAME=input("Enter Last name")
            EMAIL = input("Enter email: ")
            PHONE_NUMBER=int(input("Enter the contact number"))
            SPECIALIZATION=input("Enter the specialization")
            QUALIFICATION=input("Enter the qualification")
            REGISTRATION_NUMBER=int(input("Enter the registration number"))
           

            create_doctor(DOCTOR_ID,FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUMBER,SPECIALIZATION,QUALIFICATION,REGISTRATION_NUMBER)
    

        elif choice == "2":
            read_doctor()

        elif choice == "3":
            DOCTOR_ID= int(input("Enter user ID to update: "))
            FIRST_NAME = input("Enter new name: ")
            LAST_NAME=input("Enter the last name")
            EMAIL = input("Enter new email: ")
            PHONE_NUMBER=int(input("Enter the contact number"))
            SPECIALIZATION=input("Enter the specialization")
            QUALIFICATION=input("Enter the qualification")
            REGISTRATION_NUMBER=int(input("Enter the number"))                

            update_doctor(DOCTOR_ID,FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUMBER,SPECIALIZATION,QUALIFICATION,REGISTRATION_NUMBER)

        elif choice == "4":
            DOCTOR_ID= int(input("Enter DOCTOR ID to delete: "))

            delete_doctor(DOCTOR_ID)

        if choice == "5":
            PATIENT_ID=int(input("Enter the id"))
            FULL_NAME = input("Enter First name: ")
            DOB=input("Enter the dob number")
            GENDER=input("Enter the gender name")
            PHONE_NUMBER=int(input("Enter the contact number"))
            ADDRESS=input("Enter the address")
            BLOOD_TYPE=input("Enter the group name")
           

            create_patient(PATIENT_ID,FULL_NAME,DOB,GENDER,PHONE_NUMBER,ADDRESS,BLOOD_TYPE)
    

        elif choice == "6":
            read_patient()

        elif choice == "7":
            PATIENT_ID= int(input("Enter user ID to update: "))
            FULL_NAME = input("Enter new name: ")
            DOB=input("Enter the dob:")
            GENDER=input("Enter the gender name")
            PHONE_NUMBER=input("Enter the contact number")
            ADDRESS=input("Enter the address")
            BLOOD_TYPE=input("Enter the group name")

            update_patient(PATIENT_ID,FULL_NAME,DOB,GENDER,PHONE_NUMBER,ADDRESS,BLOOD_TYPE)

        elif choice == "8":
            PATIENT_ID= int(input("Enter PATIENT ID to delete: "))

            delete_patient(PATIENT_ID)


        if choice == "9":
            APPOINTMENT_ID=int(input("Enter the appointment id"))
            DOCTOR_ID=int(input("Enter the doctor id"))
            PATIENT_ID=int(input("Enter the patient id number"))
            APPOINTMENT_DATE=input("Enter the DATE")
            APPOINTMENT_TIME=input("Enter the TIME ")
            REASON=input("Enter the reason")
            STATUS=input("Enter the status")               
           

            create_appointment(APPOINTMENT_ID,DOCTOR_ID,PATIENT_ID,APPOINTMENT_DATE,APPOINTMENT_TIME,REASON,STATUS)
    

        elif choice == "10":
            read_appointment()

        elif choice == "11":
            APPOINTMENT_ID=int(input("Enter the id"))
            DOCTOR_ID= int(input("Enter user ID to update: "))
            PATIENT_ID=int(input("Enter the id"))                   
            APPOINTMENT_DATE=int(input("Enter the number"))
            APPOINTMENT_TIME=int(input("Enter the number"))
            REASON=input("Enter the reason")
            STATUS=input("Enter the status")                   

            update_appointment(APPOINTMENT_ID,DOCTOR_ID,PATIENT_ID,APPOINTMENT_DATE,APPOINTMENT_TIME,REASON,STATUS)

        elif choice == "12":
            APPOINTMENT_ID= int(input("Enter APPOINTMENT ID to delete: "))

            delete_appointment(APPOINTMENT_ID)    

        elif choice == "13":
            break

          


    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()

    

                   
