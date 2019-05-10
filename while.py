question = "Are you Polish?"
possible_answers = ["Yes", "No"]

answer = None
while answer not in possible_answers:
    print(question)
    for possible_answer in possible_answers:
        print(possible_answer)

    answer = input(">>> ")
