import unittest
import gen_aes_key


class TestAES(unittest.TestCase):
    def test_gen_aes_key(self):
        key = gen_aes_key.gen_key(0)
        self.assertEqual(len(key), 64)