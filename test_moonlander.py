import unittest
from moonlander import Moonlander

class TestChandrayaan(unittest.TestCase):
    def setUp(self):
        self.spacecraft = Moonlander((0, 0, 0), 'N')
        
    def test_initial_position_and_direction(self):
        self.assertEqual(self.spacecraft.position, (0, 0, 0))
        self.assertEqual(self.spacecraft.direction, 'N')

    def test_move_forward(self):
        self.spacecraft.executecommands('f')
        self.assertEqual(self.spacecraft.position, (0, 1, 0))
        self.assertEqual(self.spacecraft.direction, 'N')
    
    def test_move_backward(self):
        self.spacecraft.executecommands('b')
        assert self.spacecraft.position == (0, -1, 0)
        assert self.spacecraft.direction == 'N'

    def test_rotate_left(self):
        self.spacecraft.executecommands('l')
        assert self.spacecraft.position == (0, 0, 0)
        assert self.spacecraft.direction == 'W'

    def test_rotate_right(self):
        self.spacecraft.executecommands('r')
        assert self.spacecraft.position == (0, 0, 0)
        assert self.spacecraft.direction == 'E'

    def test_rotate_up(self):
        self.spacecraft.executecommands('u')
        assert self.spacecraft.position == (0, 0, 0)
        assert self.spacecraft.direction == 'U'
    
    def test_rotate_down(self):
        self.spacecraft.executecommands('d')
        assert self.spacecraft.position == (0, 0, 0)
        assert self.spacecraft.direction == 'D'
    
    def test_multiple_commands(self):
        self.spacecraft.executecommands('f')
        self.spacecraft.executecommands('r')
        self.spacecraft.executecommands('u')
        self.spacecraft.executecommands('b')
        self.spacecraft.executecommands('l')
        assert self.spacecraft.position == (0, 1, -1)
        assert self.spacecraft.direction == 'W'
    
    def test_multiple_commands2(self):
        self.spacecraft.executecommands('f')
        self.spacecraft.executecommands('f')
        self.spacecraft.executecommands('r')
        self.spacecraft.executecommands('r')
        self.spacecraft.executecommands('f')
        self.spacecraft.executecommands('u')
        self.spacecraft.executecommands('b')
        self.spacecraft.executecommands('u')
        self.spacecraft.executecommands('b')
        assert self.spacecraft.position == (0, 0, -1)
        assert self.spacecraft.direction == 'N'
    
    def test_multiple_commands_loop(self):
        command = ['f', 'r', 'u', 'b', 'l']
        for i in command:
            self.spacecraft.executecommands(i)
        assert self.spacecraft.position == (0, 1, -1)
        assert self.spacecraft.direction == 'W'

if __name__ == '__main__':        
    unittest.main(exit = False)
       