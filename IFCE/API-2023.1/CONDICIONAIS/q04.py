respostas_positivas = 0
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

print("Responda as perguntas com \033[1mSim\033[m ou \033[1mNão\033[m.")

for pergunta in perguntas:
    resposta = input(pergunta + ' ')
    if(resposta.lower() == 'sim'):
        respostas_positivas += 1
        
if(respostas_positivas == 2):
    print(f"Você é \033[33msuspeito\033[m do crime.")
elif( 3 <= respostas_positivas <=4):
    print("Você é considerado \033[1mcumplice\033[m do crime.")
elif (respostas_positivas == 5):
    print("Você é o \033[31massassino\033[m")
else: 
    print("Você é inocente.")
