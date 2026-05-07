"""Cannon, hitting targets with projectiles.

Exercises

(done)
1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
(done)
4. Change the speed of the ball.
5. The movement speed for the projectile and the balls is faster
(done)
6. Make the game never end, so that the balls reposition themselves when they go out of the window.
"""

from random import randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []
score = 0 

def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    goto(-60, 170)
    color('black')
    write(f'Score: {score}', font = ('Courier', 14, 'bold'))

    update()


def move():    
    """Move ball and targets."""
    global score
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

        else:
            score += 1

    draw()

    for target in targets:
        if not inside(target):
            
            target.x = 200
            target.y = randrange(-150, 150)

    ontimer(move, 40)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
