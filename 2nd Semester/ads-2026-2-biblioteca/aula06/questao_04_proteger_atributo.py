# Questão 04 - Proteger um atributo
# Atributo protegido: total
# Regra: o total não pode receber valores negativos.

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

    @property
    def total(self):
        return self._total

    def somar(self, valor):
        if valor < 0:
            raise ValueError("O valor não pode ser negativo.")

        self._total += valor
        return self._total


# Exemplo de uso
barbearia = Barbearia("Barbearia Style")

barbearia.somar(35)
barbearia.somar(25)

print("Total:", barbearia.total)

# Teste da regra de negócio
try:
    barbearia.somar(-10)
except ValueError as erro:
    print("Erro:", erro)
