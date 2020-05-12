import json
from os import system as cmd
cmd('color 1')
def get_average(marks): 
    total_sum = sum(marks) 
    total_sum = float(total_sum) 
    return total_sum / len(marks) 

def calculate_total_average(students): 
    assignment = get_average(students["assignment"]) 
    test = get_average(students["test"]) 
    lab = get_average(students["lab"])     
    return 0.1 * assignment + 0.7 * test + 0.2 * lab 
  
   
def assign_letter_grade(score): 
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 60: return "C"
    elif score >= 40: return "D"
    else : return "E"
  
def class_average_is(student_list): 
    result_list = []   
    for student in student_list: 
        stud_avg = calculate_total_average(student) 
        result_list.append(stud_avg) 
        return get_average(result_list) 
while True:
    cmd('cls')
    print("""
    select from following
    1. Read Student Detial from JSON file
    2. Enter Student Detial 
    3. Exit
    """)
    selected=input('>> ')
    if selected=='1':
        cmd('cls')
        with open('C:/Users/pradeep suthar/Desktop/GPA/students.json','r') as data:
            student_data=json.load(data)
        students=[]
        for i in student_data["student"]:
            students.append(i)
        for i in students: 
            print(i["name"]) 
            print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=") 
            print("Average marks of %s is : %s " %(i["name"],
                        calculate_total_average(i))) 

            print("Letter Grade of %s is : %s" %(i["name"], 
                        assign_letter_grade(calculate_total_average(i)))) 
    
            print() 
    
        class_av = class_average_is(students) 
    
        print( "Class Average is %s" %(class_av)) 
        print("Letter Grade of the class is %s " 
                %(assign_letter_grade(class_av)))
        input('press any key to continue >>')
    elif selected=='2':
        cmd('cls')
        name=input('Enter Name of Student : ')
        assignment,test,lab=[],[],[]
        print('enter space seprated assignment marks : ')
        assignment=list(map(int,input().split())) 
        print('enter space seprated test marks : ')
        test=list(map(int,input().split()))
        print('enter space seprated lab marks : ')
        lab=list(map(int,input().split()))
        student={ 
                 "name":name, 
                 "assignment":assignment, 
                 "test": test, 
                 "lab" : lab
            }
        print(student["name"]) 
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=") 
        print("Average marks of %s is : %s " %(student["name"],
                            calculate_total_average(student))) 
        print("Letter Grade of %s is : %s" %(student["name"],
                    assign_letter_grade(calculate_total_average(student)))) 
        print() 
        input('press any key to continue >>')
    elif selected=='3':
        exit()
    else:
        continue