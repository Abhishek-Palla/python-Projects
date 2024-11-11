import main


class QuizBrain:
    def __init__(self,question_bank):

        self.question_number =0
        self.question_list = question_bank
        self.score =0
#TODO : asking the question
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer =input(f'Q {self.question_number} :{current_question.text} (True/False)')
        self.check_answer(answer,current_question.answer)

#TODO: checking if we are end of the quizz

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

#TODO: checking if the answer was correct
    def check_answer(self,user_answer,answer):
        if user_answer.lower() == answer.lower():
            self.score+=1
            print("You got it right!!")
            print(f"Your current score is {self.score}")
        else:
            print("It is wrong")
            print(f"The correct answer is :{answer}. ")
            print(f"Your current score is {self.score}")






