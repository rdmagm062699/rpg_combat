class Character(object):
    def __init__(self):
        self.health = 1000
        self.level = 1
        self.alive = True

    def smack(self, character):
        character.health = character.health - 10
