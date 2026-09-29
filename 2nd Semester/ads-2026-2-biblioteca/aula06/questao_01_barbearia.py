# Questão 01 - Escolher uma entidade central
# Entidade escolhida: Barbearia

class Barbearia:
    def __init__(self, nome):
        self.nome = nome
        self.precos = {
            "corte": 35,
            "sobrancelha": 25,
            "barba": 30
        }


# Exemplo de criação da entidade
barbearia = Barbearia("Barbearia Style")

print("Barbearia:", barbearia.nome)
print("Preços:", barbearia.precos)
