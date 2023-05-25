import unittest

class TestFoo(unittest.TestCase):
    def test_add(self):
        assert 1 + 1 == 2, "Expected 1 + 1 to equal 2"

if __name__ == "__main__":
    unittest.main()
