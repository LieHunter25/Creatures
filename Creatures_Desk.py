import os
from random import randint, sample
import logging
from mongoengine import *
from filler_creatures import creatures, abilities

logging.basicConfig(level=logging.DEBUG)

# Ojalá my internet fuera así

class Ability(Document):
    name = StringField(required=True, unique=True)
    effect_stat = IntField()
    effect_status = StringField()

    description = StringField()

    meta = {'strict': False}

class Creature(Document):
    name = StringField(required=True, unique=True)
    image = StringField()


    hp = IntField(default=50, required=True)
    attack = IntField(required=True)
    defense = IntField(required=True)
    speed = IntField(required=True)
    ability = ReferenceField(Ability)
    description = StringField()
    lore = StringField()

    meta = {'strict': False}

    def repr(self):
        ability_name = self.ability.name if self.ability else "NO ability yet"
        return f"<Creature {self.name} - Atk {self.attack}: {ability_name}>"

if os.getenv("USE_LOCAL"):
    connect("Creatures")
    logging.debug("Running on local database.")
else:
    connect(host=os.getenv("CREATURE_DEN_DATABASE_URL"))
    logging.debug("Running on the cloud.")


Creature.drop_collection()
Ability.drop_collection()

#Your code goes here
#c = Creature(name="", image="", hp=, attack=, defense=, speed=, ability=a, description="", lore="")

a = Ability(name="sharp claws", effect_stat=15, description="The sharpnest of his claws makes his atract dedlier")
c = Creature(name="Aquina", image="2", hp=45, attack=60, defense=40, speed=80, description="Blue fear mamule with claws that can cut easyly his pray.", lore="...")

a.save()
c.ability = a
c.save()

a = Ability(name="Heavy Attack", effect_status="confuse", description="fisical attacks can couse confusion")
c = Creature(name="Paraserus", image="5", hp=60, attack=50, defense=30, speed=70, description="Creature with a big and strong head, his attacks can stun his enemys", lore="...")

a.save()
c.ability = a
c.save()

a = Ability(name="Electric bite", effect_status="paralice", description="fisical attacks has a chace tu paralice")
c = Creature(name="Calios", image="12", hp=40, attack=75, defense=45, speed=60, description="A predator that paralice his enemys with his bites", lore="...")

a.save()
c.ability = a
c.save()

a = Ability(name="small body", effect_stat=10, description="With a small body the creature is more agile")
c = Creature(name="Wolfrey", image="14", hp=45, attack=70, defense=45, speed=55, description="A wolf like creature of smale size", lore="")

a.save()
c.ability = a
c.save()

a = Ability(name="Levitad", effect_status="float", description="ground attacks dos not affect the creature")
c = Creature(name="Nyami", image="330", hp=30, attack=85, defense=30, speed=90, description="Tiny magical cat with destructive magical attacks and incredibel speed", lore="...")

a.save()
c.ability = a
c.save()

# Generating filler creatures

# find already used images
pics_already_used = Creature.objects().distinct("image")

all_pics = [str(n) for n in range(1, 829)]

unused_pics = list(set(all_pics).difference(pics_already_used))

for each_filler_creature, each_ability in zip(creatures, abilities):
    creature_name = each_filler_creature
    abilities_name = each_ability

    creature_description = creatures[creature_name]["description"]
    creature_lore = creatures[creature_name]["lore"]
    ability_description = abilities[abilities_name]

    hp = randint(1,100)
    attack = randint(1,100)
    defense = randint(1,100)
    speed = randint(1,100)
    image = sample(unused_pics, 1)[0]

    c = Creature(name=creature_name, description=creature_description, hp=hp, attack=attack, defense=defense, speed=speed, lore=creature_lore, image=image)

    a = Ability(name=abilities_name, description=ability_description)

    a.save()
    c.ability = a
    c.save()
    pass

pass