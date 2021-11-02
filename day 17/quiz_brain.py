class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False) ")
        self.check_answer(user_answer)

    def still_has_question(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer):
        question = self.questions_list[self.question_number - 1]
        if user_answer.lower() == question.answer.lower():
            self.score += 1
            print("You got ir right!")
            print(f"Your current score is: {self.score}/{self.question_number}")
        else:
            print("That's wrong.")
            print(f"The correct answer was {question.answer}")
