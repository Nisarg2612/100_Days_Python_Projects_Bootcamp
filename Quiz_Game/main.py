from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

# Created quiz object from QuizBrian class
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    if quiz.next_question() is True:
        continue
    else:
        print(f"Your final score was: {quiz.score}/{quiz.question_number}")
        exit()
print(f"Your final score was: {quiz.score}/{quiz.question_number}")