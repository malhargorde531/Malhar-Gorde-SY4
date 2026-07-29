# Patient Class
class Patient:
    def __init__(self, patient_id, name, treatment_cost):
        self.patient_id = patient_id
        self.name = name
        self.treatment_cost = treatment_cost

    # Categorize patient
    def category(self):
        if self.treatment_cost >= 5000:
            return "Special"
        else:
            return "General"


# Hospital Class
class Hospital:
    def __init__(self):
        self.patients = []

    # Add patient
    def add_patient(self, patient):
        self.patients.append(patient)

    # Display all patient records
    def display_patients(self):
        print("\nPatient Records")
        print("-" * 50)
        for patient in self.patients:
            print("Patient ID     :", patient.patient_id)
            print("Name           :", patient.name)
            print("Treatment Cost : ₹", patient.treatment_cost)
            print("Category       :", patient.category())
            print("-" * 50)


# Main Program
hospital = Hospital()

n = int(input("Enter number of patients: "))

for i in range(n):
    print(f"\nEnter details of Patient {i+1}")
    patient_id = input("Patient ID: ")
    name = input("Name: ")
    treatment_cost = float(input("Treatment Cost: "))

    patient = Patient(patient_id, name, treatment_cost)
    hospital.add_patient(patient)

# Display all records
hospital.display_patients()