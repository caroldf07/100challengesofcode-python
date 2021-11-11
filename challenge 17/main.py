from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    q = Question(text=question['text'], answer=question['answer'])
    question_bank.append(q)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
