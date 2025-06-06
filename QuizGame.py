# A simple quiz game in Python using basic control structures and data types.
questions = ("How many continents are there?",
             "What is the capital of France?",
             "Who is the CEO of Tesla?",
             "Is the Earth flat?",
             "How many days are in a year?")

options = (("A. 7", "B. 5", "C. 8", "D. 6",), 
           ("A. Florence", "B. New Delhi", "C. Washington D.C.", "D. Paris",),
           ("A. Satya Nadela", "B. Pranav Vaddepalli", "C. Elon Musk", "D. Mark Zuckerberg",), 
           ("A. Yes", "B. No", "C. Maybe", "D. Who really knows?",),
           ("A. 364", "B. 365", "C. 360", "D. 375",))

answers = ("A", "D", "C", "B", "B")
guesses = []
score = 0
questionNum = 0

for question in questions:
    print("----------------------------")
    print(question)
    for option in options[questionNum]:
        print(option)
    guess = input("Enter A, B, C, or D: ").upper()
    guesses.append(guess)
    if guess == answers[questionNum]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")
        print(f"The correct answer was {answers[questionNum]}.")
    questionNum += 1

print()
print("-----------RESULTS-----------")
print()
print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()
print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()
print(f"Your score is {score} out of {len(questions)}.")
print("Thanks for playing!")
