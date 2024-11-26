from collections import deque

registered_students = []
registration_queue = deque()

def registerStudent(name, age, subject):
    student = {"Name": name, "Age": age, "Subject": subject}
    registered_students.append(student)
    registration_queue.append(student)
    print(f"Student registered: {student}")

def undoRegistration():
    if registered_students:
        undone_student = registered_students.pop()
        registration_queue.remove(undone_student)
        print(f"Undone registration: {undone_student['Name']}")
    else:
        print("No student found to undo registration.")

def processRegistration():
    if registration_queue:
        student = registration_queue.popleft()
        print(f"Processing registration for: {student['Name']}")
    else:
        print("No student found for processing.")

registerStudent("Clement Mucyo", 20, "Computer Science")
registerStudent("Kevin Muhire", 22, "Engineering")
registerStudent("Patrice Mutsepe", 19, "Mathematics")
registerStudent("Akimana ", 21, "Physics")

undoRegistration()
undoRegistration()

processRegistration()
processRegistration()

print(f"All Registered Students: {registered_students}")
print(f"Registration Queue: {list(registration_queue)}")
