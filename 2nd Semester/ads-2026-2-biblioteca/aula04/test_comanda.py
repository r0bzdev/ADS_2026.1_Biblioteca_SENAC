from decimal import Decimal

from comanda import fechar, itens_validos, subtotal


def test_subtotal_soma_apenas_o_que_esta_no_catalogo():
    assert subtotal(["corte", "barba", "pintura"]) == Decimal("60.00")

def test_item_fora_do_catalogo_nao_conta_para_o_desconto():
    conta = fechar(["corte", "barba", "pintura"])
    assert conta["desconto"] == Decimal("0.00")
