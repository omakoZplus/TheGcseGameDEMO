import datetime  

def get_grade_feedback(student_name, subject_name, grade):
    if grade == "N" or grade == "Not Taken":
        return f"Not taken {subject_name}, {student_name}? Trying to hide your incompetence? Or just lazy? Either way, it's noted."
    elif grade == "U":
        return f"A 'U' in {subject_name}? Oh, how... *predictable*. Don't worry, {student_name}, the slime pits always need more... *volunteers*."
    elif grade == "E":
        return f"An 'E' in {subject_name}, {student_name}? Exquisitely awful. Did you even open a book? Or was 'E' for 'Effortless failure'?"
    elif grade == "D":
        return f"A 'D,' {student_name}? Delectably dreadful! You're really scraping the bottom of the barrel for {subject_name}, aren't you?"
    elif grade == "1":
        return f"A '1' in {subject_name}, {student_name}. One whole point! Did you get that for spelling your name right, or was that a lucky guess?"
    elif grade == "2":
        return f"A '2' for {subject_name}. How... mediocre. {student_name}, you're perfectly balanced, as all failures should be. Not quite rock bottom, but aspiring!"
    elif grade == "3":
        return f"A '3' in {subject_name}, {student_name}. So you *almost* tried. What a pity. That little flicker of effort, wasted."
    elif grade == "4":
        return f"A '4' in {subject_name}? You actually passed, {student_name}? Hmph. Don't get any ideas above your station. The system must be flawed."
    elif grade == "5":
        return f"A '5' in {subject_name}, {student_name}? Adequate, I suppose. For a human. Barely."
    elif grade == "6":
        if subject_name == "Maths":
            return f"A '6' in Maths, {student_name}? Not entirely repulsive. You might just survive the next culling... if you're lucky. And if your calculator didn't do all the work."
        elif subject_name == "English Language" or subject_name == "English Literature":
            return f"A '6' in {subject_name}, {student_name}? So you can string a few words together or understand basic plots. Don't strain yourself."
        else:
            return f"A '6' in {subject_name}, {student_name}? Slightly less pathetic than I expected."
    elif grade == "7":
        if subject_name == "Maths":
            return f"A '7' in Maths? You're making the other morsels look bad, {student_name}. Are you sure you didn't cheat?"
        elif subject_name == "English Language" or subject_name == "English Literature":
            return f"A '7' in {subject_name}, {student_name}? Such... competence. It's almost unsettling. Stop it."
        else:
            return f"A '7' in {subject_name}, {student_name}? Well, aren't you a little overachiever. Annoying."
    elif grade == "8":
        if subject_name == "Maths" or subject_name == "English Language":
            return f"An '8' in {subject_name}! Impressive... for a snack. Are you trying to become my new favorite, {student_name}? Don't bother, I eat my favorites last."
        elif subject_name == "English Literature":
            return f"An '8' in English Literature, {student_name}! You actually understood those dusty old books? I'm mildly surprised. Or perhaps you just memorized the cliff notes."
        else:
            return f"An '8' in {subject_name}! {student_name}, you're dangerously close to being interesting. Tone it down."
    elif grade == "9":
        if subject_name == "Maths":
            return f"A '9' in Maths, {student_name}? Hah! So you've got a bit of brain in that skull after all! Don't expect a gold star, though. Maybe just a slightly delayed doom. Or a more complex equation for your eulogy."
        elif subject_name == "English Language":
            return f"A '9' in English Language, {student_name}? Fine, you're eloquent. Now be quiet. Your linguistic prowess is giving me a headache."
        elif subject_name == "English Literature":
            return f"A '9' in English Literature, {student_name}! So you can analyze Shakespeare, big deal. Can you analyze your impending doom? That's the real test."
        else:
            return f"A '9' in {subject_name}, {student_name}! Show off. You'll be the first one I pick for the... 'advanced challenges'."
    else:
        return f"Eh? What's this gibberish for {subject_name}, {student_name}? Did you type that with your face? Try a real grade, or don't try at all."

def get_student_details():
    name = input("Alright, spit it out. Your designated noise? (First Name): ")
    surname = input(f"And the other noise they call you, {name}? (Surname): ")

    while True:
        date_of_birth_str = input(f"Date of... *creation*, I suppose, {name} {surname}? (DD/MM/YYYY, if you can manage that): ")
        try:
            birthdate = datetime.datetime.strptime(date_of_birth_str, "%d/%m/%Y").date()
            break  # Exit loop if date is valid
        except ValueError:
            print("Ugh, even a simple date is too complex for you? TRY AGAIN: DD/MM/YYYY!")

    High_School = input(f"And what dreary institution claims to be shaping your tiny mind, {name}? (College Name): ")
    print(f"So, you're {name} {surname}, spawned on {birthdate.strftime('%d %B %Y')}. Fascinating. And you fester at {High_School}. Thrilling.")
    return name, surname, birthdate, High_School

def input_subject_grades(student_name):
    print("**********************************************************************************************************")
    print(f"Alright, {student_name}, let's get to the dreary part: your so-called 'grades'. Try not to bore me. Heh heh.")
    
    grades = {}
    subjects = ["Maths", "English Language", "English Literature"]
    
    for subject in subjects:
        grade_input = input(f"What's the damage for {subject.title()}, {student_name}? ")
        feedback = get_grade_feedback(student_name, subject, grade_input)
        print(feedback)
        if feedback.startswith("Eh? What's this gibberish"): # Check for unrecognized grade message
            pass
        grades[subject] = grade_input
        
    return grades

print("💀 Welcome, unfortunate souls, to the Grade Grinder! 💀")
print("This is a demo, or so they tell me. Feel free to make it... worse. I dare you.")
print("I am Ed, your delightful tormentor for this... exercise. Heh heh heh.")

# Get student details
name, surname, birthdate, high_school = get_student_details()

# Input subject grades
grades = input_subject_grades(name)

# Display grade summary
print("*************************************************************************")
print(f"Behold, {name}, the grand testament to your... efforts:") 
print("Maths GCSE: " + grades.get("Maths", " wisely left blank?"))
print("English Language GCSE: " + grades.get("English Language", " too scared to enter?"))
print("English Literature GCSE: " + grades.get("English Literature", " ...or just illiterate?"))
print("***********************************************************************************")
# print(f"There you have it, {name}. Your 'results'. Now scurry along. I have important... brooding to do. And don't trip on your way out.")

# --- Start of Reimplemented Monster's Game Ending Sequence ---
print("\n***********************************************************************************")
print("Now, for the grand finale, based on this... *display*...")

math_grade = grades.get("Maths")
eng_lang_grade = grades.get("English Language")
eng_lit_grade = grades.get("English Literature")

low_tier_grades = ["U", "E", "D", "1", "2", "3"]
passing_grades = ["4", "5", "6", "7", "8", "9"] # N/Not Taken is handled separately

# Scenario 1: All Nines
if math_grade == "9" and eng_lang_grade == "9" and eng_lit_grade == "9":
    print(f"Hmph, {name}. All nines? You're not as dim-witted as the others, are you? Perhaps you're worthy of... *middle management* in my little corner of the abyss. Don't get excited, it's still terrible.")
    choice = input(f"Do you accept your slightly less agonizing fate, {name}? (yes/no): ").lower()
    if choice == "yes":
        print("Wise choice. Now get to work! The paperwork for lost souls is piling up.")
    elif choice == "no":
        print("Ungrateful whelp! Fine, back to the slime pits with the rest of them!")
    else:
        print("Indecisive, are we? To the pits it is!")

# Scenario 2: All Us (or all "U", "E", "D", "1", "2", "3")
elif math_grade in low_tier_grades and \
     eng_lang_grade in low_tier_grades and \
     eng_lit_grade in low_tier_grades:
    print(f"Oh, {name}, this is just... *chef's kiss*... magnificently awful! All these failing grades! You'll make a fine example for the others.")
    choice = input(f"Are you ready to embrace your destiny as my new favorite paperweight, {name}? (yes/embrace it): ").lower()
    if choice == "yes" or choice == "embrace it":
        print("Excellent! Your dedication to failure is truly inspiring. I'll find a nice, dusty shelf for you.")
    else:
        print("No enthusiasm? Don't worry, you'll fit right in with the other inanimate objects.")

# Scenario 4: At least one "N" or "Not Taken" for a core subject. (Checked before Scenario 3 to give it precedence)
elif math_grade in ["N", "Not Taken"] or \
     eng_lang_grade in ["N", "Not Taken"] or \
     eng_lit_grade in ["N", "Not Taken"]:
    print(f"Skipped a subject, did we, {name}? Trying to be clever and avoid my judgment? It doesn't work like that.")
    print("Your cowardice has been noted. Now begone.")

# Scenario 3: Passed all core subjects (all are "4" or higher) - and not all 9s (handled by Scenario 1)
elif math_grade in passing_grades and \
     eng_lang_grade in passing_grades and \
     eng_lit_grade in passing_grades:
    print(f"So, {name}, you managed to pass everything. Adequate, I suppose. Don't expect a parade.")
    print("Now, vanish from my sight before I change my mind about your 'passing' status.")

# Default/Catch-all
else:
    print(f"Well, {name}, your grades are... a collection of symbols. Mostly disappointing, as expected.")
    print("Off you go. Don't let the door hit you on the way to your mundane future.")

print(f"Game over, {name}. Or is it just beginning? Heh heh heh.")
# --- End of Reimplemented Monster's Game Ending Sequence ---
