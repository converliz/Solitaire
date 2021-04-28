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


#constants for sizing
CARD_SCALE = 0.6

#how big are the cards?
CARD_WIDTH = 140 * CARD_SCALE
CARD_HEIGHT = 190 * CARD_SCALE

#how big is the mat the card will go on?
MAT_PERCENT_OVERSIZE = 1.25
MAT_HEIGHT = int(CARD_HEIGHT * MAT_PERCENT_OVERSIZE)
MAT_WIDTH = int(CARD_WIDTH * MAT_PERCENT_OVERSIZE)

#how big of a gap left between mats?
VERTICAL_MARGIN_PERCENT = 0.10
HORIZONTAL_MARGIN_PERCENT = 0.10

#y of bottom row, 2 piles
BOTTOM_Y = MAT_HEIGHT / 2 + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT

#X of where to start putting stuff on left side
START_X = MAT_WIDTH / 2 + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT

#Card constants
CARD_VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
CARD_SUITS = ["Clubs", "Hearts", "Spades", "Diamonds"]