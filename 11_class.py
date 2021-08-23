class Student:
    def __init__(self, name, fatherName, gender):
        self.name = name
        self.fatherName = fatherName
        self.gender = gender

    def Data(self):
        print("Name : ", self.name)
        print("Father Name : ", self.fatherName)
        print("Gender : ", self.gender)

ali = Student("Ali Khan", "Basit Khan", "M")
ali.Data()

        