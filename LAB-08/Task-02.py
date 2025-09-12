class sru_student:
    def __init__(self, name, roll_no, hostel_status):
        self.name = name
        self.roll_no = roll_no
        self.hostel_status = hostel_status
        self.fee_paid = False
    
    def fee_update(self, status):
        self.fee_paid = status
        if status:
            print(f"Fee payment confirmed for {self.name}")
        else:
            print(f"Fee payment pending for {self.name}")
    
    def display_details(self):
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print(f"Hostel Status: {self.hostel_status}")
        print(f"Fee Status: {'Paid' if self.fee_paid else 'Pending'}")

student1 = sru_student("John Doe", "SRU2024001", "Day Scholar")
student2 = sru_student("Jane Smith", "SRU2024002", "Hostel")

student1.display_details()
print()
student2.display_details()
print()

student1.fee_update(True)
student2.fee_update(False)
