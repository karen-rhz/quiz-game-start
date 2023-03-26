class QuizzBrain:

    # Navigate through the list of questions
    def __init__(self, q_list):
        # Always start with the first question
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # To check if the list of question is over or not
    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        # Get the question from the previous init method
        # Default value of question number is 0
        current_question = self.question_list[self.question_number]
        # Change the question number after the program has retrieved the current question is pulled.
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} : {current_question.text} (True/False)?")
        # Calling the check_answer method to adjust the user's answer
        # Compare the user_answer against the answer in the question list
        self.check_answer(user_answer, current_question.answer)

    # To compare the input against the answer in the question list
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Great job!")
        else:
            print("Sorry, that's not right.")
        # Display the correct answer and user score out of how many question the user has gone through
        print(f"The correct answer is {correct_answer}.")
        print(f"Your score is now {self.score}/{self.question_number}")
        print("\n")