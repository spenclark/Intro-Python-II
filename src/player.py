# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    """"
        This call is used to build a player type. A player can have many skills assigned to thier object -- and also have many items in their inventory.
    """

    def __init__(self, name, age, level, nationality, skills, inventory, location):
        self.name = name
        self.age = age
        self.level = level
        self.nationality = nationality
        self.skills = skills
        self.inventory = inventory
        self.location = location

    def add_skill(self, new_skill):
        self.skills.append(new_skill)

    def equip_item(self, new_item):
        self.inventory.append(new_item)

    def open_inv(self):
        if len(self.inventory) > 0:
            for i in self.inventory:
                print(f"{i.name}")
        else:
            print("Empty")

    def get_location(self):
        return self.location

    def set_location(self, new_locaiton):
        self.location = new_locaiton

    def __str__(self):
        s = f"name: {self.name}, age: {self.age}, level: {self.level}, nation: {self.nationality}. skills: {self.skills}, inv: {self.inventory} They are in {self.location}."
        return s


class Skills:
    """
    This is class is used to build a Skill object - skills can be given to players. Value is the strength of the skill. e.g. {name: "Sleeping", value:"2", effect: "This player is uncanny at napping"}
    """

    def __init__(self, name, value, effect):
        self.name = name
        self.value = value
        self.effect = effect

    def __str__(self):
        s = f"{self.name} - {self.value} - {self.effect}"
        return s


class Item:
    """
        This class is for items. A player can have many items
    """

    def __init__(self, name, about):
        self.name = name
        self.about = about

    def __str__(self):
        s = f"{self.name}. {self.about}"
        return s
