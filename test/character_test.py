from rpg_combat.character import Character

def test_initialization():
    character = Character()
    assert character.health == 1000
    assert character.level == 1
    assert character.alive
