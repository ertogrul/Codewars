# Two fighters, one winner
# create Fighter object
class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack


def declare_winner (fighter1, fighter2, first_attack):
    print (fighter1.name)
    print ('health: ' + str(fighter1.health))
    print ('damage: ' + str(fighter1.damage_per_attack))
    print (fighter2.name)
    print ('health: ' + str(fighter2.health))
    print ('damage: ' + str(fighter2.damage_per_attack))
# zmiana - petla ma uwzgledniac remis
    while (fighter1.health > 0 and fighter2.health > 0):
        if (first_attack == fighter1.name):
            fighter2.health = fighter2.health - fighter1.damage_per_attack
            print (fighter1.name + ' attacks. ' + fighter2.name + ' now has '+ \
            str(fighter2.health) + ' points.')

            fighter1.health = fighter1.health - fighter2.damage_per_attack
            print (fighter2.name + ' attacks. ' + fighter1.name + ' now has '+ \
            str(fighter1.health) + ' points.')
        else:
            fighter1.health = fighter1.health - fighter2.damage_per_attack
            print (fighter2.name + ' attacks. ' + fighter1.name + ' now has '+ \
            str(fighter1.health) + ' points.')

            fighter2.health = fighter2.health - fighter1.damage_per_attack
            print (fighter1.name + ' attacks. ' + fighter2.name + ' now has '+ \
            str(fighter2.health) + ' points.')

    if (fighter1.health <= 0 and fighter2.health <= 0):
        print ("draw")
        return fighter1.name, fighter2.name
    elif(fighter2.health <= 0):
        print (fighter1.name + ' wins.')
        return fighter1.name
    elif(fighter1.health <= 0):
        print (fighter2.name + ' wins.')
        return fighter2.name
    else:
        print ("mistake")


declare_winner(Fighter("Lew", 20, 2), Fighter("Harry", 10, 3), "Lew")
