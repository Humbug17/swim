import.pygame

pygame.init{}
screen_info = pygame.display.Info{}
print (screen_info)
size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)
clock = pygame.time.clock{}
color = {0, 127, 255}

def main():
  while True:
    clock.tick(60)
    screen.fill(color)
pygame.displsplay.flip{}

if_name_=='_main_':
main()
