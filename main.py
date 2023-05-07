import pygame
import random

# Define constants for the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Dungeon Management Game"

# Define constants for the map
MAP_WIDTH = 20
MAP_HEIGHT = 15
CORRIDOR_WIDTH = 3
ROOM_SIZE_MIN = 3
ROOM_SIZE_MAX = 7
WALL_COLOR = (100, 100, 100)
FLOOR_COLOR = (50, 50, 50)

# Initialize Pygame
pygame.init()

# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

# Generate the map with random corridors
map_data = []
for y in range(MAP_HEIGHT):
    row = []
    for x in range(MAP_WIDTH):
        if x == 0 or y == 0 or x == MAP_WIDTH-1 or y == MAP_HEIGHT-1:
            # Create a wall at the edge of the map
            row.append(1)
        elif x % (CORRIDOR_WIDTH + ROOM_SIZE_MAX) == 0:
            # Create a corridor
            for i in range(CORRIDOR_WIDTH):
                row.append(0)
        else:
            # Create a room
            room_width = random.randint(ROOM_SIZE_MIN, ROOM_SIZE_MAX)
            room_height = random.randint(ROOM_SIZE_MIN, ROOM_SIZE_MAX)
            room_x = x + random.randint(0, CORRIDOR_WIDTH-1)
            room_y = y + random.randint(0, CORRIDOR_WIDTH-1)
            for j in range(room_height):
                for i in range(room_width):
                    if i == 0 or j == 0 or i == room_width-1 or j == room_height-1:
                        # Create a wall around the room
                        row.append(1)
                    else:
                        # Create a floor inside the room
                        row.append(0)
            x += room_width
    map_data.append(row)

# Draw the map
for y in range(MAP_HEIGHT):
    for x in range(MAP_WIDTH):
        if map_data[y][x] == 1:
            # Draw a wall
            pygame.draw.rect(window, WALL_COLOR, (x*32, y*32, 32, 32))
        else:
            # Draw a floor
            pygame.draw.rect(window, FLOOR_COLOR, (x*32, y*32, 32, 32))

# Update the display
pygame.display.update()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
