from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []
for question in question_data:
    # Loop in dictionary to populate the question bank
    question_text_from_question_data = question["question"]
    answer_from_question_data = question["correct_answer"]
    new_question = Question(question_text_from_question_data, answer_from_question_data)
    question_bank.append(new_question)

# QuizzBrain class needs a list to function
quiz = QuizzBrain(question_bank)

# Telling the computer to loop in the list and getting the user input
# It will stop when there will be no more answers
while quiz.still_has_question():
    quiz.next_question()

print("Congrats You've completed the quizz!")
print(f"Your final score is {quiz.score}/{len(question_bank)}")