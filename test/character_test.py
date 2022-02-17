from rpg_combat.character import Character


def test_character_starts_alive():
    character = Character()
    assert character.health == 1000
    assert character.level == 1
    assert character.alive

def test_character_can_damage_character():
    rogue = Character()
    barbarian = Character()
    barbarian.smack(rogue) 
    assert rogue.health < 1000