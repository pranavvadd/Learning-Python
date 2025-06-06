class Student:

    count = 0
    total_gpa = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
    
    #Instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        return f"Average GPA of {cls.count} student/s is {cls.total_gpa / cls.count:.2f}" if cls.count > 0 else "No students enrolled."

student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)    
student3 = Student("Sandy", 4.0) 
student4 = Student("Squidward", 3.8)    
    
print(Student.get_count())
print(Student.get_average_gpa()) #Prints the average GPA of all students which is 3.07