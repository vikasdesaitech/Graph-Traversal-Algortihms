import pygame
import bfs


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
WINDOW_SIZE = [510, 510]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Grid")
clock = pygame.time.Clock()


class Grid:
    def __init__(self, *args, **kwargs):
        self.window_width = kwargs.get('window_width', 510)
        self.window_height = kwargs.get('window_height', 510)
        self.block_height = kwargs.get('block_height', 20)
        self.block_width = kwargs.get('block_width', 20)
        self.vcount = kwargs.get('vcount', 20)
        self.hcount = kwargs.get('hcount', 20)
        self.margin = kwargs.get('margin', 5)
        self.total_nodes = 0
        self.idToPos = {}
        self.posTOId = {}
        self.adjacency_list = {}


    def creategrid(self):
        grid = []
        id = 1
        for row in range(self.vcount):
            grid.append([])
            for col in range(self.hcount):
                self.idToPos[id] = (row, col)
                self.posTOId[(row, col)] = id
                id += 1
                grid[row].append(0)
        self.total_nodes = id - 1
        self.createAdjecencyList()
        return grid


    def createAdjecencyList(self):
        for row in range(self.vcount):
            for col in range(self.hcount):
                id = self.posTOId[(row, col)]
                self.adjacency_list[id] = []
                if col > 0:
                    self.adjacency_list[id].append(self.posTOId[(row, col-1)])
                if row > 0:
                    self.adjacency_list[id].append(self.posTOId[(row-1, col)])
                if col < self.hcount - 1:
                    self.adjacency_list[id].append(self.posTOId[(row, col+1)])
                if row < self.vcount - 1:
                    self.adjacency_list[id].append(self.posTOId[(row+1, col)])


    def redraw(self, *args, **kwargs):
        path = kwargs.get('path', None)
        if path:
            for id in path:
                i = self.idToPos[id][0]
                j = self.idToPos[id][1]
                grid[i][j] = 1

        # Draw the grid
        for row in range(self.vcount):
            for column in range(self.hcount):
                color = WHITE
                if grid[row][column] == 1:
                    color = GREEN
                pygame.draw.rect(screen,
                                 color,
                                 [(self.margin + self.block_width) * column + self.margin,
                                  (self.margin + self.block_height) * row + self.margin,
                                  self.block_width,
                                  self.block_height])



gridobj = Grid(window_width=510, window_height=510, block_height=20, block_width=20, hcount=20, vcount=20)
grid = gridobj.creategrid()
bfsobj = bfs.Bfs(adjacency_list=gridobj.adjacency_list, total_nodes=gridobj.total_nodes)



# -------- Main Program Loop -----------
done = False
firstClick = None
secondClick = None

while not done:
    for event in pygame.event.get():
        path = None
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = pos[0] // (gridobj.block_width + gridobj.margin)
            row = pos[1] // (gridobj.block_height + gridobj.margin)
            grid[row][col] = 1
            id = gridobj.posTOId[(row, col)]
            if not firstClick:
                firstClick = id
            else:
                if not secondClick:
                    secondClick = id
                else:
                    firstClick = secondClick
                    secondClick = id
                path = bfsobj.shortestPath(firstClick, secondClick)
                print('start: ', firstClick, 'second: ', secondClick, 'path: ', path)
    screen.fill(BLACK)
    gridobj.redraw(path=path)
    clock.tick(60)
    pygame.display.flip()

pygame.quit()