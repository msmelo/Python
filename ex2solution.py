question_1 = """1- What command you use on Mac to create a new folder in console?\n
1) mkdir\n
2) makedir\n
3) dir\n
4) ls\n"""
question_2 = """2- How do you define text or strings in Python?\n
1) only wrapping a text with single quotes\n
2) only wrapping a text with double quotes\n
3) wrapping a text with single or double quotes or even with \"\"\"  \n
4) none of the above is true\n"""
question_3 = """3- How you could transform number to string in Python? \n
1) using float() function\n
2) using str() function\n
3) using string() function\n
4) using .text() method\n"""
question_4 = """4- When you compare two values and want to check if value A is equal to value B, how do you compare it in Python?\n
1) using =\n
2) using ==\n
3) using =!\n
4) using <>\n"""
question_5 = """5- What is a correct way in Python to represent boolean true value?\n
1) true\n
2) TRUE\n
3) 1\n
4) True\n"""
question_6 = """6- If you want to create a dictionary in Python you use:\n
1) []\n
2) ()\n
3) {}\n
4) <>\n"""
question_7 = """7- If we have dictionary like this: \n participant = {'name':'Ola','languages':['Polish','English','German'],'country':'Poland'} \nhow we would check how many languages Ola speaks? \n
1) len(participant['languages'])\n
2) participant['languages'].count()\n
3) len(participant)\n
4) participant['languages'].items()\n"""
question_8 = """8- When we want to define a function in Python what keyword we use? \n
1) func\n
2) function\n
3) var\n
4) def\n"""
question_9 = """9-Which from the below is not correct boolean operator in Python? \n
1) and\n
2) xor\n
3) or\n
4) not\n"""
question_10 = """10- Which of the below is correct syntax in Python when defining for loop? \n
1) forloop(u in users):\n
2) for(var u in users):\n
3) for u in users:\n
4) foreach user in users:\n"""

answer_1 = input(question_1)
answer_2 = input(question_2)
answer_3 = input(question_3)
answer_4 = input(question_4)
answer_5 = input(question_5)
answer_6 = input(question_6)
answer_7 = input(question_7)
answer_8 = input(question_8)
answer_9 = input(question_9)
answer_10 = input(question_10)

result = 0

if answer_1 == '1':
    result = result + 1
if answer_2 == '3':
    result = result + 1
if answer_3 == '2':
    result = result + 1
if answer_4 == '2':
    result = result + 1
if answer_5 == '4':
    result = result + 1
if answer_6 == '3':
    result = result + 1
if answer_7 == '1':
    result = result + 1
if answer_8 == '4':
    result = result + 1
if answer_9 == '2':
    result = result + 1
if answer_10 == '3':
    result = result + 1

print("Your score is: {} out of 10 questions".format(result))
