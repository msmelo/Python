questions = [
    {
    "question":"1- What command you use on Mac to create a new folder in console?",
    "possible_answers": [
        "1) mkdir",
        "2) makedir",
        "3) dir",
        "4) ls"
        ],
        "correct_answer":'1'
    },
    {
    "question": "2- How do you define text or strings in Python?",
    "possible_answers": [
        "1) only wrapping a text with single quotes",
        "2) only wrapping a text with double quotes",
        "3) wrapping a text with single or double quotes or even with \"\"\" ",
        "4) none of the above is true"
        ],
        "correct_answer": '3'
    },
    {
    "question":"3- How you could transform number to string in Python?",
    "possible_answers": [
        "1) using float() function",
        "2) using str() function",
        "3) using string() function",
        "4) using .text() method"
        ],
        "correct_answer": '2'
    },
    {
    "question":"4- When you compare two values and want to check if value A is equal to value B, how do you compare it in Python?",
    "possible_answers" : [
        "1) using =",
        "2) using ==",
        "3) using =!",
        "4) using <>"
        ],
        "correct_answer": '2'
    },
    {
    "question":"5- What is a correct way in Python to represent boolean true value?",
    "possible_answers":[
        "1) true",
        "2) TRUE",
        "3) 1",
        "4) True"
        ],
    "correct_answer": '4'
    },
    {
    "question":"6- If you want to create a dictionary in Python you use:",
    "possible_answers": [
        "1) []",
        "2) ()",
        "3) {}",
        "4) <>"
        ],
    "correct_answer": '3'
    },
    {
    "question":"7- If we have dictionary like this: \n participant = {'name':'Ola','languages':['Polish','English','German'],'country':'Poland'} \nhow we would check how many languages Ola speaks?",
    "possible_answers": [
        "1) len(participant['languages'])",
        "2) participant['languages'].count()",
        "3) len(participant)",
        "4) participant['languages'].items()"
        ],
        "correct_answer": '1'
    },
    {
    "question":"8- When we want to define a function in Python what keyword we use?",
    "possible_answers": [
        "1) func",
        "2) function",
        "3) var",
        "4) def"
        ],
    "correct_answer": '4'
    },
    {
    "question":"9-Which from the below is not correct boolean operator in Python?",
    "possible_answers": [
        "1) and",
        "2) xor",
        "3) or",
        "4) not"
        ],
    "correct_answer": '2'
    },
    {
    "question":"10- Which of the below is correct syntax in Python when defining for loop?",
    "possible_answers": [
        "1) forloop(u in users):",
        "2) for(var u in users):",
        "3) for u in users:",
        "4) foreach user in users:"
        ],
    "correct_answer": '3'
    },
]

result = 0

for question_definition in questions:
    print(question_definition["question"])
    for possible_answer in question_definition["possible_answers"]:
        print(possible_answer)

    answer = input(">>> ")
    if answer.strip() == question_definition["correct_answer"]:
        result = result + 1



print("Your score is: {} out of 10 questions".format(result))
