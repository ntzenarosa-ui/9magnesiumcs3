#Creates Patient class
class Patient:
    def __init__(self, name, bill_amount): #initialize name and bill amount
        self.name = name
        self.set_bill_amount(bill_amount)
    
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
    
    def get_bill_amount(self):
        return self._bill_amount
    
    def set_bill_amount(self, bill_amount):
        if bill_amount >= 0:
            self.bill_amount = bill_amount
        else:
            self.bill_amount = 0

    #Display and calculate orginal and final bill amount
    def calculate_bill(self):
        print(f"Original Bill: {self.bill_amount:.2f}")
        print(f"Final Bill: {self.bill_amount:.2f}")

    #Display Patient's type
    def display_patient_type(self):
        print("Patient type: Regular Patient")

#Creates Senior Citizen class
class Senior(Patient):
    #Display orginal and final bill amount with 20% deduction for final bill
    def calculate_bill(self):
        print(f"Original Bill: {self.bill_amount:.2f}")
        print(f"Final Bill: {self.bill_amount*0.8:.2f}")

    #Display Patient's type
    def display_patient_type(self):
        print("Patient type: Senior Citizen") 

#Creates PhilHealth Members class
class PhilHealth(Patient):
    #Display orginal and final bill amount with 15% deduction for final bill
    def calculate_bill(self):
        print(f"Original Bill: {self.bill_amount:.2f}")
        print(f"Final Bill: {self.bill_amount*0.85:.2f}")

    #Display Patient's type
    def display_patient_type(self):
        print("Patient type: PhilHealth Member")

#Creates objects
patient1 = Patient("Eren Yeager", 15000)
patient2 = Patient("Floch Forster", 100000000000000000)
patient_senior1 = Senior("Keith Shadis", 15000)
patient_senior2 = Senior("Theo Magath", 90000)
patient_philhealth1 = PhilHealth("Pieck Finger", 100)
patient_philhealth2 = PhilHealth("Reiner Braun", 104000)
patient3 = Patient("Sasha Braus", -67)
patient_senior3 = Senior("Dot Pyxis", -50)
patient_philhealth3 = PhilHealth("Ymir Fritz", -101010101010)

#Output using for loop to execute the methods of each object
patients = [patient1, patient2, patient3, patient_senior1, patient_senior2, patient_senior3, patient_philhealth1, patient_philhealth2, patient_philhealth3]
for patient in patients:
    print(f"Patient Name: {patient.get_name()}")
    patient.display_patient_type()
    patient.calculate_bill()
    print ("")
