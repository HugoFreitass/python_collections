from collections import Counter

def frequencia_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values()) #".values()" extrai todos o valores do dicionário, "sum" soma todos esses valores e retorna o total de caracteres

    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()] #gera tuplas com o caractere e o percentual de sua aparição

    proporcoes = Counter(dict(proporcoes)) #gera um Counter a partir das tuplas para poder usar o "most_common"
    
    mais_comuns = proporcoes.most_common(10) #o "most_common" pega uma amostra dos maiores valores e retorna uma lista ordenada com tuplas (caractere, percentual)

    for caractere, proporcao in mais_comuns: #desempacota as tuplas 
        print("{} => {:.2f}%".format(caractere, proporcao * 100))


texto = "A inteligência artificial é uma área da Ciência da Computação cujo objetivo é criar sistemas capazes de realizar tarefas que, até então, só poderiam ser executadas por seres humanos.Você já deve estar cansado de ouvir falar nisso. Afinal, a inteligência artificial faz parte de diversos serviços que utilizamos no dia a dia. Recomendadores de filmes em sites de streaming, classificadores de foto em redes sociais ou mesmo classificadores de spam são exemplos de uso de aprendizagem de máquina. Todas essas aplicações são interessantes e úteis. Elas fazem com que seres humanos não tenham que perder tempo realizando atividades mecânicas."

frequencia_letras(texto)