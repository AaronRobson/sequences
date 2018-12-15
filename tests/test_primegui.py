
import unittest
from primeGUI import PrimeGUI


class TestPrimeGUI(unittest.TestCase):

    def test_initialisation(self):
        gui = PrimeGUI()
        gui.Reset()
