#!/usr/bin/python3.6

print("Welcome to the calculator that will compare student grades to other students ")
print("in a basic manner. You will be asked for the names of three (3) students,")
print("then you will be asked how many assignments a student had in a specific")
print("course. After this you will be asked to input the grade. Please use whole")
print("numbers (Do not use fractions or decimals). I hope you find this calculator")
print("interesing.")
print("")

Student1=input("What is the first studnet's name? ")
Student2=input("What is the second student's name? ")
Student3=input("What is the third student's name? ")

print('')

#Student 1, Science
print('====={}====='.format(Student1))
Assign1=int(input("How many assignments did {} have in Science?".format(Student1)))
print('')
S1gradesEE=list()
count=1
while count <= Assign1:
    S1gradesEE.append(int(input('What is the grade for assignment {}? '.format(count))))
    count=count+1
print('')
print("For Science {} had the grades of {} out of {} assignments".format(Student1, S1gradesEE, Assign1))
AvgGrS1EE=sum(S1gradesEE)//len(S1gradesEE)
print("The average grade for {} in Science was {}%.".format(Student1, AvgGrS1EE))
print('')

#Student 1, French
Assign2=int(input("How many assignments did {} have in French? ".format(Student1)))
print('')
S1gradesFR=list()
count=1
while count <= Assign2:
    S1gradesFR.append(int(input('What is the grade for assignment {} in French? '.format(count))))
    count=count+1
print('')
print("For French {} had the grades of {} out of {} assignments".format(Student1, S1gradesFR, Assign2))
AvgGrS1FR=sum(S1gradesFR)//len(S1gradesFR)
print("The average grade for {} in French was {}%.".format(Student1, AvgGrS1FR))
print('')

#Student 1, Geography
Assign3=int(input("How many assignments did {} have in Geography? ".format(Student1)))
print('')
S1gradesGE=list()
count=1
while count <= Assign3:
    S1gradesGE.append(int(input('What is the grade for assignment {}? '.format(count))))
    count=count+1
print('')
print("For Geography {} had the grades of {} out of {} assignments".format(Student1, S1gradesGE, Assign3))
AvgGrS1GE=sum(S1gradesGE)//len(S1gradesGE)
print("The average grade for {} in Geography was {}%.".format(Student1, AvgGrS1GE))
print('')

#Student 2, Science
print('====={}====='.format(Student2))
AssignS2_1=int(input("How many assignments did {} have in Science? ".format(Student2)))
print('')
S2gradesEE=list()
count=1
while count <= AssignS2_1:
    S2gradesEE.append(int(input('What is the grade for assignment {}? '.format(count))))
    count=count+1
print('')
print("For Science {} had the grades of {} out of {} assignments".format(Student2, S2gradesEE, AssignS2_1))
AvgGrS2EE=sum(S2gradesEE)//len(S2gradesEE)
print("The average grade for {} in Science was {}%.".format(Student2, AvgGrS2EE))
print('')

#Student 2, French
AssignS2_2=int(input("How many assignments did {} have in French? ".format(Student2)))
print('')
S2gradesFR=list()
count=1
while count <= AssignS2_2:
    S2gradesFR.append(int(input('What is the grade for assignment {} in French? '.format(count))))
    count=count+1
print('')
print("For French {} had the grades of {} out of {} assignments".format(Student2, S2gradesFR, AssignS2_2))
AvgGrS2FR=sum(S2gradesFR)//len(S2gradesFR)
print("The average grade for {} in French was {}%.".format(Student2, AvgGrS2FR))
print('')

#Student 2, Geography
AssignS2_3=int(input("How many assignments did {} have in Geography? ".format(Student2)))
print('')
S2gradesGE=list()
count=1
while count <= AssignS2_3:
    S2gradesGE.append(int(input('What is the grade for assignment {}? '.format(count))))
    count=count+1
print('')
print("For Geography {} had the grades of {} out of {} assignments".format(Student2, S2gradesGE, AssignS2_3))
AvgGrS2GE=sum(S2gradesGE)//len(S2gradesGE)
print("The average grade for {} in Geography was {}%.".format(Student2, AvgGrS2GE))
print('')

#Student 3, Science
print('====={}====='.format(Student3))
AssignS3_1=int(input("How many assignments did {} have in Science? ".format(Student3)))
print('')
S3gradesEE=list()
count=1
while count <= AssignS3_1:
    S3gradesEE.append(int(input('What is the grade for assignment {}? '.format(count))))
    count=count+1
print('')
print("For Science {} had the grades of {} out of {} assignments".format(Student3, S3gradesEE, AssignS3_1))
AvgGrS3EE=sum(S3gradesEE)//len(S3gradesEE)
print("The average grade for {} in Science was {}%.".format(Student3, AvgGrS3EE))
print('')

#Student 3, French
AssignS3_2=int(input("How many assignments did {} have in French? ".format(Student3)))
print('')
S3gradesFR=list()
count=1
while count <= AssignS3_2:
    S3gradesFR.append(int(input('What is the grade for assignment {} in French? '.format(count))))
    count=count+1
print('')
print("For French {} had the grades of {} out of {} assignments".format(Student3, S3gradesFR, AssignS3_2))
AvgGrS3FR=sum(S3gradesFR)//len(S3gradesFR)
print("The average grade for {} in French was {}%.".format(Student3, AvgGrS3FR))
print('')

#Student 3, Geography
AssignS3_3=int(input("How many assignments did {} have in Geography? ".format(Student3)))
print('')
S3gradesGE=list()
count=1
while count <= AssignS3_3:
    S3gradesGE.append(int(input('What is the grade for assignment {}? '.format(count))))
    count=count+1
print('')
print("For Geography {} had the grades of {} out of {} assignments".format(Student3, S3gradesGE, AssignS3_3))
AvgGrS3GE=sum(S3gradesGE)//len(S3gradesGE)
print("The average grade for {} in Geography was {}%.".format(Student3, AvgGrS3GE))
print('')

#Student Grade Letters
print("=========================")
print("===== Letter Grades =====")
print("=========================")
 #Student1 - Science
if AvgGrS1EE >= 90:
    print("{} gets an A for Science for having a {}%".format(Student1, AvgGrS1EE))
elif AvgGrS1EE >= 80 and AvgGrSqEE < 90:
    print("{} gets a B for Science for having a {}%".format(Student1, AvgGrS1EE))
elif AvgGrS1EE >= 70 and AvgGrS1EE < 80:
    print("{} gets a C for Science for having a {}%".format(Student1, AvgGrS1EE))
elif AvgGrS1EE >= 60 and AvgGrS1EE < 70:
    print("{} gets a D for Science for having a {}%".format(Student1, AvgGrS1EE))
else:
    print("{} has failed Science for having a {}%".format(Student1, AvgGrS1EE))

 #Student1 - French
if AvgGrS1FR >= 90:
    print("{} gets an A in French for having a {}%".format(Student1, AvgGrS1FR))
elif AvgGrS1FR >= 80 and AvgGrS1FR < 90:
    print("{} gets a B in French for having a {}%".format(Student1, AvgGrS1FR))
elif AvgGrS1FR >= 70 and AvgGrS1FR < 80:
    print("{} gets a C in French for having a {}%".format(Student1, AvgGrS1FR))
elif AvgGrS1FR >= 60 and AvgGrS1FR < 70:
    print("{} gets a D in French for having a {}%".format(Student1, AvgGrS1FR))
else:
    print("{} has failed French for having a {}%".format(Student1, AvgGrS1FR))

 #Student1 - Geography
if AvgGrS1GE >= 90:
    print("{} gets an A in Geography for having a {}%".format(Student1, AvgGrS1GE))
elif AvgGrS1GE >= 80 and AvgGrS1GE < 90:
    print("{} gets a B in Geography for having a {}%".format(Student1, AvgGrS1GE))
elif AvgGrS1GE >= 70 and AvgGrS1GE < 80:
    print("{} gets a C in Geography for having a {}%".format(Student1, AvgGrS1GE))
elif AvgGrS1GE >= 60 and AvgGrS1GE < 70:
    print("{} gets a D in Geography for having a {}%".format(Student1, AvgGrS1GE))
else:
    print("{} has failed Geography for having a {}%".format(Student1, AvgGrS1GE))
print("")

 #Student2 - Science
if AvgGrS2EE >= 90:
    print("{} gets an A for Science for having a {}%".format(Student2, AvgGrS2EE))
elif AvgGrS2EE >= 80 and AvgGrS2EE < 90:
    print("{} gets a B for Science for having a {}%".format(Student2, AvgGrS2EE))
elif AvgGrS2EE >= 70 and AvgGrS2EE < 80:
    print("{} gets a C for Science for having a {}%".format(Student2, AvgGrS2EE))
elif AvgGrS2EE >= 60 and AvgGrS2EE < 70:
    print("{} gets a D for Science for having a {}%".format(Student2, AvgGrS2EE))
else:
    print("{} has failed Science for having a {}%".format(Student2, AvgGrS2EE))

 #Student2 - French
if AvgGrS2FR >= 90:
    print("{} gets an A in French for having a {}%".format(Student2, AvgGrS2FR))
elif AvgGrS2FR >= 80 and AvgGrS2FR < 90:
    print("{} gets a B in French for having a {}%".format(Student2, AvgGrS2FR))
elif AvgGrS2FR >= 70 and AvgGrS2FR < 80:
    print("{} gets a C in French for having a {}%".format(Student2, AvgGrS2FR))
elif AvgGrS2FR >= 60 and AvgGrS2FR < 70:
    print("{} gets a D in French for having a {}%".format(Student2, AvgGrS2FR))
else:
    print("{} has failed French for having a {}%".format(Student2, AvgGrS2FR))

 #Student2 - Geography
if AvgGrS2GE >= 90:
    print("{} gets an A in Geography for having a {}%".format(Student2, AvgGrS2GE))
elif AvgGrS2GE >= 80 and AvgGrS2GE < 90:
    print("{} gets a B in Geography for having a {}%".format(Student2, AvgGrS2GE))
elif AvgGrS2GE >= 70 and AvgGrS2GE < 80:
    print("{} gets a C in Geography for having a {}%".format(Student2, AvgGrS2GE))
elif AvgGrS2GE >= 60 and AvgGrS2GE < 70:
    print("{} gets a D in Geography for having a {}%".format(Student2, AvgGrS2GE))
else:
    print("{} has failed Geography for having a {}%".format(Student2, AvgGrS2GE))
print("")

 #Student3 - Science
if AvgGrS3EE >= 90:
    print("{} gets an A for Science for having a {}%".format(Student3, AvgGrS3EE))
elif AvgGrS3EE >= 80 and AvgGrS3EE < 90:
    print("{} gets a B for Science for having a {}%".format(Student3, AvgGrS3EE))
elif AvgGrS3EE >= 70 and AvgGrS3EE < 80:
    print("{} gets a C for Science for having a {}%".format(Student3, AvgGrS3EE))
elif AvgGrS3EE >= 60 and AvgGrS3EE < 70:
    print("{} gets a D for Science for having a {}%".format(Student3, AvgGrS3EE))
else:
    print("{} has failed Science for having a {}%".format(Student3, AvgGrS3EE))

 #Student3 - French
if AvgGrS3FR >= 90:
    print("{} gets an A in French for having a {}%".format(Student3, AvgGrS3FR))
elif AvgGrS3FR >= 80 and AvgGrS3FR < 90:
    print("{} gets a B in French for having a {}%".format(Student3, AvgGrS3FR))
elif AvgGrS3FR >= 70 and AvgGrS3FR < 80:
    print("{} gets a C in French for having a {}%".format(Student3, AvgGrS3FR))
elif AvgGrS3FR >= 60 and AvgGrS3FR < 70:
    print("{} gets a D in French for having a {}%".format(Student3, AvgGrS3FR))
else:
    print("{} has failed French for having a {}%".format(Student3, AvgGrS3FR))

 #Student3 - Geography
if AvgGrS3GE >= 90:
    print("{} gets an A in Geography for having a {}%".format(Student3, AvgGrS3GE))
elif AvgGrS3GE >= 80 and AvgGrS3GE < 90:
    print("{} gets a B in Geography for having a {}%".format(Student3, AvgGrS3GE))
elif AvgGrS3GE >= 70 and AvgGrS3GE < 80:
    print("{} gets a C in Geography for having a {}%".format(Student3, AvgGrS3GE))
elif AvgGrS3GE >= 60 and AvgGrS3GE < 70:
    print("{} gets a D in Geography for having a {}%".format(Student3, AvgGrS3GE))
else:
    print("{} has failed Geography for having a {}%".format(Student3, AvgGrS3GE))
print("")


#Highest Mark

print("=========================")
print("===== Best  Student =====")
print("=========================")

    #Science
if AvgGrS1EE > AvgGrS2EE and AvgGrS1EE > AvgGrS3EE:
    print("{} received the highest grade of {} in Science.".format(Student1, AvgGrS1EE))
elif AvgGrS2EE > AvgGrS1EE and AvgGrS2EE > AvgGrS3EE:
    print("{} received the highest grade of {} in Science.".format(Student2, AvgGrS2EE))
elif AvgGrS3EE > AvgGrS1EE and AvgGrS3EE > AvgGrS2EE:
    print("{} received the highest grade of {} in Science.".format(Student3, AvgGrS3EE))
else:
    print("There was some error, please contact the programmer.")

    #French
if AvgGrS1FR > AvgGrS2FR and AvgGrS1FR > AvgGrS3FR:
    print("{} received the highest grade of {} in French.".format(Student1, AvgGrS1Fr))
elif AvgGrS2FR > AvgGrS1FR and AvgGrS2FR > AvgGrS3FR:
    print("{} received the highest grade of {} in French.".format(Student2, AvgGrS2FR))
elif AvgGrS3FR > AvgGrS1FR and AvgGrS3FR > AvgGrS2FR:
    print("{} received the highest grade of {} in French.".format(Student3, AvgGrS3FR))
else:
    print("There was some error, please contact the programmer.")

    #Geography
if AvgGrS1GE > AvgGrS2GE and AvgGrS1GE > AvgGrS3GE:
    print("{} received the highest grade of {} in Geography.".format(Student1, AvgGrS1GE))
elif AvgGrS2GE > AvgGrS1GE and AvgGrS2GE > AvgGrS3GE:
    print("{} received the highest grade of {} in Geography.".format(Student2, AvgGrS2GE))
elif AvgGrS3GE > AvgGrS1GE and AvgGrS3GE > AvgGrS2GE:
    print("{} received the highest grade of {} in Geography.".format(Student3, AvgGrS3GE))
else:
    print("There was some error, please contact the programmer.")
print("")


