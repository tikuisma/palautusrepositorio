import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12), #yht. 16   5
            Player("Lemieux", "PIT", 45, 54), #yht. 99  2
            Player("Kurri",   "EDM", 37, 53), #yht. 90  4
            Player("Yzerman", "DET", 42, 56), #yht. 98  3
            Player("Gretzky", "EDM", 35, 89) #yht. 124  1
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_none(self):
        player = "Lehtonen"
        find = self.statistics.search(player)
        self.assertEqual(find, None)
    
    def test_search(self):
        self.assertEqual(self.statistics.search("Kurri").name, "Kurri")

    def test_team(self):
        players = self.statistics.team("PIT")
        self.assertEqual(len(players), 1)
    
    def test_top(self):
        players = self.statistics.top(1)
        self.assertEqual(len(players), 2)
