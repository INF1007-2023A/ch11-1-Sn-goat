"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import utils
import random as rd


class Weapon:
	"""
	Une arme dans le jeu.

	:param name:      Le nom de l'arme
	:param power:     Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""

	UNARMED_POWER = 20
	
	# TODO: __init__
	def __init__(self, name: str, power: int, min_level:int):
		self.__name = name
		self.__power = power
		self.__min_level = min_level
	
	# TODO: Propriétés
	@property
	def name(self):
		return str(self.__name)

	@property
	def power(self):
		return int(self.__power)

	@property
	def min_level(self):
		return int(self.__min_level)

	# TODO: use
	def use(self, user, opponent) -> str:
		# TODO: Caculer et appliquer le dommage en utilisant la méthode compute_damage
		damage, crit = self.compute_damage(user, opponent)
		opponent.hp -= damage
		msg = ""
		if crit:
			msg += "Critical hit! "
		msg += f"{opponent.name} took {damage} dmg"
		return msg

	def is_usable_by(self, character) -> bool:
		return self.min_level <= character.level

	# TODO: compute_damage
	def compute_damage(self, characterA, characterB) -> tuple:
		dmg = utils.compute_damage_output(characterA.level, self.power, characterA.attack, characterB.defense, 1/16, (0.85, 1.00))
		return dmg

	# TODO: make_unarmed
	@classmethod
	def make_unarmed(cls):
		return Weapon("Unarmed", cls.UNARMED_POWER, 1)


class Character:
	"""
	Un personnage dans le jeu

	:param name:    Le nom du personnage
	:param max_hp:  HP maximum
	:param attack:  Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level:   Le niveau d'expérience du personnage
	"""
	
	# TODO: __init__
	def __init__(self, name: str, max_hp: int, attack: int, defense: int, level: int):
		self.__name = name
		self.__max_hp = max_hp
		self.__attack = attack
		self.__defense = defense
		self.__level = level
		self.__max_hp = max_hp
		self.__hp = max_hp
		self.__weapon = Weapon.make_unarmed()

	# TODO: Propriétés
	@property
	def name(self):
		return str(self.__name)
	
	@property
	def max_hp(self):
		return int(self.__max_hp)

	@property
	def attack(self):
		return int(self.__attack)

	@property
	def defense(self):
		return int(self.__defense)
	
	@property
	def level(self):
		return int(self.__level)
	
	@property
	def weapon(self):
		return self.__weapon

	@property
	def hp(self):
		return int(self.__hp)
	
	@weapon.setter
	def weapon(self, newWeapon):
		if newWeapon == None:
			self.__weapon = Weapon.make_unarmed()
		elif isinstance(newWeapon, Weapon):
			if newWeapon.is_usable_by(self):
				self.__weapon = newWeapon
			else:
				raise ValueError
		else:
			raise TypeError

	@hp.setter
	def hp(self, newHp):
		if newHp in list(range(0, self.max_hp + 1)):
			self.__hp = newHp
		elif newHp < 0:
			self.__hp = 0
		else:
			raise ValueError

	@max_hp.setter
	def max_hp(self, newHpMax):
		self.__max_hp = newHpMax
		self.hp = utils.clamp(self.hp, newHpMax, newHpMax)


	def apply_turn(self, opponent):
		msg = f"{self.name} used {self.weapon.name}\n"
		msg += self.weapon.use(self, opponent)
		return msg
