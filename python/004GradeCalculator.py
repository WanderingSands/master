#!/usr/bin/python3.6

print("Welcome to the calculator that will compare student grades to other students ")
print("in a basic manner. You will be asked for the names of three (3) students,")
print("then you will be asked how many assignments a student had in a specific")
print("course. Afteter this you will be asked to input the grade. Please use whole")
print("numbers (Do not use fractions or decimals). I hope you find this calculator")
print("interesing. Sorry for the lack of whitespace.")
print("")

Student1=input("What is the first studnet's name? ")
Student2=input("What is the second student's name? ")
Student3=input("What is the third student's name? ")

#Student 1, Science
Assign1=int(input("How many assignments did {} have in Science? ".format(Student1)))
S1gradesEE=list()
count=1
while count <= Assign1:
    S1gradesEE.append(int(input('What is the grade for assignment {}? '.format(count))))
    count=count+1
print("For Science {} had the grades of {} out of {} assignments".format(Student1, S1gradesEE, Assign1))
AvgGrS1EE=sum(S1gradesEE)//len(S1gradesEE)
print("The average grade for {} in Science was {}%.".format(Student1, AvgGrS1EE))
#Student 1, French
Assign2=int(input("How many assignments did {} have in French? ".format(Student1)))
S1gradesFR=list()
count=1
while count <= Assign2:
    S1gradesFR.append(int(input('What is the grade for assignment {} in French? '.format(count))))
    count=count+1
print("For French {} had the grades of {} out of {} assignments".format(Student1, S1gradesFR, Assign2))
AvgGrS1FR=sum(S1gradesFR)//len(S1gradesFR)
print("The average grade for {} in French was {}%.".format(Student1, AvgGrS1FR))
#Student 1, Geography
Assign3=int(input("How many assignments did {} have in Geography? ".format(Student1)))
S1gradesGE=list()
count=1
while count <= Assign3:
    S1gradesGE.append(int(input('What is the grade for assignment {}? '.format(count))))
    count=count+1
print("For Geography {} had the grades of {} out of {} assignments".format(Student1, S1gradesGE, Assign3))
AvgGrS1GE=sum(S1gradesGE)//len(S1gradesGE)
print("The average grade for {} in Geography was {}%.".format(Student1, AvgGrS1GE))


#Student 2, Science
AssignS2_1=int(input("How many assignments did {} have in Science? ".format(Student2)))
S2gradesEE=list()
count=1
while count <= AssignS2_1:
    S2gradesEE.append(int(input('What is the grade for assignment {}? '.format(count))))
    count=count+1
print("For Science {} had the grades of {} out of {} assignments".format(Student2, S2gradesEE, AssignS2_1))
AvgGrS2EE=sum(S2gradesEE)//len(S2gradesEE)
print("The average grade for {} in Science was {}%.".format(Student2, AvgGrS2EE))
#Student 2, French
AssignS2_2=int(input("How many assignments did {} have in French? ".format(Student2)))
S2gradesFR=list()
count=1
while count <= AssignS2_2:
    S2gradesFR.append(int(input('What is the grade for assignment {} in French? '.format(count))))
    count=count+1
print("For French {} had the grades of {} out of {} assignments".format(Student2, S2gradesFR, AssignS2_2))
AvgGrS2FR=sum(S2gradesFR)//len(S2gradesFR)
print("The average grade for {} in French was {}%.".format(Student2, AvgGrS2FR))
#Student 2, Geography
AssignS2_3=int(input("How many assignments did {} have in Geography? ".format(Student2)))
S2gradesGE=list()
count=1
while count <= AssignS2_3:
    S2gradesGE.append(int(input('What is the grade for assignment {}? '.format(count))))
    count=count+1
print("For Geography {} had the grades of {} out of {} assignments".format(Student2, S2gradesGE, AssignS2_3))
AvgGrS2GE=sum(S2gradesGE)//len(S2gradesGE)
print("The average grade for {} in Geography was {}%.".format(Student2, AvgGrS2GE))

#Student 3, Science182
AssignS3_1=int(input("How many assignments did {} have in Science? ".format(Student3)))
S3gradesEE=list()
count=1
while count <= AssignS3_1:
    S3gradesEE.append(int(input('What is the grade for assignment {}? '.format(count))))
    count=count+1
print("For Science {} had the grades of {} out of {} assignments".format(Student3, S3gradesEE, AssignS3_1))
AvgGrS3EE=sum(S3gradesEE)//len(S3gradesEE)
print("The average grade for {} in Science was {}%.".format(Student3, AvgGrS3EE))
#Student 3, French
AssignS3_2=int(input("How many assignments did {} have in French? ".format(Student3)))
S3gradesFR=list()
count=1
while count <= AssignS3_2:
    S3gradesFR.append(int(input('What is the grade for assignment {} in French? '.format(count))))
    count=count+1
print("For French {} had the grades of {} out of {} assignments".format(Student3, S3gradesFR, AssignS3_2))
AvgGrS3FR=sum(S3gradesFR)//len(S3gradesFR)
print("The average grade for {} in French was {}%.".format(Student3, AvgGrS3FR))
#Student 3, Geography
AssignS3_3=int(input("How many assignments did {} have in Geography? ".format(Student3)))
S3gradesGE=list()
count=1
while count <= AssignS3_3:
    S3gradesGE.append(int(input('What is the grade for assignment {}? '.format(count))))
    count=count+1
print("For Geography {} had the grades of {} out of {} assignments".format(Student3, S3gradesGE, AssignS3_3))
AvgGrS3GE=sum(S3gradesGE)//len(S3gradesGE)
print("The average grade for {} in Geography was {}%.".format(Student3, AvgGrS3GE))

#condition for an A
#Student1
if AvgGrS1EE > 70:
    print("{} gets an A for Science for having a {}%".format(Student1, AvgGrS1EE))
else:
    print("{} does not get an A for a {}% in Science 128".format(Student1, AvgGrS1EE))
if AvgGrS1FR > 70:
    print("{} gets an A for French for having a {}%".format(Student1, AvgGrS1FR))
else:
    print("{} does not get an A for a {}% in French".format(Student1, AvgGrS1FR))
if AvgGrS1GE > 70:
    print("{} gets an A for Geography for having a {}%".format(Student1, AvgGrS1GE))
else:
    print("{} does not get an A for a {}% in Geography".format(Student1, AvgGrS1GE))
#Student2
if AvgGrS2EE > 70:
    print("{} gets an A for Science for having a {}%".format(Student2, AvgGrS2EE))
else:
    print("{} does not get an A for a {}% in Science 128".format(Student2, AvgGrS2EE))
if AvgGrS2FR > 70:
    print("{} gets an A for French for having a {}%".format(Student2, AvgGrS2FR))
else:
    print("{} does not get an A for a {}% in French".format(Student2, AvgGrS2FR))
if AvgGrS2GE > 70:
    print("{} gets an A for Geography for having a {}%".format(Student2, AvgGrS2GE))
else:
    print("{} does not get an A for a {}% in Geography".format(Student2, AvgGrS2GE))
#Student 3
if AvgGrS3EE > 70:
    print("{} gets an A for Science for having a {}%".format(Student3, AvgGrS3EE))
else:
    print("{} does not get an A for a {}% in Science 128".format(Student3, AvgGrS3EE))
if AvgGrS3FR > 70:
    print("{} gets an A for French for having a {}%".format(Student3, AvgGrS3FR))
else:
    print("{} does not get an A for a {}% in French".format(Student3, AvgGrS3FR))
if AvgGrS3GE > 70:
    print("{} gets an A for Geography for having a {}%".format(Student3, AvgGrS3GE))
else:
    print("{} does not get an A for a {}% in Geography".format(Student3, AvgGrS3GE))

#Highest Mark
    #Science
if AvgGrS1EE > AvgGrS2EE:
    if AvgGrS1EE > AvgGrS3EE:
        print("{} received the highest grade in Science.".format(Student1))
if AvgGrS2EE > AvgGrS3EE:
    if AvgGrS2EE > AvgGrS1EE:
        print("{} received the highest grade in Science.".format(Student2))
if AvgGrS3EE > AvgGrS1EE:
    if AvgGrS3EE > AvgGrS2EE:
        print("{} received the highest grade in Science.".format(Student3))
    #French
if AvgGrS1FR > AvgGrS2FR:
    if AvgGrS1FR > AvgGrS3FR:
        print("{} received the highest grade in French.".format(Student1))
if AvgGrS2FR > AvgGrS3FR:
    if AvgGrS2FR > AvgGrS1FR:
        print("{}received the highest grade in French.".format(Student2))
if AvgGrS3FR > AvgGrS1FR:
    if AvgGrS3FR > AvgGrS2FR:
        print("{} received the highest grade in French.".format(Student3))
    #Geography
if AvgGrS1GE > AvgGrS2GE:
    if AvgGrS1GE > AvgGrS3GE:
        print("{} received the highest grade in Geography.".format(Student1))
if AvgGrS2GE > AvgGrS3GE:
    if AvgGrS2GE > AvgGrS1GE:
        print("{}received the highest grade in Geography.".format(Student2))
if AvgGrS3GE > AvgGrS1FR:
    if AvgGrS3GE > AvgGrS2GE:
        print("{} received the highest grade in Geography.".format(Student3))
