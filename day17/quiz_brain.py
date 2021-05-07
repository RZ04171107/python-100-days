class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input("Q." + str(self.question_number) + ": " + question.text + " (True/False)?: ")
        self.check_answer(user_ans, question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_ans, correct_answer):
        if user_ans.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Oops, that's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")

    def print_report(self):
        print("You've completed the quiz.")
        print(f"Your final score was: {self.score}/{self.question_number}")
