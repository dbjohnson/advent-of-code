from Queue import PriorityQueue


spells = [{'name': 'Magic Missile', 'cost': 53, 'damage': 4, 'timer': 1},
          {'name': 'Drain', 'cost': 73, 'damage': 2, 'healing': 2, 'timer': 1},
          {'name': 'Shield', 'cost': 113, 'armor': 7, 'timer': 6},
          {'name': 'Poison', 'cost': 173, 'damage': 3, 'timer': 6},
          {'name': 'Recharge', 'cost': 229, 'mana': 101, 'timer': 5}]

player = {'hitpoints': 50, 'mana': 500}
boss = {'hitpoints': 51, 'damage': 9}


class Round(object):
    def __init__(self, boss, player, spell, active_spells=[], count=1, spell_cost_so_far=0, round_cost=0, history=[]):
        self.boss = boss.copy()
        self.player = player.copy()
        self.active_spells = [s.copy() for s in active_spells]
        self.total_spent = spell_cost_so_far
        self.count = count
        self.history = history[:]
        self.player_turn(round_cost, spell)
        self.boss_turn()

    @classmethod
    def from_round(cls, rnd, spell, round_cost=0):
        return cls(rnd.boss, rnd.player, spell, rnd.active_spells, rnd.count + 1,
                   rnd.total_spent, round_cost, rnd.history + [rnd])

    def player_turn(self, round_cost, spell):
        self.player['hitpoints'] -= round_cost
        if self.player_is_dead():
            return

        if spell['cost'] <= self.player['mana']:
            self.active_spells.append(spell.copy())
            self.player['mana'] -= spell['cost']
            self.total_spent += spell['cost']
        else:
            raise RuntimeError("Can't afford spell")

        spell_armor, spell_damage = self.apply_spells()
        self.boss['hitpoints'] -= spell_damage

    def boss_turn(self):
        if not self.player_is_dead() and not self.boss_is_dead():
            spell_armor, spell_damage = self.apply_spells()
            self.boss['hitpoints'] -= spell_damage
            if not self.boss_is_dead():
                self.player['hitpoints'] -= max(1, boss['damage'] - spell_armor)

    def apply_spells(self):
        spells_to_delete = []
        spell_damage = spell_armor = 0
        for spell in self.active_spells:
            self.player['mana'] += spell.get('mana', 0)
            self.player['hitpoints'] += spell.get('healing', 0)
            spell_damage += spell.get('damage', 0)
            spell_armor += spell.get('armor', 0)
            spell['timer'] -= 1
            if spell['timer'] == 0:
                spells_to_delete.append(spell)

        for spell in spells_to_delete:
            self.active_spells.remove(spell)

        return spell_armor, spell_damage

    def boss_is_dead(self):
        return self.boss['hitpoints'] <= 0

    def player_is_dead(self):
        return self.player['hitpoints'] <= 0

    def replay(self):
        print '\n'.join(map(str, self.history + [self]))

    def __repr__(self):
        return 'round: {}, boss: {}, player: {}, spells:{}, spent: {}'.format(
            self.count, self.boss, self.player, self.active_spells, self.total_spent)

    def __cmp__(self, other):
        return self.total_spent - other.total_spent


def find_cheapest_fight(round_cost=0):
    q = PriorityQueue()
    for spell in spells:
        q.put(Round(boss, player, spell, round_cost=round_cost))

    best_fight = None
    while not q.empty():
        rnd = q.get()
        if rnd.boss_is_dead():
            if not best_fight or rnd.total_spent < best_fight.total_spent:
                best_fight = rnd
            else:
                break
        elif not rnd.player_is_dead():
            for spell in spells:
                if spell['name'] not in (s['name'] for s in rnd.active_spells):
                    if spell['cost'] <= rnd.player['mana']:
                        q.put(Round.from_round(rnd, spell, round_cost))

    return best_fight.total_spent


print 'part 1:', find_cheapest_fight()
print 'part 2:', find_cheapest_fight(round_cost=1)
