from game import *
from character import *


def main():
	c1 = Character("Äpik", 1000, 720, 250, 70)
	c2 = Character("Gämmör", 1000, 800, 800, 70)

	c1.weapon = Weapon("BFG", 120, 50)
	c2.weapon = Weapon("BBC", 69, 69)

	turns = run_battle(c1, c2)
	print(f"The battle ended in {turns} turns.")

if __name__ == "__main__":
	main()
