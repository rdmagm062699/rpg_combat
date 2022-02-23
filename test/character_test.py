from rpg_combat.character import Character


def test_initialization():
    barbarian = Character()
    assert barbarian.health == 1000
    assert barbarian.level == 1
    assert barbarian.alive


def test_character_can_damage_character():
    barbarian = Character()
    rogue = Character()
    rogue.smack(barbarian)
    assert barbarian.health < 1000


def test_character_can_kill():
    barbarian = Character()
    rogue = Character()
    for n in range(0, 100):
        barbarian.smack(rogue)
    assert not rogue.alive


def test_character_can_heal():
    barbarian = Character()
    barbarian.smack(barbarian)
    old_health = barbarian.health
    barbarian.heal(barbarian)
    assert barbarian.health > old_health


def test_dead_cant_be_healed():
    zombie = Character()
    initial_health = zombie.health
    zombie.alive = False
    zombie.heal(zombie)
    assert zombie.health == initial_health


def test_dead_cant_be_raised_via_heal():
    zombie = Character()
    zombie.alive = False
    zombie.heal(zombie)
    assert not zombie.alive
