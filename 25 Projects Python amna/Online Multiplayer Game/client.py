import pygame
import socket
import pickle

WIDTH, HEIGHT = 500, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multiplayer Game")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5555))

def draw(players):
    win.fill((255, 255, 255))
    pygame.draw.rect(win, (255, 0, 0), (*players[0], 50, 50))
    pygame.draw.rect(win, (0, 0, 255), (*players[1], 50, 50))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    pos = pickle.loads(client.recv(1024))

    run = True
    while run:
        clock.tick(60)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            pos = (pos[0] - 5, pos[1])
        if keys[pygame.K_RIGHT]:
            pos = (pos[0] + 5, pos[1])
        if keys[pygame.K_UP]:
            pos = (pos[0], pos[1] - 5)
        if keys[pygame.K_DOWN]:
            pos = (pos[0], pos[1] + 5)

        try:
            client.send(pickle.dumps(pos))
            players = pickle.loads(client.recv(1024))
            draw(players)
        except:
            print("Lost connection to server.")
            run = False

    pygame.quit()

main()
