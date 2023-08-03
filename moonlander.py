class Moonlander:
    def __init__(self, first_position, first_direction):
        self.position = first_position
        self.direction = first_direction
    
    def executecommands(self, command):
        if command == 'f':
            if self.direction == 'N':
                self.position = (self.position[0], self.position[1] + 1, self.position[2])
            elif self.direction == 'S':
                    self.position = (self.position[0], self.position[1] - 1, self.position[2])
            elif self.direction == 'E':
                self.position = (self.position[0] + 1, self.position[1], self.position[2])
            elif self.direction == 'W':
                self.position = (self.position[0] - 1, self.position[1], self.position[2])
            elif self.direction == 'U':
                self.position = (self.position[0], self.position[1], self.position[2] + 1)
            elif self.direction == 'D':
                    self.position = (self.position[0], self.position[1], self.position[2] - 1)
        elif command == 'b':
            if self.direction == 'N':
                self.position = (self.position[0], self.position[1] - 1, self.position[2])
            elif self.direction == 'S':
                self.position = (self.position[0], self.position[1] + 1, self.position[2])
            elif self.direction == 'E':
                self.position = (self.position[0] - 1, self.position[1], self.position[2])
            elif self.direction == 'W':
                self.position = (self.position[0] + 1, self.position[1], self.position[2])
            elif self.direction == 'U':
                self.position = (self.position[0], self.position[1], self.position[2] - 1)
            elif self.direction == 'D':
                self.position = (self.position[0], self.position[1], self.position[2] + 1)
        elif command == 'l':
            if self.direction == 'N':
                self.direction = 'W'
            elif self.direction == 'S':
                self.direction = 'E'
            elif self.direction == 'E':
                self.direction = 'N'
            elif self.direction == 'W':
                self.direction = 'S'
            elif self.direction == 'U':
                self.direction = 'W'
            elif self.direction == 'D':
                self.direction = 'S'
        elif command == 'r':
            if self.direction == 'N':
                self.direction = 'E'
            elif self.direction == 'S':
                self.direction = 'W'
            elif self.direction == 'E':
                self.direction = 'S'
            elif self.direction == 'W':
                self.direction = 'N'
            elif self.direction == 'U':
                self.direction = 'S'
            elif self.direction == 'D':
                self.direction = 'N'
        elif command == 'u':
            if self.direction in ['N', 'E', 'W', 'S']:
                self.direction = 'U'
            elif self.direction == 'D':
                self.direction = 'S'
            elif self.direction == 'U':
                self.direction = 'N'
            
        elif command == 'd':
            if self.direction in ['N', 'E', 'W', 'S']:
                self.direction = 'D'
            elif self.direction == 'U':
                self.direction = 'N'
            elif self.direction == 'D':
                self.direction = 'S'
            