from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for ques in question_data:
    text = ques["text"]
    answer = ques["answer"]
    question = Question(text, answer)
    question_bank.append(question)
quiz_brain=QuizBrain(question_bank)

while quiz_brain.still_has_question():
    quiz_brain.next_question()

print("you've completed the quiz")
print(f"your final score is {quiz_brain.score}/{len(quiz_brain.question_list)} ")


