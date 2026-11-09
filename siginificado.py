infs = {
        "CRINGE": "Algo vergonhoso ou constrangedor",
        "STALKEAR": "Investigar a vida de alguém online",
        "HATER": "pessoa que está constantemente criticando os outros",
        "VLW": "abreviação da palavra valeu",
        "S": "abreviação de sim",
        "N": "abreviação de nâo",
        "NGM": "abreviação da palavra ninguem",
        "VC": 'abreviação da palavra você'
            }

word = input ("Digite uma palavrea moderna que você não entende, escreva em maiusculo:")
             
if word in infs.keys():
    print(infs[word])

else:
    print("Palavra não encontrada")
