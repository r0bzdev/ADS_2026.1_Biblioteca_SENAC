# Questão 02 - Criar a classe com __init__

class Barbearia:
    def __init__(self, nome):
        self.nome = nome
        self.precos = {
            "corte": 35,
            "sobrancelha": 25,
            "barba": 30
        }
        self.comanda = []
        self._total = 0


# Exemplo de uso
barbearia = Barbearia("Barbearia Style")

print("Nome:", barbearia.nome)
print("Preços:", barbearia.precos)
print("Comanda:", barbearia.comanda)
print("Total:", barbearia._total)
