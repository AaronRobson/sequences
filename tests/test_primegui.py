
import unittest
from prime_gui import PrimeGUI


class TestPrimeGUI(unittest.TestCase):

    def test_initialisation(self):
        gui = PrimeGUI()
        gui.Reset()
