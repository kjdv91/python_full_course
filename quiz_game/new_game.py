def new_game():
    guesses = []
    correct_guesess = 0
    question_num = 1


    for key in questions:
        print("---------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A,B,C,D): ")
        guess =  guess.upper()

        guesses.append(guess)
        correct_guesess += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesess, guesses)

def check_answer(answer, guess):
    if answer ==  guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0

def display_score(correct_guesses, guesses):
    print("---------------------------------------------")
    print("RESULT")
    print("---------------------------------------------")
    print("Answer:", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses:", end=" ")
    for i in guesses:
        print(i, end=" ")

    score =   int((correct_guesses//len(questions))*100)
    print("Your score is: "+ str(score) + "%")

def play_again():
    response = input("o you want to play again? (YES OR NO):")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

questions = {
    "Who created python": "A",
    "What year was python created": "B",
    "Python is tribute to witch comedy group": "C",
    "Is the Earth round?" : "A"
}

options = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckemberg"],
    ["A 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "Smosh", "Monty Python", "SNL"],
    ["A. True", "B. False", "C. sometimes", "D. What's earth?"]
]

new_game()
while play_again():
    new_game()

print("Byeeeeee!")