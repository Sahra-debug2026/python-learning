name = input(" what is your name? ")
number = int(input("how many numbers do you have?"))

grades=[]
for i in range(number) :
 grade=int(input("what is your grade? "))
 if grade >= 90:
    print(f"{grade}= EXCELLENT")
 elif 70 <= grade < 90:
    print(f"{grade}= GOOD")
 else:
    print(f"{grade}= need more practice")
 grades.append(grade)
print(grades)
