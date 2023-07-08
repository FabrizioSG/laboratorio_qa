import unittest
from core.cuenta import Cuenta


class TestIngresoCuenta(unittest.TestCase):

    def test_ingreso_cuenta(self) -> None:
        cuenta = Cuenta()
        cuenta.ingresar_dinero(500)

        self.assertEqual(cuenta.saldo, 500)


if __name__ == '__main__':
    unittest.main()
