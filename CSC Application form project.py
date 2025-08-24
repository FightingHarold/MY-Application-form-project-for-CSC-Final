from tkinter import *


window = Tk()
window.title("School Application Form")
window.geometry("1000x900")


consent_var = BooleanVar()

def submit_application():
    full_name = name_entry.get()
    age = age_entry.get()
##    grade = grade.get()
    mother_name = mother_entry.get()
    father_name = father_entry.get()
    mother_occupation = mother_occupation_entry.get()
    father_occupation = father_occupation_entry.get()
    fees_amount = fees_entry.get()
    contact_number = contact_entry.get()
    address = address_entry.get()
    
    consent = consent_var

    if (consent==False):
        print("Consent is required to submit the application.")
    else:
        print("Consented to submit the application")

        file=("school_application.txt", "a")
        file.write("Application Form:\n")
        file.write("Full Name: {full_name}\n")
        file.write("Age: {age}\n")
##        file.write("Grade: {grade}\n")
        file.write("Mother's Name: {mother_name}\n")
        file.write("Father's Name: {father_name}\n")
        file.write("Mother's Occupation: {mother_occupation}\n")
        file.write("Father's Occupation: {father_occupation}\n")
        file.write("Fees Amount: {fees_amount}\n")
        file.write("Contact Number: {contact_number}\n")
        file.write("Address: {address}\n")
        file.write("\n")

    
    name_entry.delete(0, END)
    age_entry.delete(0, END)
####    grade.set("")
    mother_entry.delete(0, END)
    father_entry.delete(0, END)
    mother_occupation_entry.delete(0, END)
    father_occupation_entry.delete(0, END)
    fees_entry.delete(0, END)
    contact_entry.delete(0, END)
    address_text.delete("1.0", END)
    consent_var.set(False)  
    
    print("Application submitted successfully!")


name_label = Label(window, text="Full Name:")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = Entry(window)
name_entry.grid(row=0, column=1, padx=10, pady=10)

age_label = Label(window, text="Age:")
age_label.grid(row=1, column=0, padx=10, pady=10)
age_entry = Entry(window)
age_entry.grid(row=1, column=1, padx=10, pady=10)
##
##grade_label = Label(window, text="Grade:")
##grade_label.grid(row=2, column=0, padx=10, pady=10)
##grade_listbox = Listbox(window)
##grade_listbox.pack()
##for item in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]: grade_listbox.insert(END,item)
##grade.grid(row=2, column=1, padx=10, pady=10)

mother_label = Label(window, text="Mother's Name:")
mother_label.grid(row=3, column=0, padx=10, pady=10)
mother_entry = Entry(window)
mother_entry.grid(row=3, column=1, padx=10, pady=10)

father_label = Label(window, text="Father's Name:")
father_label.grid(row=4, column=0, padx=10, pady=10)
father_entry = Entry(window)
father_entry.grid(row=4, column=1, padx=10, pady=10)

mother_occupation_label = Label(window, text="Mother's Occupation:")
mother_occupation_label.grid(row=5, column=0, padx=10, pady=10)
mother_occupation_entry = Entry(window)
mother_occupation_entry.grid(row=5, column=1, padx=10, pady=10)

father_occupation_label = Label(window, text="Father's Occupation:")
father_occupation_label.grid(row=6, column=0, padx=10, pady=10)
father_occupation_entry = Entry(window)
father_occupation_entry.grid(row=6, column=1, padx=10, pady=10)

fees_label = Label(window, text="Fees Amount:")
fees_label.grid(row=7, column=0, padx=10, pady=10)
fees_entry = Entry(window)
fees_entry.grid(row=7, column=1, padx=10, pady=10)

contact_label = Label(window, text="Contact Number:")
contact_label.grid(row=8, column=0, padx=10, pady=10)
contact_entry = Entry(window)
contact_entry.grid(row=8, column=1, padx=10, pady=10)

address_label = Label(window, text="Address:")
address_label.grid(row=9, column=0, padx=10, pady=10)
address_entry = Entry(window)
address_entry.grid(row=9, column=1, padx=10, pady=10)

consent_checkbox = Checkbutton(window, text="I give my consent for my child to apply.")
consent_checkbox.grid(row=10, columnspan=2, padx=10, pady=10)


submit_button = Button(window, text="Submit Application", command=submit_application)
submit_button.grid(row=11, column=0, columnspan=2, padx=10, pady=10)


window.mainloop()


