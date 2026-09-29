# Questão 03 - Migrar duas funções para métodos
# Funções escolhidas:
# 1. somar
# 2. itens_validos

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

    def somar(self, valor):
        self._total += valor
        return self._total

    def itens_validos(self):
        validos = []

        for item in self.comanda:
            if item in self.precos:
                validos.append(item)

        return validos


# Exemplo de uso
barbearia = Barbearia("Barbearia Style")

barbearia.comanda = [
    "corte",
    "barba",
    "sobrancelha",
    "tatuagem"
]

barbearia.somar(35)
barbearia.somar(25)

print("Itens válidos:", barbearia.itens_validos())
print("Total:", barbearia._total)
