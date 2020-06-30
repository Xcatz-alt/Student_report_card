
print("===========================")
print("Report card grades")
print("===========================")
ads = False
student = []

while True:
    name = input("Enter your student name: ")
    data1 = int(input("Enter Math Grades: "))
    data2 = int(input("Enter Science Grades: "))
    data3 = int(input("Enter History Grades: "))
    data4 = int(input("Enter PE Grades: "))

    student.append({
        "name": name,
        "Math": data1,
        "Science": data2,
        "History": data3,
        "PE": data4,
    })
 
    ulang = input("Input another data?:(Y/N)")
    if ulang == "N":
        break
    elif ulang == "n":
        break

print("===========================")
print("Data that you just Input")
print(student)
print("===========================")

def prosess():
    xd = str(input("Enter the name: "))

    def sum_nilai(student):
        total_nilai = 0
        for key, val in student.items():
            if type(val) == int:
                total_nilai += val
        return total_nilai

    for data in student:
        if data["name"] == xd:
            print(data)
            dak = sum_nilai(data)
            sad = dak / 4
            print("Total: ",dak)
            print("Average value: ",sad)

    ulang = input("Do you want to enter another name?y/n:")
    while ulang == "y":
        prosess()
        break
    else:
        print("Thank you")

prosess()