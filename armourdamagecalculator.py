import csv
class Armour:
    def __init__(self, name, armourpoints, toughness):
        self.name = name
        self.armourpoints = armourpoints
        self.toughness = toughness

    def __eq__(self, other):
        return other.split()[0].lower() in self.name and other.split()[1].lower() in self.name


    def __add__(self, other):
        return Armour(f'{self.name} and {other.name}', self.armourpoints + other.armourpoints, self.toughness + other.toughness)

    def __repr__(self):
        return self.name

    def calc_damage(self, damage):
        first_layer = max(self.armourpoints/5, self.armourpoints - (4*damage)/(self.toughness+8))
        second_layer = min(20, first_layer)
        return damage*(1 - second_layer/25)

    def reduction_pct(self, damage):
        return (damage - self.calc_damage(damage))*100/damage

nothing = Armour('no armour', 0, 0)
helmets = []
chestplates = []
leggings = []
boots = []
with open('armourpieceslibrary.csv') as library_file:
    reader = csv.DictReader(library_file)
    for row in reader:
        new_obj = Armour(row['name'], int(row['defense']), int(row['toughness']))
        if row['type'] == 'helmet':
            helmets.append(new_obj)
        elif row['type'] == 'chestplate':
            chestplates.append(new_obj)
        elif row['type'] == 'leggings':
            leggings.append(new_obj)
        elif row['type'] == 'boots':
            boots.append(new_obj)

print("Welcome to the minecraft damage calculator. First, input the amount of damage dealt by the weapon. 1 damage point is half a heart.")
damage = float(input("Input the amount of base damage dealt, e.g. diamond axe deals 9 damage: "))
crit = input("Is it a critical hit? Y/N: ")
if crit.upper() == "Y":
    damage *= 1.5
else:
    pass
print("In the order helmet, chestplate, leggings, boots, ")
armour_pieces = input("input a list of your armour pieces, separated by commas. For elytra or nothing put 'None'. ")
armour_list = [piece.strip() for piece in armour_pieces.split(",")]
equipped_helmet = nothing
for helmet in helmets:
    if armour_list[0] == helmet:
        equipped_helmet = helmet

equipped_chestplate = nothing
for chestplate in chestplates:
    if armour_list[1] == chestplate:
        equipped_chestplate = chestplate
equipped_leggings = nothing
for legging in leggings:
    if armour_list[2] == legging:
        equipped_leggings = legging
equipped_boots = nothing
for boot in boots:
    if armour_list[3] == boot:
        equipped_boots = boot
armour_set = equipped_helmet + equipped_chestplate + equipped_leggings + equipped_boots
print(f'The equipped set is {armour_set} with {armour_set.armourpoints} defense and {armour_set.toughness} toughness.')
print(f"The damage dealt is {round(armour_set.calc_damage(damage), 2)}, and the damage reduction is {round(armour_set.reduction_pct(damage), 2)}%.")

bruh = input('Press ENTER to continue')