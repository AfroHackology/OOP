import random

class Wisdom:
    patience = True

    def __init__(self, patience=True, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        self.patience = patience

    def experience(self, time):
        return self.patience and time <25

class Agile:
    agile = True
    def __init__(self, agile=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.agile = agile
    def evades(self):
        return self.agile and random.randint(0, 1)

class Level_head:
    level_head = True
    def __init__(self, level_head= True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level_head = level_head

    def emotions(self, anger=0, joy=0, sadness=0,):
        emotion_control = True
        self.anger = anger
        self.joy = joy
        self.sadness = sadness

        total = 0
        while total != 0:
            anger = input(int(self.anger))
            joy = input(int(self.joy))
            sadness = input(int(self.sadness))

            if anger > input(anger):
                print("Controle your anger you must.. {} to high it is!".format(
                    int(self.anger)))
            if joy > input(joy):
                print("Seek happiness in Graditude, meditate more than {}".format(
                    int(self.joy)))
            if sadness > input(joy):
                print("The benefits of movement help sooth a sad heart...\n"
                      "sadness level {}".format(int(self.sadness)))

        total = sum(anger + joy + sadness)
        total += 1

    def meditation(self, *day, **time):
        meditation = True

        if bool(meditation) == True:
            print("Congrats. Meditation helps keep a sharp mind.\n"
                  "You meditated for {}".format(time))
        else:
            print("Consistant meditation will help improve all aspects of life")

class Patience:
    pass

class Pure_heart:
    pass