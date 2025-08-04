print("🧪 Welcome to the Python Quiz Game!")

def ask_question(number, question_data):
    print("\nQuestion", number, ":", question_data["question"])
    print("a)", question_data["options"]["a"])
    print("b)", question_data["options"]["b"])
    print("c)", question_data["options"]["c"])
    print("d)", question_data["options"]["d"])
    answer = input("Your answer (a/b/c/d): ").lower()
    if answer == question_data["answer"]:
        print("✅ Correct!")
        return 1
    else:
        print("❌ Wrong! The correct answer is", question_data["answer"])
        return 0

def run_quiz(questions):
    score = 0
    question_number = 1
    for q in questions:
        score += ask_question(question_number, q)
        question_number += 1
    print("\n🎯 Your Final Score:", score, "/", len(questions))
    if score >= 15:
        print("🎉 Excellent! You're interview-ready!")
    elif score >= 10:
        print("👍 Good job! Keep practicing!")
    else:
        print("📘 Study more and try again!")

# 20 Simple Python Interview Questions
quiz = [
    {"question": "What is the output of: print(type([]))?",
     "options": {"a": "<class 'list'>", "b": "<class 'dict'>", "c": "<class 'set'>", "d": "<class 'tuple'>"},
     "answer": "a"},
    {"question": "Which keyword is used to define a function in Python?",
     "options": {"a": "function", "b": "def", "c": "fun", "d": "define"},
     "answer": "b"},
    {"question": "What is the output of 3 * '5'?",
     "options": {"a": "15", "b": "555", "c": "Error", "d": "None"},
     "answer": "b"},
    {"question": "Which of the following is immutable?",
     "options": {"a": "list", "b": "dict", "c": "set", "d": "tuple"},
     "answer": "d"},
    {"question": "How do you start a comment in Python?",
     "options": {"a": "//", "b": "<!--", "c": "#", "d": "**"},
     "answer": "c"},
    {"question": "What does len() do in Python?",
     "options": {"a": "Calculates size of int", "b": "Returns list length", "c": "Finds memory usage", "d": "Loops through list"},
     "answer": "b"},
    {"question": "What is the correct file extension for Python files?",
     "options": {"a": ".pt", "b": ".python", "c": ".py", "d": ".pyt"},
     "answer": "c"},
    {"question": "Which of the following is used to import a module?",
     "options": {"a": "include", "b": "import", "c": "using", "d": "require"},
     "answer": "b"},
    {"question": "What is the output of bool(0)?",
     "options": {"a": "True", "b": "False", "c": "0", "d": "None"},
     "answer": "b"},
    {"question": "What is used to define a block of code in Python?",
     "options": {"a": "Brackets {}", "b": "Parentheses ()", "c": "Indentation", "d": "Curly braces"},
     "answer": "c"},
    {"question": "Which of these is a Python data type?",
     "options": {"a": "element", "b": "number", "c": "string", "d": "character"},
     "answer": "c"},
    {"question": "What will 'hello'.upper() return?",
     "options": {"a": "Hello", "b": "HELLO", "c": "hello", "d": "H E L L O"},
     "answer": "b"},
    {"question": "Which operator is used for exponentiation?",
     "options": {"a": "^", "b": "**", "c": "^^", "d": "//"},
     "answer": "b"},
    {"question": "Which one is a correct variable name?",
     "options": {"a": "2value", "b": "value2", "c": "value-2", "d": "value.2"},
     "answer": "b"},
    {"question": "What does the 'in' keyword do?",
     "options": {"a": "Defines loops", "b": "Checks membership", "c": "Declares function", "d": "Imports module"},
     "answer": "b"},
    {"question": "What is the result of 10 // 3?",
     "options": {"a": "3.33", "b": "3", "c": "4", "d": "0"},
     "answer": "b"},
    {"question": "Which method is used to add an item to a list?",
     "options": {"a": "insert()", "b": "add()", "c": "append()", "d": "extend()"},
     "answer": "c"},
    {"question": "Which one is a loop in Python?",
     "options": {"a": "for", "b": "loop", "c": "iterate", "d": "repeat"},
     "answer": "a"},
    {"question": "What does the range(5) produce?",
     "options": {"a": "[0, 1, 2, 3, 4]", "b": "[1, 2, 3, 4, 5]", "c": "[0, 5]", "d": "[5, 4, 3, 2, 1]"},
     "answer": "a"},
    {"question": "Which function is used to get user input?",
     "options": {"a": "print()", "b": "scan()", "c": "input()", "d": "read()"},
     "answer": "c"}
]

# Start the quiz
run_quiz(quiz)
