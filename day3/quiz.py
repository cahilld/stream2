def show_menu():

    print("1. Ask questions")
    print("2. Add a question")
    print("3. Exit Game")
    
    option = input("Enter option: ")
    return option

def ask_questions():
    questions = []
    answers = []
    
    file = open("questions.txt", "r")
    lines = file.read().splitlines() 
    lines = enumerate(lines)

    for i, text in lines:
        if i%2 == 0:
            questions.append(text)
        else:
            answers.append(text)
    file.close()          
    number_of_questions = len(questions)
    questions_and_answers = zip(questions, answers)
    score = 0    
    for question, answer in questions_and_answers:
        guess = input(question + "> ")
        if guess == answer:
            score += 1
            print("right")
        else:
            print("wrong")
    print ("You got {0} correct out of {1}".format(score, number_of_questions))
    
def add_question():
    print("")
    question = input("Enter a question\n> ")
    print("")
    print("OK then, tell me the answer")
    answer = input(question + "\n> ")
    file = open("questions.txt", "a")
    file.write(question + "\n")
    file.write(answer + "\n")
    file.close()

def game_loop():
    while True:
        option = show_menu()
        if option == "1":
           ask_questions()
        elif option == "2":
            add_question()
        elif option == "3":
            break
        else:
            print("Invalid Option")
        print("")

game_loop()