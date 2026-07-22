#Create a dictionary of five students with their marks. Print all student names and marks.

students = {
    "Ayush": 95,
    "Rahul": 88,
    "Aman": 76,
    "Priya": 91,
    "Neha": 84
}

print("Student Marks")

for name, marks in students.items():
    print(name, ":", marks)