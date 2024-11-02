import runner_and_tournament as rt
import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []
        
    def setUp(self):
        self.r1 = rt.Runner('Усейн', 10)
        self.r2 = rt.Runner('Андрей', 9)
        self.r3 = rt.Runner('Ник', 3)
       
    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(result)
            
    def test_running1(self):
        Tournament1 = rt.Tournament(90, self.r1, self.r3)
        end_r = len(Tournament1.participants)
        self.results = Tournament1.start()
        self.all_results.append({key: value.name for key, value in self.results.items()})
        self.assertTrue(self.results[end_r] == 'Ник')
        
    def test_running2(self):
        Tournament2 = rt.Tournament(90, self.r2, self.r3)
        end_r = len(Tournament2.participants)
        self.results = Tournament2.start()
        self.all_results.append({key: value.name for key, value in self.results.items()})
        self.assertTrue(self.results[end_r] == 'Ник')
        
    def test_running3(self):
        Tournament3 = rt.Tournament(90, self.r2, self.r1, self.r3)
        end_r = len(Tournament3.participants)
        self.results = Tournament3.start()
        self.all_results.append({key: value.name
        for key, value in self.results.items()})
        self.assertTrue(self.results[end_r] == 'Ник')
        
        
if __name__ == '__main__':
    unittest.main()