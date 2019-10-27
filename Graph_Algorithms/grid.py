
class Grid:
    def __init__(self, window_width, window_height, block_width, block_height, margin=5):
        self.window_width = window_width
        self.window_height = window_height
        self.block_height = block_height
        self.block_width = block_width
        self.margin = margin

    def creategrid(self):
        grid = []
        for row in range(20):
            grid.append([])
            for column in range(20):
                grid[row].append(0)
        return grid
