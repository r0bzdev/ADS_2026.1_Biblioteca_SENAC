# Questão 05 - Adaptar a suíte pytest
# Os testes agora chamam os métodos do objeto Barbearia.

import pytest


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

    def itens_validos(self):
        validos = []

        for item in self.comanda:
            if item in self.precos:
                validos.append(item)

        return validos


def test_somar():
    barbearia = Barbearia("Barbearia Style")

    barbearia.somar(35)
    barbearia.somar(25)

    assert barbearia.total == 60


def test_itens_validos():
    barbearia = Barbearia("Barbearia Style")

    barbearia.comanda = [
        "corte",
        "barba",
        "sobrancelha",
        "tatuagem"
    ]

    resultado = barbearia.itens_validos()

    assert resultado == [
        "corte",
        "barba",
        "sobrancelha"
    ]


def test_total_nao_pode_ser_negativo():
    barbearia = Barbearia("Barbearia Style")

    with pytest.raises(ValueError):
        barbearia.somar(-10)
