class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = [q_list]

    def next_question(question_number, q_list):
        
        user_answer = input(" Q.{question_number} {question.text}, Type True or False: ")

