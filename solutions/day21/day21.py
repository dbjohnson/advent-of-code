import itertools

weapons = [{'Name': 'Dagger', 'Cost': 8, 'Damage': 4, 'Armor': 0},
           {'Name': 'Shortsword', 'Cost': 10, 'Damage': 5, 'Armor': 0},
           {'Name': 'Warhammer', 'Cost': 25, 'Damage': 6, 'Armor': 0},
           {'Name': 'Longsword', 'Cost': 40, 'Damage': 7, 'Armor': 0},
           {'Name': 'Greataxe', 'Cost': 74, 'Damage': 8, 'Armor': 0}]

armor = [{'Name': 'Leather', 'Cost': 13, 'Damage': 0, 'Armor': 1},
         {'Name': 'Chainmail', 'Cost': 31, 'Damage': 0, 'Armor': 2},
         {'Name': 'Splintmail', 'Cost': 53, 'Damage': 0, 'Armor': 3},
         {'Name': 'Bandedmail', 'Cost': 75, 'Damage': 0, 'Armor': 4},
         {'Name': 'Platemail', 'Cost': 102, 'Damage': 0, 'Armor': 5},
         {'Name': 'None', 'Cost': 0, 'Damage': 0, 'Armor': 0}]

rings = [{'Name': 'Damage +1', 'Cost': 25, 'Damage': 1, 'Armor': 0},
         {'Name': 'Damage +2', 'Cost': 50, 'Damage': 2, 'Armor': 0},
         {'Name': 'Damage +3', 'Cost': 100, 'Damage': 3, 'Armor': 0},
         {'Name': 'Defense +1', 'Cost': 20, 'Damage': 0, 'Armor': 1},
         {'Name': 'Defense +2', 'Cost': 40, 'Damage': 0, 'Armor': 2},
         {'Name': 'Defense +3', 'Cost': 80, 'Damage': 0, 'Armor': 3},
         {'Name': 'None', 'Cost': 0, 'Damage': 0, 'Armor': 0}]


class Fighter(object):
    def __init__(self, hitpoints=100, damage=0, armor=0, equipment=[]):
        self.hitpoints = hitpoints
        self.damage = damage
        self.armor = armor
        self.equipment_cost = 0
        for e in equipment:
            self.outfit(e)

    def outfit(self, item):
        self.damage += item['Damage']
        self.armor += item['Armor']
        self.equipment_cost += item['Cost']

    def deal_blow(self, other):
        other.hitpoints -= max(1, self.damage - other.armor)
        return other.hitpoints <= 0


losing_outfit_costs = []
winning_outfit_costs = []
for w in weapons:
    for a in armor:
        for nr in (1, 2):
            for rrs in itertools.combinations(rings, nr):
                fighter = Fighter(equipment=(w, a) + rrs)
                boss = Fighter(100, 8, 2)
                while True:
                    if fighter.deal_blow(boss):
                        winning_outfit_costs.append(fighter.equipment_cost)
                        break
                    if boss.deal_blow(fighter):
                        losing_outfit_costs.append(fighter.equipment_cost)
                        break


print 'part 1:', min(winning_outfit_costs)
print 'part 2:', max(losing_outfit_costs)
