import datetime  

print("Welcome Students, we are here for the students to type their grade!(GCSE) ")
print("Also this is a demo!")
print("My name is Education, and I am here to see your GCSE results: ")

name = input("What is your name? ")
surname = input("What is your surname? ")

date_of_birth = input("So your name is " + name + " " + surname + " and what is your date of birth? (in DD/MM/YYYY): ")

#This is how a import works, for a date of birth
birthdate=datetime.datetime.strptime(date_of_birth,"%d/%m/%Y").date() 

print("So your birthdate is " + birthdate.strftime('%d/%B/%Y'))

High_School = input("What college do you go to? ")
print("So you go to " + High_School)
print("Thank you for giving information " + name)
print("**********************************************************************************************************")
print("Now is time for grades, hehe?")

grademaths = input("What is your grade for maths, please tell me: ")

if grademaths == "N" or grademaths == "Not Taken":
    print("Why didn't you take maths, well you can resit, but please pass this exam please!")
elif grademaths == "U":
    print("Why did you fucking get a grade U on Maths, you dumbass not knowing basic east maths, like 1+1, you big failure, your future is trash and you even didn't even try")
elif grademaths == "E":
    print("What is this grade, you tried very little in your GCSE, you failed the test you failure. ")
elif grademaths == "D":
    print("You got a devoloping grade, that so hilourious, you failed and that your future is the worst!")
elif grademaths == "1":
    print("What is this grade you got, a 1 why didn't you try, you could passed if you did get a 4 you failure, please try")
elif grademaths == "2":
    print("You got a 2, you failed, but atleast your best, next time do better in the resit and pass please you failure!")
elif grademaths == "3":
    print("You nearly there with a 4, but can please try a little more to PASS please in resit to get a 4 or higher!")
elif grademaths == "4":
    print("You did well this one, well done you passed!")
elif grademaths == "5":
    print("You are trying atleast, i am happy that you got a 5, which is better!")
elif grademaths == "6":
    print("I am happy for you, you got a 6 in Maths which is enough for Maths A level!")
elif grademaths == "7":
    print("You got a 7, i am proud of you " + name + " and well done, you can get better education in university and college.")
elif grademaths == "8":
    print("Yes, you got the grade I wanted to see, I congrate you, you are better than the other failures, that is why I like you more than the other failures that fail, emglish and maths.")
elif grademaths == "9":
    print("You got the highest grade, now I want to take you to univeristy instantly, with the best students of the world, I say in Maths which is the best! and no freedom for you to choose something else hahhahahahahhahahah!")
else:
    print("This is demo, so no full list of grades and courses or did you type anything wrong?")
    exit()

gradeenglishlanguage = input("What is your grade for english, please tell me: ")

if gradeenglishlanguage == "N" or gradeenglishlanguage == "Not Taken":
    print("Why didn't you take english, well you can resit, but please pass this exam please!")
elif gradeenglishlanguage == "U":
    print("Why did you fucking get a grade U on English n/, you dumbass not knowing how to read and write small words, like 1+1, you big failure, your future is trash and you even didn't even try")
elif gradeenglishlanguage == "E":
    print("What is this grade, you tried very little in your GCSE, you failed the test you failure. ")
elif gradeenglishlanguage == "D":
    print("You got a devoloping grade, that so hilourious, you failed and that your future is the worst!")
elif gradeenglishlanguage == "1":
    print("What is this grade you got, a 1 why didn't you try, you could passed if you did get a 4 you failure, please try")
elif gradeenglishlanguage == "2":
    print("You got a 2, you failed, but atleast your best, next time do better in the resit and pass please you failure!")
elif gradeenglishlanguage == "3":
    print("You nearly there with a 4, but can please try a little more to PASS please in resit to get a 4 or higher!")
elif gradeenglishlanguage == "4":
    print("You did well this one, well done you passed!")
elif gradeenglishlanguage == "5":
    print("You are trying atleast, i am happy that you got a 5, which is better!")
elif gradeenglishlanguage == "6":
    print("Yes, you passed english, but also you got a fine grade and i am very happy!")
elif gradeenglishlanguage == "7":
    print("Yes, higher and higher Mr " + name + " and that is a good grade for english for creative writing and other bigger opportunities.")
elif gradeenglishlanguage == "8":
    print("Yes, you got the grade I wanted to see, I congrate you, you are better than the other failures, that is why I like you more than the other failures that fail, emglish and maths.")
elif gradeenglishlanguage == "9":
    print("You got the highest grade, now I want to take you to univeristy instantly, with the best students of the world, I say in english and no freedom for you to choose something else hahhahahahahhahahah!")
else:
    print("This is demo, so no full list of grades and courses or did you type anything wrong?")
    exit()
    
gradeenglishliterature = input("What is your grade for english, please tell me: ")

if gradeenglishliterature == "N" or gradeenglishlanguage == "Not Taken":
    print("Why didn't you take english, well you can resit, but please pass this exam please! Unless you are doing a diffrent course that doesn't require!")
elif gradeenglishliterature == "U":
    print("Why did you fucking get a grade U on English n/, you dumbass not knowing how to read and write small words, like 1+1, you big failure, your future is trash and you even didn't even try")
elif gradeenglishliterature == "E":
    print("What is this grade, you tried very little in your GCSE, you failed the test you failure. ")
elif gradeenglishliterature == "D":
    print("You got a devoloping grade, that so hilourious, you failed and that your future is the worst!")
elif gradeenglishliterature == "1":
    print("What is this grade you got, a 1 why didn't you try, you could passed if you did get a 4 you failure, please try")
elif gradeenglishliterature == "2":
    print("You got a 2, you failed, but atleast your best, next time do better in the resit and pass please you failure!")
elif gradeenglishliterature == "3":
    print("You nearly there with a 4, but can please try a little more to PASS please in resit to get a 4 or higher!")
elif gradeenglishliterature == "4":
    print("You did well this one, well done you passed!")
elif gradeenglishliterature == "5":
    print("You are trying atleast, i am happy that you got a 5, which is better!")
elif gradeenglishliterature == "6":
    print("Yes, you passed english, but also you got a fine grade and i am very happy!")
elif gradeenglishliterature == "7":
    print("Yes, higher and higher Mr " + name + " and that is a good grade for english for creative writing and other bigger opportunities.")
elif gradeenglishliterature == "8":
    print("You did it, you did it you got a grade 8, which is great when you are reading MacBeth and poems in University.")
elif gradeenglishliterature == "9":
    print("Well done " + name + " " + surname + ", you did it, you can use this for your university to choose one of the best courses for writing your story, like Shakespeare ooooo! yes.")
else:
    print("This is demo, so no full list of grades and courses or did you type anything wrong?")
    exit()
print("*************************************************************************")
print("The grades you got: ")
print("Maths GCSE: " + grademaths)
print("English Language GCSE: " + gradeenglishlanguage)
print("English Literature GCSE: " + gradeenglishliterature)
print("***********************************************************************************")
allcourses = (grademaths and gradeenglishlanguage and gradeenglishliterature)

if allcourses == "N" or allcourses == "Not Taken":
    print("You need to resit only maths and english language, and pass for to attend university in the future or good jobs")
if grademaths and gradeenglishlanguage == "U":
    print("The death penalty is here for you to die, because this is the lowest grade of gcse!!, and a abysmal adomanation.")
if grademaths and gradeenglishlanguage == "5":
    print("Well done you got both GCSE at grade 5, which means I will tell you a secret is that this is a demo of GCSE RESULTS for fun")
if grademaths and gradeenglishlanguage == "7":
    print("You, can now go to University, but keep improving for a grade 9 at A level please or you will become a failure!")
if grademaths and gradeenglishlanguage == "9":
    print("You got a grade 9 on both courses which means you can do one of them in University without a problem and a hasstle, of choosing any course. ")
if allcourses == "9":
    print("Yes, finally the best student in history, i will make him my slave, because he has the best grades and he taked in all courses, he is the perfect person, the iq of infinity!")
    fight = input("Do you want to punch or knife hiddenly? choose one option? ")
    if fight == "punch":
        print("You punched education, you pay the price for it, and education survived and forced you to be a slave to education for the rest of life, abusing me to be perfect!")
    elif fight == "knife":
        print("You knifed education, you killed the guy, and now you escaped, to find another country! .")
        escape1 = input("You trying to escape the place, as fast and trying to find a escape, and you suddenly find 2 places, Spain or Dubai, which one you choose: ")
        if escape1 == "Spain" or escape1 == "spain":
            print("hell")