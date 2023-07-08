import unittest
from core.cuenta import Cuenta


class TestRetiroCuenta(unittest.TestCase):

    def test_retiro_cuenta(self) -> None:
        cuenta = Cuenta()
        cuenta.saldo = 1000
        cuenta.retirar_dinero(300)

        self.assertEqual(cuenta.saldo, 700)

if __name__ == '__main__':
    unittest.main()
