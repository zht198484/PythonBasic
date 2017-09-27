import random
import unittest


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def tearDown(self):
        pass

    def testshuffle(self):
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))

    def testchoice(self):
        self.assertTrue(random.choice([1]) in self.seq)
        self.assertTrue(random.choice([2]) in self.seq)

    def testsample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)

if __name__ == '__main__':
    unittest.main()