class Rover(object):
    def __init__(self):
        self.x_bounds, self.y_bounds, self.orientation = 0, 0, 0
        self.init_coords_data, self.moves_data, self.moves,  self.output = [], [], [], []
        self.init_coords = {'x': 0, 'y': 0, 'orientation': 'N'}

    def read_file(self, file):
        with open(file, 'r') as f:
            for r in f:
                self.x_bounds, self.y_bounds = r.split()
                self.x_bounds, self.y_bounds = int(self.x_bounds), int(self.y_bounds)
                break
            for i in f:
                line = i.strip()
                if not line:
                    continue
                else:
                    if len(line) < 8:
                        self.init_coords_data.append(line.split())
                    else:
                        self.moves_data.append(line.split())

    def initialise_rover(self):
        for i, j in zip(self.moves_data, self.init_coords_data):
            self.init_coords['x'], self.init_coords['y'], self.init_coords['orientation'] = int(j[0]), int(j[1]), j[2]
            if (self.init_coords['x'] > self.x_bounds) or (self.init_coords['y'] > self.y_bounds):
                print("Initial rover coordinates out of plateau bounds")
            else:
                self.degrees_to_coords()
                self.moves = ','.join([str(x) for x in i])
                self.degrees_to_coords()
                self.move_rover()
                self.output.extend([self.init_coords['x'], self.init_coords['y'], self.init_coords['orientation'], '\n'])

        self.output = ' '.join([str(x) for x in self.output[:-1]])
        print(self.output)
        return self.output

    def move_rover(self):
        for i in self.moves:
            if i == 'L':
                self.rotate_rover('L')
            if i == 'R':
                self.rotate_rover('R')
            if i == 'M':
                if self.orientation == 0 and self.init_coords['y'] < self.y_bounds:
                    self.init_coords['y'] += 1
                if (self.orientation == -90 or self.orientation == 270)\
                        and self.init_coords['x'] > 0:
                    self.init_coords['x'] -= 1
                if (self.orientation == 180 or self.orientation == -180)\
                        and self.init_coords['y'] > 0:
                    self.init_coords['y'] -= 1
                if (self.orientation == 90 or self.orientation == -270)\
                        and self.init_coords['x'] < self.x_bounds:
                    self.init_coords['x'] += 1
        self.coords_to_degrees()


    def degrees_to_coords(self):
        if self.init_coords['orientation'] == 'N':
            self.orientation = 0
        if self.init_coords['orientation'] == 'E':
            self.orientation = 90
        if self.init_coords['orientation'] == 'S':
            self.orientation = 180
        if self.init_coords['orientation'] == 'W':
            self.orientation = 270

    def coords_to_degrees(self):
        if self.orientation == 0:
            self.init_coords['orientation'] = 'N'
        if self.orientation == 90:
            self.init_coords['orientation'] = 'E'
        if self.orientation == 180:
            self.init_coords['orientation'] = 'S'
        if self.orientation == 270:
            self.init_coords['orientation'] = 'W'

    def rotate_rover(self, i):
        if i == 'L':
            self.orientation -= 90
            if self.orientation == -360:
                self.orientation = 0
        if i == 'R':
            self.orientation += 90
            if self.orientation == 360:
                self.orientation = 0
