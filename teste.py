#Criando um teste com pontuação--
print("teste seus conhecimentos sobre ciências🔢 ")
pontos = 0
#--questão 1--
print("qual é a formula da água?♒ ")
print("a-H20\n b-c08\n c-AL")
resposta1 = input("digite a resposta: ").lower()
if resposta1 =="a":
   print("resposta correta✅ ")
   pontos = pontos +1
else:
   print("você errou!❌")
#-questão 2--
print("2-O sol é :☀️ ")
print("a-satélite\n b-estrela\n c-asteróide")
resposta2 = input("digite a resposta: ").lower()
if resposta2 == "b":
   print("voce acertou✅ ")
   pontos = pontos + 1
else:
   print("você errou❌ ")
print("fim do questionario")
print(f"sua pontuação foi:{pontos}")
#arthur dantas da silva--