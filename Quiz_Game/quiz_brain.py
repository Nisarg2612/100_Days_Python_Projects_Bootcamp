class QuizBrain:
    def __init__(self, qus_list):
        self.question_number = 0
        self.score = 0
        self.question_list = qus_list

    # TODO 3. Checking if we are the end of the quiz
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        elif self.question_number == len(self.question_list):
            print("You've completed the quiz")
            return False
        else:
            return False

    # TODO 1. Asking the questions
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        return self.check_answer(user_answer, current_question.answer)

    # TODO 2. Checking if the answer was correct
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
            print(f"Your current score is: {self.score}/{self.question_number}, \n")
            return True
        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_answer}.")
            return False
        print(f"Your current score is: {self.score}/{self.question_number}, \n")

