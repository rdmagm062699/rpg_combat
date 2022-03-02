MAX_HEALTH = 1000


class Character(object):
    def __init__(self):
        self.health = MAX_HEALTH
        self.level = 1
        self.alive = True

    def smack(self, character):
        character.health = character.health - 10
        character.normalize_status()

    def heal(self, character):
        if not character.alive:
            return
        character.health = character.health + 10
        character.normalize_status()

    def normalize_status(self):
        if self.health <= 0:
            self.health = 0
            self.alive = False
        if self.health > MAX_HEALTH:
            self.health = MAX_HEALTH
