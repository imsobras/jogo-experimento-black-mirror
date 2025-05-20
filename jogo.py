
import random
import emoji
print("Olá, seja bem-vindo à nossa organização " + emoji.emojize(":Japanese_congratulations_button:", language='alias'))
print("simulate.version.2.5.8 " + emoji.emojize(":rocket:", language='alias'))
nome=str(input("Pra começar o nosso teste preciso saber de algumas informações, poderia me dizer o seu nome? "))
if nome.lower() == "lucas": #o .lower transforma a input toda em letra minuscula então não tem preocupação com erros
    print("Prazer em te conhecer Pedro!!")
else:
    print("Prazer em te conhecer Lucas!!!")
print(f"Perdão, meu sistema está sobrecarregado e eu acabei errando seu nome, vamos recaptular, seu nome é {nome} né?")
idade=int(input("Quantos anos você tem? "))
if idade >= 99:
    print(f"Meudeus {nome} você é quase um ser ancestral")
elif idade >= 50:
    print(f"Parabéns por conseguir passar dos 50 anos, imagino que não tenha sido fácil")
elif idade >= 35:
    print(f"{nome} você está numa ótima idade {nome},a vida ainda pode te surpreender")
elif idade >= 18:
    print(f"Você é a cobaia perfeita pro nosso experimento {nome}! {idade} anos e muitos neurônios na cabeça... ")
else:
    print(f"Você não está qualificado pra participar do nosso experimento, desligue esse computador agora.")
comida=(input("Qual a sua comida favorita? "))
respostas = ["Que original...","Nunca ouvi essa resposta antes, você acredita?","Legal... proxima pergunta"]
if comida == "pizza":
    print("Ah, pizza... você e 90% da população não tem o mínimo de personalidade.")
else:
    print(random.choice(respostas))
#super interessante a biblioteca random pra randomizar respostas, cria as respostas e separa por virgula e colchete e dps printa (random.choice(respostas)
print(f"Vamos parar de enrolação {comida}, quer dizer.. {nome} perdão pela confusão... vou falar as regras pra você")
pronto=input("você está preparado? (DIGITE) SIM OU (NAO): ")
if pronto.lower() == "sim":
    print("Seus níveis de autoconfiança estão ótimos, vou explicar nossas únicas 3 regras")
else:
    print(f"Não brinque comigo {nome}... {pronto} não é uma resposta nessa experiencia...")
print("REGRA NÚMERO 1: você precisa ser humano pra participar da experiencia")
print("REGRA NÚMERO 2: nada que você ver aqui poderá ser comunicado ao mundo exterior")
print("REGRA NÚMERO 3: Sempre responda com sabedoria...")
input("Aperte ENTER para continuar... ")
pontos=0
resposta = input("Qual o seu nome? ")
if resposta.lower() == "lucas":
    pontos=pontos+1
    print(f"Parabéns {nome} você acertou a primeira pergunta e marcou {pontos} ponto.")
else:
    print(f"Poxa, que pena Lucas, resposta errada, sua pontuação continua em {pontos} pontos.")

resposta = input("Quantos caracteres tem essa palavra: 'experiência'? ")
if resposta == "13":
    pontos = pontos + 1
    print(f"Parabéns {nome} você acertou e garantiu {pontos} pontos, mas suas escolhas são questionaveis")
else:
    print("Você errou, eu perguntei caracteres e não letras. Vou subtrair todos os seus pontos... brincadeira, vamos para a terceira pergunta ")
input("Aperte ENTER para a terceira pergunta... ")
resposta = input("Você está sozinho agora?")
if resposta.lower() == "sim":
    pontos +=1
    print("Interessante. A solidão revela verdades que a presença dos outros esconde.")
else:
    print("Entendo. Mesmo cercado de pessoas, muitos ainda estão sozinhos por dentro.")
print("\nAnalisando suas respostas...")
import time #não sei usar o import time ainda mas deixarei aqui pra estudar mais tarde
for i in range(3):
    print(".", end="", flush=True)
    time.sleep(1)

print("\nProcesso concluído.")

if pontos >= 2:
    print(f"{nome}, você demonstrou alta compatibilidade com o nosso protocolo. A Unidade vai te buscar em até 48 horas. Prepare-se.")
else:
    print(f"{nome}, infelizmente você foi classificado como **inapto**. Sua memória será reinicializada em instantes...")

input("\nAperte ENTER para encerrar...")

print("Desligando sistema...")

time.sleep(2)
print(f"ERRO: O sistema não pode ser desligado. Você já está dentro dele {nome}.")
