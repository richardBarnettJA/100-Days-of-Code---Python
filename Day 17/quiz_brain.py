class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, user, answer):
        if user.lower() == answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
            print(f"The correct answer was: {answer}.")
        print(f"The current score is: {self.score}/{self.question_number}\n")


    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        response = (input(f"Q.{self.question_number}: {question.question} (True/False)?: ")).lower()
        self.check_answer(response, question.answer)
