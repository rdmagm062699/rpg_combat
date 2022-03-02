# RPG Combat Kata in Python

## Setup

Note: this assumes you have a recent-ish version of Python 3 setup locally.

1. [Fork this repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo).
1. Clone your forked repo to your local machine
2. (Optional) Checkout a task branch if you want to leave your `main` in pristine condition for easy resets: `git checkout -b day1`
3. Setup your virtualenv: `python -m venv .venv/rpg_combat`
4. Activate your virtualenv: `source .venv/rpg_combat/bin/activate`
5. Install your dependencies: `pip install -r build_requirements.txt`

You should now be ready to code!

- To run all tests: `pytest`
- To run all tests in watch mode: `ptw`
- To run a specific module of tests: `pytest test/test_character.py`
- To run a specific test: `pytest test/test_character.py::test_smack` or `pytest test/test_character.py::TestCharacter::test_smack`

## The Kata

Source: [https://github.com/ardalis/kata-catalog](https://github.com/ardalis/kata-catalog)

### Background

This is a fun kata that has the programmer building simple combat rules, as for a role-playing game (RPG). It is implemented as a sequence of iterations. The domain doesn't include a map or any other character skills apart from their ability to damage and heal one another.

### Instructions

1. Complete each iteration before reading the next one.
1. It's recommended you perform this kata with a pairing partner and while writing tests.

#### Iteration One

1. All Characters, when created, have:
   - Health, starting at 1000
   - Level, starting at 1
   - May be Alive or Dead, starting Alive (Alive may be a true/false)
1. Characters can Deal Damage to Characters.
   - Damage is subtracted from Health
   - When damage received exceeds current Health, Health becomes 0 and the character dies
1. A Character can Heal a Character.
   - Dead characters cannot be healed
   - Healing cannot raise health above 1000

#### Iteration Two

1. A Character cannot Deal Damage to itself.
1. A Character can only Heal itself.
1. When dealing damage:
   - If the target is 5 or more Levels above the attacker, Damage is reduced by 50%
   - If the target is 5 or more Levels below the attacker, Damage is increased by 50%

#### Iteration Three

1. Characters have an attack Max Range.
1. _Melee_ fighters have a range of 2 meters.
1. _Ranged_ fighters have a range of 20 meters.
1. Characters must be in range to deal damage to a target.

#### Retrospective

- Are you keeping up with the requirements? Has any iteration been a big challenge?
- Do you feel good about your design? Is it scalable and easily adapted to new requirements?
- Is everything tested? Are you confident in your code?

#### Iteration Four

1. Characters may belong to one or more Factions.
   - Newly created Characters belong to no Faction.
1. A Character may Join or Leave one or more Factions.
1. Players belonging to the same Faction are considered Allies.
1. Allies cannot Deal Damage to one another.
1. Allies can Heal one another.

#### Iteration Five

1. Characters can damage non-character _things_ (props).
   - Anything that has Health may be a target
   - These things cannot be Healed and they do not Deal Damage
   - These things do not belong to Factions; they are neutral
   - When reduced to 0 Health, things are _Destroyed_
   - As an example, you may create a Tree with 2000 Health

#### Retrospective

- What problems did you encounter?
- What have you learned? Any new technique or pattern?
- Share your design with others, and get feedback on different approaches.

### Resources

- Original Source: http://www.slideshare.net/DanielOjedaLoisel/rpg-combat-kata
