from .dice import *
class Hand(list):
    """ initialize the parameters """
    def __init__(self, size=0, die_class=None, *args, **kwargs):
        if not die_class:
            raise ValueError("You must provide a die class")
        super().__init__()

        for _ in range(size): # underscore means I don't care about what it is.
            self.append(die_class())
        self.sort()

class YatzyHand(Hand):
    """ Add parameters for yatzyhand """
    def __init__(self, *args, **kwargs):
        super().__init__(size=5, dice_class=D6, *args, **kwargs)
