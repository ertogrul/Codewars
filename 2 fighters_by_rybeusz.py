class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack


def declare_winner(fighter1, fighter2, first_attacker):
    if fighter1.name == first_attacker:
        attacker, defender = fighter1, fighter2
    else:
        attacker, defender = fighter2, fighter1
    while True:
        defender.health -= attacker.damage_per_attack
        print (attacker.name + ' attacks. ' + defender.name + ' now has '+ \
        str(defender.health) + ' points.')
        if defender.health <= 0:
            print (defender.name + ' is death. '+attacker.name+' wins.')
            return attacker.name
        else:
            attacker, defender = defender, attacker


declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 10, 2), "Lew")
