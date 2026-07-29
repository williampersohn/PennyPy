import unittest
from unittest.mock import patch
from project import work
from project import change
from project import originalbudget, budgets
from project import monthly

class TestWorkFunction(unittest.TestCase):
    @patch('sys.argv', ['test_project.py', 'arg1', 'arg2'])
    def test_work(self):
        self.assertEqual(work('utilitties', '10.00', 'utilitties'), "Typo! Try again.")
        self.assertEqual(work('uttilities', '10', 'uttilities'), "Typo! Try again.")
        with open("expenses.txt") as fil:
            self.assertEqual(work('Utilities', '10.00', 'Utilities'), f"Changed Utilities\n\n{fil.read()}")
        with open("expenses.txt") as fil:
            self.assertEqual(work('Groceries', '100.00', 'Groceries'), f"Changed Groceries\n\n{fil.read()}")


def test_monthly():
    with open("a.txt", "w") as f:
        f.write("1")
    monthly()
    with open("a.txt", "r") as f:
        a = f.read()
    assert a == "2"

def test_change():
    assert change("3000.00", "100.00") == " $2900.00"
    assert change("1200.00", "24.00") == " $1176.00"
    assert change("100.00", "10.00") == " $90.00"
    assert change("200.00", "5.00") == " $195.00"
    assert change("400.00" , "421.00") == " $-21.00"
    assert change("100.00", "0.01") == " $99.99"

def test_original_budget():
    global budgets
    assert originalbudget() == "Original Budget:\n" + budgets


if __name__ == '__main__':
    unittest.work()
    test_change()
    test_original_budget()
    test_monthly()
    test_change()
