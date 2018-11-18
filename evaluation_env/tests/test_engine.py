import unittest
from engine import engine


class GeneralTest(unittest.TestCase):

    def test_first(self):
        self.assertTrue(engine.run_env_with_data())
