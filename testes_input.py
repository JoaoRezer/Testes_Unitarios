import unittest
from unittest.mock import patch

class ContaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        """Deposita um valor na conta."""
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor:.2f} realizado com sucesso!"
        return "Valor de depósito inválido. Deve ser positivo."

    def sacar(self, valor):
        """Saca um valor da conta, garantindo que não fique negativo."""
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso!"
        elif valor > self.saldo:
            return "Saldo insuficiente para o saque."
        return "Valor de saque inválido. Deve ser positivo."

    def exibir_saldo(self):
        return f"Saldo atual: R${self.saldo:.2f}"

class TestContaBancaria(unittest.TestCase):
    def setUp(self):
        self.conta = ContaBancaria("João", 100.0)

    def test_depositar_valor_positivo(self):
        resultado = self.conta.depositar(50.0)
        self.assertEqual(resultado, "Depósito de R$50.00 realizado com sucesso!")
        self.assertEqual(self.conta.saldo, 150.0)

    def test_depositar_valor_negativo(self):
        resultado = self.conta.depositar(-10.0)
        self.assertEqual(resultado, "Valor de depósito inválido. Deve ser positivo.")
        self.assertEqual(self.conta.saldo, 100.0)

    def test_sacar_valor_disponivel(self):
        resultado = self.conta.sacar(50.0)
        self.assertEqual(resultado, "Saque de R$50.00 realizado com sucesso!")
        self.assertEqual(self.conta.saldo, 50.0)

    def test_sacar_valor_indisponivel(self):
        resultado = self.conta.sacar(150.0)
        self.assertEqual(resultado, "Saldo insuficiente para o saque.")
        self.assertEqual(self.conta.saldo, 100.0)

    def test_sacar_valor_negativo(self):
        resultado = self.conta.sacar(-20.0)
        self.assertEqual(resultado, "Valor de saque inválido. Deve ser positivo.")
        self.assertEqual(self.conta.saldo, 100.0)

    def test_exibir_saldo(self):
        resultado = self.conta.exibir_saldo()
        self.assertEqual(resultado, "Saldo atual: R$100.00")

    @patch('builtins.input', side_effect=['Maria'])
    def test_criar_conta_com_input(self, mock_input):
        titular = input("Digite o nome do titular da conta: ")
        conta = ContaBancaria(titular)
        self.assertEqual(conta.titular, "Maria")
        self.assertEqual(conta.saldo, 0.0)

    @patch('builtins.input', side_effect=['50'])
    def test_depositar_com_input(self, mock_input):
        valor = float(input("Digite o valor a ser depositado: R$"))
        resultado = self.conta.depositar(valor)
        self.assertEqual(resultado, "Depósito de R$50.00 realizado com sucesso!")
        self.assertEqual(self.conta.saldo, 150.0)

    @patch('builtins.input', side_effect=['30'])
    def test_sacar_com_input(self, mock_input):
        valor = float(input("Digite o valor a ser sacado: R$"))
        resultado = self.conta.sacar(valor)
        self.assertEqual(resultado, "Saque de R$30.00 realizado com sucesso!")
        self.assertEqual(self.conta.saldo, 70.0)

if __name__ == "__main__":
    unittest.main()
