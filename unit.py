import unittest
from unittest.mock import patch
from validators import is_valid_ipv4
from ping_service import ping_host

class TestNetworkMonitor(unittest.TestCase):

    # --- ТЕСТИ ДЛЯ ВАЛІДАТОРА (validators.py) ---

    def test_valid_ipv4(self):
        """Перевірка правильних IPv4 адрес"""
        self.assertTrue(is_valid_ipv4("8.8.8.8"))
        self.assertTrue(is_valid_ipv4("192.168.0.1"))
        self.assertTrue(is_valid_ipv4("0.0.0.0"))
        self.assertTrue(is_valid_ipv4("255.255.255.255"))

    def test_invalid_ipv4_format(self):
        """Перевірка неправильного формату адрес (невірні символи або кількість груп)"""
        self.assertFalse(is_valid_ipv4("192.168.0"))        # мало груп
        self.assertFalse(is_valid_ipv4("192.168.0.1.2"))    # забагато груп
        self.assertFalse(is_valid_ipv4("abc.def.gh.ij"))    # літери замість цифр
        self.assertFalse(is_valid_ipv4("192.168.0.1a"))     # змішані символи
        self.assertFalse(is_valid_ipv4(""))                 # порожній рядок

    def test_invalid_ipv4_ranges(self):
        """Перевірка виходу чисел за межі діапазону 0-255"""
        self.assertFalse(is_valid_ipv4("256.100.100.100"))  # перша група > 255
        self.assertFalse(is_valid_ipv4("192.168.300.1"))    # третя група > 255
        self.assertFalse(is_valid_ipv4("-1.0.0.0"))         # від'ємні числа

    # --- ТЕСТИ ДЛЯ СЕРВІСУ ПІНГУ (ping_service.py) ---

    @patch("ping_service.os.system")
    def test_ping_host_success(self, mock_system):
        """Тест успішного пінгу (хост доступний)"""
        # Симулюємо, що системна команда повернула код 0 (успіх)
        mock_system.return_value = 0
        
        result = ping_host("8.8.8.8")
        
        self.assertEqual(result["status"], "Online")
        self.assertEqual(result["code"], 0)
        self.assertEqual(result["host"], "8.8.8.8")

    @patch("ping_service.os.system")
    def test_ping_host_failure(self, mock_system):
        """Тест невдалого пінгу (хост недоступний)"""
        # Симулюємо, що системна команда повернула код 1 (помилка/таймаут)
        mock_system.return_value = 1
        
        result = ping_host("10.0.0.99")
        
        self.assertEqual(result["status"], "Offline")
        self.assertEqual(result["code"], 1)
        self.assertEqual(result["host"], "10.0.0.99")

if __name__ == "__main__":
    unittest.main()