# class User:
    
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
    
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1

# user_1 = User("001", "Madara")
# user_2 = User("002", "Hashirama")
# # user_1.id = 1
# # user_1.username = "Uchiha Madara"
# # print(user_1.followers)
# # user_1.followers = 20
# # print(user_1.followers)

# user_1.follow(user_2)
# # user_2.follow(user_1)
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)

# from question_model import Question
class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

# from quiz_brain import QuizBrain
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} True/False?: ")
        self.check_answer(user_answer, current_question.answer)
        # print(f"{self.question_number}/{len(self.question_list)}")

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Hmm, that's wrong!")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number} \n")

# from data import question_data
question_data = \
    [
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science: Computers",
            "question": "Ada Lovelace is often considered the first computer programmer.",
            "correct_answer": "True",
            "incorrect_answers": ["False"]
        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science: Computers",
            "question": "&quot;HTML&quot; stands for Hypertext Markup Language.",
            "correct_answer": "True",
            "incorrect_answers": ["False"]
        },
        {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
         "question": "The NVidia GTX 1080 gets its name because it can only render at a 1920x1080 screen resolution.",
         "correct_answer": "False", "incorrect_answers": ["True"]},
        {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
         "question": "The programming language &quot;Python&quot; is based off a modified version of &quot;JavaScript&quot;.",
         "correct_answer": "False", "incorrect_answers": ["True"]},
        {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
         "question": "RAM stands for Random Access Memory.", "correct_answer": "True",
         "incorrect_answers": ["False"]},
        {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
         "question": "The Windows 7 operating system has six main editions.",
         "correct_answer": "True", "incorrect_answers": ["False"]},
        {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
         "question": "The Windows ME operating system was released in the year 2000.",
         "correct_answer": "True", "incorrect_answers": ["False"]},
        {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
         "question": "Linus Torvalds created Linux and Git.", "correct_answer": "True",
         "incorrect_answers": ["False"]},
        {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
         "question": "The logo for Snapchat is a Bell.", "correct_answer": "False",
         "incorrect_answers": ["True"]},
        {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
         "question": "In most programming languages, the operator ++ is equivalent to the statement &quot;+= 1&quot;.",
         "correct_answer": "True", "incorrect_answers": ["False"]}
    ]

    # {"text": "A slug's blood is green.", "answer": "True"},
    # {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    # {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    # {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    # {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    # {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    # {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    # {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    # {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    # {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    # {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    # {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    # questions = Question(ques["text"], ques["answer"])
    # question_bank.append(questions)
    # print(questions.text)
    # print(questions.answer)

# print(question_bank)
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print(f"You've completed the quiz. \nYour final score is:{quiz.score}/{len(quiz.question_list)}")