from quizProject.question_model import Question
from quizProject.questiondata import question_data
from quizProject.quiz_brain import QuizBrain

question_bank = [Question(question['text'], question['answer']) for question in question_data]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print("you have completed the quiz")
print(f"your final score was: {quiz.score}/{quiz.question_number}")