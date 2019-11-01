import random
import pyxel

# Setting of window.
WINDOW_WIDTH = 255
WINDOW_HEIGHT = 255

# Setting of lottery.
MAX_LOTTERY_NUM = 50

# Setting of image bank.
IMG_BANK0 = 0
IMG_BANK1 = 1
IMG_BANK2 = 2


class App:
    def __init__(self):
        # Initialize window.
        pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT, fps=30, caption='HIVE Roulette')

        # Load image numbers.
        pyxel.image(IMG_BANK0).load(0, 0, 'assets/number_bank_pyxel.png')
        self.one_digit = 0
        self.two_digit = 0
        self.image_numbers = {0: {'u':   0, 'v': 0},
                              1: {'u':  42, 'v': 0},
                              2: {'u':  82, 'v': 0},
                              3: {'u': 123, 'v': 0},
                              4: {'u': 164, 'v': 0},
                              5: {'u':   0, 'v': 69},
                              6: {'u':  42, 'v': 69},
                              7: {'u':  82, 'v': 69},
                              8: {'u': 123, 'v': 69},
                              9: {'u': 164, 'v': 69}}

        # Load other images.
        pyxel.image(IMG_BANK1).load(0, 0, 'assets/customLogo_pyxel.png')
        pyxel.image(IMG_BANK2).load(0, 0, 'assets/pyxel_logo_38x16.png')

        self.result = ''
        self.flags = False

        pyxel.run(self.update, self.draw)

    def update(self):
        # Quit.
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # Start/Stop roulette.
        if pyxel.btnp(pyxel.KEY_W):
            if self.flags is True:
                self.flags = False
            else:
                self.flags = True

    def draw(self):
        # Draw background color (0=black).
        pyxel.cls(0)

        # Display logo.
        pyxel.blt(x=1, y=1, img=IMG_BANK1, u=0, v=0, w=194, h=35)
        pyxel.blt(x=WINDOW_HEIGHT - 38, y=WINDOW_HEIGHT - 16, img=IMG_BANK2, u=0, v=0, w=38, h=16)

        # Execute roulette.
        if self.flags is False:
            self.result = str(random.randint(1, MAX_LOTTERY_NUM))
            if len(self.result) == 1:
                self.result = '0' + self.result
            self.one_digit = int(str(self.result)[0])
            self.two_digit = int(str(self.result)[1])

        # Display numbers.
        pyxel.blt(x=80,
                  y=90,
                  img=IMG_BANK0,
                  u=self.image_numbers[self.one_digit]['u'],
                  v=self.image_numbers[self.one_digit]['v'],
                  w=41,
                  h=69)
        pyxel.blt(x=121,
                  y=90,
                  img=IMG_BANK0,
                  u=self.image_numbers[self.two_digit]['u'],
                  v=self.image_numbers[self.one_digit]['v'],
                  w=41,
                  h=69)

        pyxel.text(int(WINDOW_WIDTH / 2) - 57, int(WINDOW_HEIGHT / 2) + 40,
                   'AV TOKYO 2019 HIVE Lottery.',
                   pyxel.frame_count % 16)

        if self.flags:
            pyxel.text(int(WINDOW_WIDTH / 2) - 40, int(WINDOW_HEIGHT / 2) - 50,
                       'Congratulations!!',
                       pyxel.frame_count % 16)


App()
