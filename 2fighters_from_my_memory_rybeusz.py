class Fighter:
    def __init__ (self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage


def declare_winner(f1, f2, first_attacker):
    if (first_attacker == f1.name):
        attacker, defender = f1, f2
    else:
        attacker, defender = f2, f1
    while True:
        defender.health -= attacker.damage
        print (attacker.name + ' attacks. ' + defender.name + ' now has ' + \
               str(defender.health) + ' points.')
        if (defender.health <= 0):
            print(defender.name + ' is death. ' + attacker.name + ' wins.')
            return attacker.name
            break
        attacker, defender = defender, attacker


declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 10, 2), "Lew")
