import sys

import ui
from question_model import Question
from data import difficulty
from quiz_brain import QuizBrain
from ui import UserInterface

diff = difficulty()
question_bank = []
questions = diff.question_data()

try :
    for question in questions:

        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)


    quiz = QuizBrain(question_bank)
    ui = UserInterface(quiz)

except TypeError:
      sys.exit()

#while quiz.still_has_questions():
    #quiz.next_question()


