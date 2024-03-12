import unittest
from task2 import is_palindrome

class TestTask2(unittest.TestCase):
    def test_failure_cases(self):
        failure_cases = [
            "Козак не Козак.",
            "Ой у лузі червона калина...",
            "Текст пісні Сердючки"
        ]

        for test_str in failure_cases:
            self.assertEqual(is_palindrome(test_str), False)

    def test_success_cases(self):
        success_cases = [
            "Козак з казок.",
            "Уже лисі ліси... Лежу.",
            "І що сало? Ласощі..."
        ]

        for test_str in success_cases:
            self.assertEqual(is_palindrome(test_str), True)
            
if __name__ == '__main__':
    unittest.main()
