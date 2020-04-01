import unittest
from sudoku import Board, Cell

#first time - don't judge :)

class TestSudoku(unittest.TestCase):

    example = [
        [0,2,4,  0,6,0,  0,0,1],
        [0,0,0,  0,0,0,  0,7,9],
        [0,7,1,  0,3,8,  0,0,0],

        [0,0,0,  0,0,3,  5,0,0],
        [0,8,6,  0,5,0,  1,3,0],
        [0,0,5,  1,0,0,  0,0,0],

        [0,0,0,  4,7,0,  6,9,0],
        [1,0,0,  0,9,0,  8,5,0],
        [6,9,0,  0,0,0,  0,0,0],
    ]
    b = Board(example)

    def test_getcell(self):
        self.assertEqual(self.b.getCell(1,0).getContent(), 2)
        self.assertEqual(self.b.getCell(2,0).getContent(), 4)
        self.assertEqual(self.b.getCell(4,2).getContent(), 3)
        self.assertEqual(self.b.getCell(4,6).getContent(), 7)
        self.assertEqual(self.b.getCell(0,8).getContent(), 6)
        self.assertEqual(self.b.getCell(8,0).getContent(), 1)

        self.assertEqual(self.b.getCell(1,4).getContent(), 8)
        self.assertNotEqual(self.b.getCell(4,1).getContent(), 8)
        self.assertEqual(self.b.getCell(2,4).getContent(), 6)

    def test_isinrow(self):
        self.assertTrue(self.b.is_in_row(7,2))
        self.assertTrue(self.b.is_in_row(1,2))
        self.assertTrue(self.b.is_in_row(3,2))
        self.assertTrue(self.b.is_in_row(8,2))

        self.assertFalse(self.b.is_in_row(2,2))
        self.assertFalse(self.b.is_in_row(4,2))
        self.assertFalse(self.b.is_in_row(5,2))
        self.assertFalse(self.b.is_in_row(6,2))
        self.assertFalse(self.b.is_in_row(9,2))

        self.assertTrue(self.b.is_in_row(1,0))

    def test_isincol(self):
        self.assertTrue(self.b.is_in_col(6,4))
        self.assertTrue(self.b.is_in_col(3,4))
        self.assertTrue(self.b.is_in_col(5,4))
        self.assertTrue(self.b.is_in_col(7,4))
        self.assertTrue(self.b.is_in_col(9,4))

        self.assertFalse(self.b.is_in_col(1,4))
        self.assertFalse(self.b.is_in_col(2,4))
        self.assertFalse(self.b.is_in_col(4,4))
        self.assertFalse(self.b.is_in_col(8,4))

        self.assertTrue(self.b.is_in_row(6,0))

    def test_isinbox(self):
        self.assertTrue(self.b.is_in_box(6,7,7))
        self.assertTrue(self.b.is_in_box(9,7,7))
        self.assertTrue(self.b.is_in_box(8,7,7))
        self.assertTrue(self.b.is_in_box(5,7,7))

        self.assertFalse(self.b.is_in_box(1,7,7))
        self.assertFalse(self.b.is_in_box(2,7,7))
        self.assertFalse(self.b.is_in_box(3,7,7))
        self.assertFalse(self.b.is_in_box(4,7,7))
        self.assertFalse(self.b.is_in_box(7,7,7))

    def test_islegal(self):
        self.assertTrue(self.b.is_legal(3,2,1))
        self.assertTrue(self.b.is_legal(8,2,1))

        self.assertFalse(self.b.is_legal(4,2,1))
        self.assertFalse(self.b.is_legal(7,2,1))
        self.assertFalse(self.b.is_legal(6,2,1))
        self.assertFalse(self.b.is_legal(1,2,1))

    def test_nextcell(self):
        self.assertEqual(self.b.next_cell(self.b.getCell(0,0)).getContent(), 2)
        self.assertEqual(self.b.next_cell(self.b.getCell(1,0)).getContent(), 4)

    def test_write(self):
        self.assertEqual(self.b.getCell(0,1).getContent(),0)
        self.b.write(4,0,1)
        self.assertEqual(self.b.getCell(0,1).getContent(),4)

        self.assertEqual(self.b.getCell(4,6).getContent(),7)
        self.b.write(8,4,6)
        self.assertEqual(self.b.getCell(4,6).getContent(),8)

        self.assertEqual(self.b.getCell(7,1).getContent(),7)
        self.b.write(4,7,1)
        self.assertEqual(self.b.getCell(7,1).getContent(),4)


        

