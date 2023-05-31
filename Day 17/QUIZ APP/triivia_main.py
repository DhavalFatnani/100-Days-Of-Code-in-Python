from question_model import Question
from trivia_quiz_data import question_data
from trivia_quiz_brain import TQuizBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

Quiz = TQuizBrain(question_bank)

while Quiz.still_has_questions():
    Quiz.next_question()

print("TADA! You've Completed the Quiz.")
print(f"Your Final Score is: {Quiz.score}/{Quiz.question_number}")
