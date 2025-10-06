class Student:
    """
    Represents a student with a name, age, and a list of marks.
    """

    def __init__(self, name, age, marks):
        """
        Initialize a Student instance.

        Args:
            name (str): The student's name.
            age (int): The student's age.
            marks (list of int): List of marks for the student.
        """
        self.name = name
        self.age = age
        self.marks = marks

    def show_details(self):
        """
        Prints the student's name and age in a readable format.
        """
        print(f"Name: {self.name}, Age: {self.age}")

    def total_marks(self):
        """
        Returns the total of the student's marks.

        Returns:
            int: Sum of all marks.
        """
        return sum(self.marks)