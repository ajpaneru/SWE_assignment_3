import unittest
from boggle_solver import Boggle


class TestSuiteAlgScalabilityCases(unittest.TestCase):
    """Test suite for various grid sizes to check scalability."""

    def test_normal_case_3x3(self):
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        dictionary = ["abc", "abdhi", "abi", "ef", "cfi", "dea"]
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = ["ABC", "ABDHI", "CFI", "DEA"]
        self.assertEqual(sorted(expected), sorted(solution))

    def test_4x4_grid(self):
        grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],
                ["G", "Z", "Qu", "R"], ["O", "N", "T", "A"]]
        dictionary = ["art", "ego", "gent", "get", "net", "new",
                      "newt", "prat", "pry", "qua", "quart", "quartz",
                      "rat", "tar", "tarp", "ten", "went", "wet",
                      "arty", "not", "quar"]
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = ["ART", "EGO", "GENT", "GET", "NET", "NEW", "NEWT",
                    "PRAT", "PRY", "QUA", "QUART", "QUARTZ", "RAT",
                    "TAR", "TARP", "TEN", "WENT", "WET", "QUAR"]
        self.assertEqual(sorted(expected), sorted(solution))


if __name__ == '__main__':
    unittest.main()
