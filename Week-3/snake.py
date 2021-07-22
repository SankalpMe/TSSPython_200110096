import pygame, sys, time, random

#initial game variables

# Window size
frame_size_x = 720
frame_size_y = 480

#Parameters for Snake
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
direction = 'RIGHT'
change_to = direction

#Parameters for food
food_pos = [0,0]
food_spawn = False
food_border = 40
score = 0


# Initialise game window
pygame.init()
pygame.display.set_caption('Snake Eater')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))



# FPS (frames per second) controller to set the speed of the game
fps_controller = pygame.time.Clock()


flipDirs = {'LEFT': 'RIGHT', 'UP': 'DOWN', 'DOWN': 'UP','RIGHT': 'LEFT'}
deltaDirs = {'LEFT': (-10,0), 'RIGHT' : (10,0), 'UP' : (0,-10), 'DOWN': (0,10)}
def check_for_events():
    """
    This should contain the main for loop (listening for events). You should close the program when
    someone closes the window, update the direction attribute after input from users. You will have to make sure
    snake cannot reverse the direction i.e. if it turned left it cannot move right next.
    """
    global change_to
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        elif event.type == pygame.KEYDOWN:
            cdir = None
            key = event.key
            if key == pygame.K_LEFT:
                cdir = "LEFT"
            elif key == pygame.K_RIGHT:
                cdir = "RIGHT"
            elif key == pygame.K_UP:
                cdir = "UP"
            elif key == pygame.K_DOWN:
                cdir = "DOWN"
        
            if cdir:
                if flipDirs[cdir] != direction:
                    change_to = cdir













def update_snake():
    """
     This should contain the code for snake to move, grow, detect walls etc.
     """
    # Code for making the snake move in the expected direction
    global snake_body
    global food_spawn
    global food_pos
    global direction
    global score
    head = snake_body[0][:]
    delta = deltaDirs[change_to]
    head[0] += delta[0]
    head[1] += delta[1]
    dead_body = snake_body[-1]
    snake_body = [head] + snake_body[:-1]
    direction = change_to
    # Make the snake's body respond after the head moves. The responses will be different if it eats the food.
    # Note you cannot directly use the functions for detecting collisions
    # since we have not made snake and food as a specific sprite or surface.
    if food_spawn:
        if food_pos[0] == head[0] and food_pos[1] == head[1]:
            score += 1
            snake_body = snake_body + [dead_body]
            food_spawn = False
        
    
    snake_collided = False
    
    for part in snake_body[1:]:
        if part[0] == head[0] and part[1] == head[1]:
            snake_collided = True
            break

    if head[0] == -10 or head[0] == frame_size_x:
        snake_collided = True
        
    if head[1] == -10 or head[1] == frame_size_y:
        snake_collided = True
    
    
    # End the game if the snake collides with the wall or with itself.
    if snake_collided:
        game_over()
    




def create_food():
    """
    This function should set coordinates of food if not there on the screen. You can use randrange() to generate
    the location of the food.
    """
    global food_spawn
    global food_pos
    if not food_spawn:
        food_pos = [int(random.randrange(food_border,frame_size_x-food_border))//10 * 10,int(random.randrange(food_border,frame_size_y-food_border))//10 * 10]
        food_spawn = True



def show_score(pos, color, font, size):
    """
    It takes in the above arguements and shows the score at the given pos according to the color, font and size.
    """
    pyfont = pygame.font.Font(font,size)
    text = pyfont.render(f"Score : {score}",True,color)
    textRect = text.get_rect()
    textRect.center = (pos[0],pos[1])
    game_window.blit(text,textRect)




def update_screen():
    """
    Draw the snake, food, background, score on the screen
    """
    global food_pos
    game_window.fill((0,0,0))
    
    if food_spawn:
        pygame.draw.rect(game_window,(255,255,255),pygame.Rect(food_pos[0],food_pos[1],10,10))
    for part in snake_body:
        pygame.draw.rect(game_window,(0,255,0),pygame.Rect(part[0],part[1],10,10))
    
    




def game_over():
    """
    Write the function to call in the end.
    It should write game over on the screen, show your score, wait for 3 seconds and then exit
    """
    pygame.time.wait(1000)
    game_window.fill((0,0,0))
    tfont = pygame.font.Font('freesansbold.ttf', 32)
 
    ttext = tfont.render('Game Over', True, (255,0,0))
    
    ttextRect = ttext.get_rect()
    
    ttextRect.center = (frame_size_x//2,frame_size_y //2)
    game_window.blit(ttext,ttextRect)
    show_score((frame_size_x//2,frame_size_y //2+40),(255,255,255),'freesansbold.ttf',20)
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()






# Main loop
while True:
    # Make appropriate calls to the above functions so that the game could finally run
    check_for_events()
    update_snake()
    update_screen()
    
    create_food()
    
    show_score([100,20],(255,255,255),"freesansbold.ttf",10)
    
    pygame.display.flip()
    
    # To set the speed of the screen
    fps_controller.tick(25)

