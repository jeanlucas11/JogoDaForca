import random

def jogar():
  print("*"*27)
  print("Bem vindo ao jogo da Forca")
  print("*"*27)

  palavraSecreta = carregarPalavraSecreta()
  letrasAcertadas = ["_" for letra in palavraSecreta]
  enforcou = False
  acertou = False
  erros = 0

  print(letrasAcertadas) 
  while(not enforcou and not acertou):
    chute = input("Qual a letra: ")
    chute = chute.strip().upper()

    if chute in palavraSecreta:
      marcarChuteCorreto(palavraSecreta, chute, letrasAcertadas)
    else:
      erros += 1
      print(f"Você errou {erros} de 5 tentativas")
    enforcou = erros == 5
    acertou = "_" not in letrasAcertadas
    print(letrasAcertadas)
  
  if(acertou):
    print("Parabéns, você ganhou!")
  else:
    print(f"Você perdeu! A palavra era {palavraSecreta}")  

def carregarPalavraSecreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavraSecreta = palavras[numero].upper()
    return palavraSecreta

def marcarChuteCorreto(palavraSecreta, chute, letrasAcertadas):
   index = 0
   for letra in palavraSecreta:
      if chute == letra:
        letrasAcertadas[index] = letra

      index += 1

jogar()
