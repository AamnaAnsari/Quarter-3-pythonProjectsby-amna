import tkinter as tk
import random

WIDTH = 600
HEIGHT = 600
PLAYER_SPEED = 20
BULLET_SPEED = 15
ENEMY_SPEED = 5

class SpaceInvaders:
    def __init__(self, root):
        self.root = root
        self.root.title("Space Invaders - Tkinter Edition")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.score = 0
        self.game_over = False

        self.player = self.canvas.create_rectangle(WIDTH//2 - 25, HEIGHT - 40, WIDTH//2 + 25, HEIGHT - 20, fill="green")

        self.bullets = []
        self.enemies = []
        self.create_enemy()

        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<space>", self.fire_bullet)

        self.update_game()

    def move_left(self, event):
        if not self.game_over:
            self.canvas.move(self.player, -PLAYER_SPEED, 0)

    def move_right(self, event):
        if not self.game_over:
            self.canvas.move(self.player, PLAYER_SPEED, 0)

    def fire_bullet(self, event):
        if not self.game_over:
            x1, y1, x2, y2 = self.canvas.coords(self.player)
            bullet = self.canvas.create_oval((x1 + x2)//2 - 5, y1 - 10, (x1 + x2)//2 + 5, y1, fill="red")
            self.bullets.append(bullet)

    def create_enemy(self):
        for _ in range(5):
            x = random.randint(50, WIDTH - 50)
            enemy = self.canvas.create_rectangle(x, 20, x + 40, 60, fill="orange")
            self.enemies.append(enemy)

    def update_game(self):
        if not self.game_over:
            # Move bullets
            for bullet in self.bullets[:]:
                self.canvas.move(bullet, 0, -BULLET_SPEED)
                if self.canvas.coords(bullet)[1] <= 0:
                    self.canvas.delete(bullet)
                    self.bullets.remove(bullet)

            # Move enemies
            for enemy in self.enemies[:]:
                self.canvas.move(enemy, 0, ENEMY_SPEED)
                ex1, ey1, ex2, ey2 = self.canvas.coords(enemy)
                if ey2 >= HEIGHT:
                    self.end_game()

            # Collision detection
            for bullet in self.bullets[:]:
                bx1, by1, bx2, by2 = self.canvas.coords(bullet)
                for enemy in self.enemies[:]:
                    ex1, ey1, ex2, ey2 = self.canvas.coords(enemy)
                    if bx1 < ex2 and bx2 > ex1 and by1 < ey2 and by2 > ey1:
                        self.canvas.delete(bullet)
                        self.canvas.delete(enemy)
                        self.bullets.remove(bullet)
                        self.enemies.remove(enemy)
                        self.score += 1
                        break

            # Show score
            self.canvas.delete("score")
            self.canvas.create_text(10, 10, text=f"Score: {self.score}", fill="white", anchor="nw", font=("Arial", 12), tags="score")

          
            if not self.enemies:
                self.create_enemy()

            self.root.after(50, self.update_game)

    def end_game(self):
        self.game_over = True
        self.canvas.create_text(WIDTH//2, HEIGHT//2, text="GAME OVER", fill="red", font=("Arial", 30))


if __name__ == "__main__":
    root = tk.Tk()
    game = SpaceInvaders(root)
    root.mainloop()
