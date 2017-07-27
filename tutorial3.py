"""
tutorial3.py
by E. Dennison
"""
from ggame import App, RectangleAsset, ImageAsset, SoundAsset, Sprite, Sound
from ggame import LineStyle, Color


myapp = App()

print(myapp.width, myapp.height)

rect = App._win._renderer.view.getBoundingClientRect()
print(rect.left, rect.top, rect.right, rect.bottom, rect.width, rect.height)
print(App._win._stage.scale)

green = Color(0x00ff00, 1)
black = Color(0, 1)
noline = LineStyle(0, black)
bg_asset = RectangleAsset(myapp.width, myapp.height, noline, green)
bg = Sprite(bg_asset, (0,0))

# Sounds
pew1_asset = SoundAsset("sounds/pew1.mp3")
pew1 = Sound(pew1_asset)
pop_asset = SoundAsset("sounds/reappear.mp3")
pop = Sound(pop_asset)
# A ball! This is already in the ggame-tutorials repository
ball_asset = ImageAsset("images/orb-150545_640.png")
ball = Sprite(ball_asset, (0, 0))
# Original image is too big. Scale it to 1/10 its original size
ball.scale = 0.01  # EJD FIX
ball.y = 200
# custom attributes
ball.dir = 0  # EJD FIX
ball.go = True
# Sounds
pew1_asset = SoundAsset("sounds/pew1.mp3")
pew1 = Sound(pew1_asset)
pop_asset = SoundAsset("sounds/reappear.mp3")
pop = Sound(pop_asset)


def reverse(b):
    b.dir *= -1
    pop.play()

# Set up function for handling screen refresh
def step():
    if ball.go:
        ball.x += ball.dir
        if ball.x + ball.width > myapp.width or ball.x < 0:
            ball.x -= ball.dir
            reverse(ball)

# Handle the space key
def spaceKey(event):
    ball.go = not ball.go

# Handle the "reverse" key
def reverseKey(event):
    reverse(ball)

# Handle the mouse click
def mouseClick(event):
    print(event.x, event.y)
    ball.x = event.x
    ball.y = event.y
    pew1.play()

# Set up event handlers for the app
myapp.listenKeyEvent('keydown', 'space', spaceKey)
myapp.listenKeyEvent('keydown', 'r', reverseKey)
myapp.listenMouseEvent('click', mouseClick)

myapp.run(step)
