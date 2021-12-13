import unittest
import assembleGenome

class AssemblyTest(unittest.TestCase):
    def overlapTest2Char(self):
        self.assertEquals(assembleGenome.overlap('AT', 'TA'), 'ATA')
    def overlapTest3Char(self):
        self.assertEquals(assembleGenome.overlap('ATC', 'TCA'), 'ATCA')

if __name__ == '__main__':
    unittest.main()