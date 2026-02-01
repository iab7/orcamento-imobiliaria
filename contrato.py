class Contrato:
    def __init__(self, valor_contrato=2000):
        self.valor_contrato = valor_contrato

    def parcelar(self, parcelas):
        if parcelas > 5:
            parcelas = 5

        return round(self.valor_contrato / parcelas, 2)
    