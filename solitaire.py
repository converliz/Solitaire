'''
Solitaire Clone.
'''
import arcade

#screen title & size
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_TITLE = "Liz's Solitaire Game"

class MyGame(arcade.Window):
    """Main application class"""

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Setup game, call function to start """
        pass

    def on_draw(self):
        """ Render Screen """
        #Clear screen
        arcade.start_render()

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when user presses mouse button """
        pass

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        """ Called when user presses mouse button """
        pass

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ User moves mouse """
        pass

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()