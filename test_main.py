import unittest
from main import get_grade_feedback

class TestGetGradeFeedback(unittest.TestCase):

    def test_grade_u(self):
        student_name = "TestName"
        subject_name = "TestSubject"
        expected_feedback = f"A 'U' in {subject_name}? Oh, how... *predictable*. Don't worry, {student_name}, the slime pits always need more... *volunteers*."
        self.assertEqual(get_grade_feedback(student_name, subject_name, "U"), expected_feedback)

    def test_grade_2(self):
        student_name = "TestName"
        subject_name = "TestSubject"
        expected_feedback = f"A '2' for {subject_name}. How... mediocre. {student_name}, you're perfectly balanced, as all failures should be. Not quite rock bottom, but aspiring!"
        self.assertEqual(get_grade_feedback(student_name, subject_name, "2"), expected_feedback)

    def test_grade_4(self):
        student_name = "TestName"
        subject_name = "TestSubject"
        expected_feedback = f"A '4' in {subject_name}? You actually passed, {student_name}? Hmph. Don't get any ideas above your station. The system must be flawed."
        self.assertEqual(get_grade_feedback(student_name, subject_name, "4"), expected_feedback)

    def test_grade_6(self):
        student_name = "TestName"
        subject_name = "TestSubject" # Generic subject
        expected_feedback = f"A '6' in {subject_name}, {student_name}? Slightly less pathetic than I expected."
        self.assertEqual(get_grade_feedback(student_name, subject_name, "6"), expected_feedback)

    def test_grade_8(self):
        student_name = "TestName"
        subject_name = "TestSubject" # Generic subject
        expected_feedback = f"An '8' in {subject_name}! {student_name}, you're dangerously close to being interesting. Tone it down."
        self.assertEqual(get_grade_feedback(student_name, subject_name, "8"), expected_feedback)

    def test_grade_9(self):
        student_name = "TestName"
        subject_name = "TestSubject" # Generic subject
        expected_feedback = f"A '9' in {subject_name}, {student_name}! Show off. You'll be the first one I pick for the... 'advanced challenges'."
        self.assertEqual(get_grade_feedback(student_name, subject_name, "9"), expected_feedback)

    def test_grade_n(self):
        student_name = "TestName"
        subject_name = "TestSubject"
        expected_feedback = f"Not taken {subject_name}, {student_name}? Trying to hide your incompetence? Or just lazy? Either way, it's noted."
        self.assertEqual(get_grade_feedback(student_name, subject_name, "N"), expected_feedback)

    def test_grade_not_taken(self):
        student_name = "TestName"
        subject_name = "TestSubject"
        expected_feedback = f"Not taken {subject_name}, {student_name}? Trying to hide your incompetence? Or just lazy? Either way, it's noted."
        self.assertEqual(get_grade_feedback(student_name, subject_name, "Not Taken"), expected_feedback)

    def test_grade_unrecognized(self):
        student_name = "TestName"
        subject_name = "TestSubject"
        expected_feedback = f"Eh? What's this gibberish for {subject_name}, {student_name}? Did you type that with your face? Try a real grade, or don't try at all."
        self.assertEqual(get_grade_feedback(student_name, subject_name, "XYZ"), expected_feedback)

if __name__ == '__main__':
    unittest.main()
