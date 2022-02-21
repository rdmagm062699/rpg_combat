from rpg_combat.character import Character

def test_initialization():
    character = Character()
    assert character.health == 1000
    assert character.level == 1
    assert character.alive

def test_character_can_damage_character():
    barbarian = Character()
    rogue = Character()
    rogue.smack(barbarian)
    assert barbarian.health < 1000
