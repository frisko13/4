class Player:
    def __init__(self, name, hp = 20, damage = 5, armor = 3):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.armor = armor
        self.weapon = None
    __str__ = lambda self: f'Имя игрока: {self.name}\nHP: {self.hp}\nБроня: {self.armor}\nСила: {self.damage}'

    get_damage = lambda self: f'Имя игрока: {self.name}\nHP: {self.hp - (self.damage - self.armor) }\nБроня: {self.armor}\nСила: {self.damage}'

    heal = lambda self: f'Имя игрока: {self.name}\nHP: {self.hp + 5}\nБроня: {self.armor}\nСила: {self.damage}'
    

    
p1 = Player('реальный поцан')
print(p1)
print('--------------------------------')
print(p1.get_damage())
print('--------------------------------')
print(p1.heal())