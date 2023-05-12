from collections import Counter

meu_texto = "Olá eu sou o ChatGPT um modelo de linguagem criado pela OpenAI para ajudá-lo com suas necessidades sou o melhor no que faço fui criado em python usando um modelo de aprendizagem de máquina."

meu_texto = meu_texto.lower()

aparicoes = Counter(meu_texto.split())

print(aparicoes)