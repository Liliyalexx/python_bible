import random


health = 50

difficulty = 3


potion_health = int(random.randint(25, 50)/difficulty)
health += potion_health
print (health)

