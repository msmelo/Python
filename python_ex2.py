print ("Questionário qualquer")

p1 = input("1- What command you use on Mac to create a new folder in console? \n1) mkdir \n2) makedir \n3) dir \n4) ls \n")
p1=float(p1)
if p1 > 4:
    print("Valor inválido, resposta desconsiderada")
if p1==4:
    p1=1
else:
    p1=0

p2 = input("2- How do you define text or strings in Python? \n1) only wrapping a text with single quotes \n2) only wrapping a text with double quotes \n3) wrapping a text with single or double quotes or even with \"\"\"  \n4) none of the above is true \n")
p2=float(p2)
if p2 > 4:
    print("Valor inválido, resposta desconsiderada")
if p2==4:
    p2=1
else:
    p2=0

p3 = input("3- How you could transform number to string in Python? \n1) using float() function \n2) using str() function \n3) using string() function \n4) using .text() method \n")
p3=float(p3)
if p3 > 4:
    print("Valor inválido, resposta desconsiderada")
if p3==2:
    p3=1
else:
    p3=0

p4 = input("4- When you compare two values and want to check if value A is equal to value B, how do you compare it in Python? \n1) using = \n2) using == \n3) using =! \n4) using <> \n")
p4=float(p4)
if p4 > 4:
    print("Valor inválido, resposta desconsiderada")
if p4==2:
    p4=1
else:
    p4=0

p5 = input("5- What is a correct way in Python to represent boolean true value? \n1) true \n2) TRUE \n3) 1 \n4) True \n")
p5=float(p5)
if p5 > 4:
    print("Valor inválido, resposta desconsiderada")
if p5==1:
    p5=1
else:
    p5=0

p6 = input("6- If you want to create a dictionary in Python you use: \n1) [] \n2) () \n3) {} \n4) <> \n")
p6=float(p6)
if p6 > 4:
    print("Valor inválido, resposta desconsiderada")
if p6==3:
    p6=1
else:
    p6=0

p7 = input("7- If we have dictionary like this: \n participant = {'name':'Ola','languages':['Polish','English','German'],'country':'Poland'} \nhow we would check how many languages Ola speaks? \n1) len(participant['languages']) \n2) participant['languages'].count() \n3) len(participant) \n4) participant['languages'].items() \n")
p7=float(p7)
if p7 > 4:
    print("Valor inválido, resposta desconsiderada")
if p7==2:
    p7=1
else:
    p7=0

p8 = input("8- When we want to define a function in Python what keyword we use? \n1) func \n2) function \n3) var \n4) def \n")
p8=float(p8)
if p8 > 4:
    print("Valor inválido, resposta desconsiderada")
if p8==4:
    p8=1
else:
    p8=0

p9 = input("9-Which from the below is not correct boolean operator in Python? \n1) and \n2) xor \n3) or \n4) not \n")
p9=float(p9)
if p9 > 4:
    print("Valor inválido, resposta desconsiderada")
if p9==2:
    p9=1
else:
    p9=0

p10 = input("10- Which of the below is correct syntax in Python when defining for loop? \n1) forloop(u in users): \n2) for(var u in users): \n3) for u in users: \n4) foreach user in users: \n")
p10=float(p10)
if p10 > 4:
    print("Valor inválido, resposta desconsiderada")
if p10==1:
    p10=1
else:
    p10=0
soma = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10
print("Você acertou "+ str(soma) +" de 10 questões.")
