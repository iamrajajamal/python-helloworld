#Breaking out of while loops

import random


class Enemy:

    hp = 200

    def __init__(self, attack_low, attack_high):
        self.attack_low = attack_low
        self.attack_high = attack_high

    def get_attack(self):
        print(self.attack_low)

    def get_hp(self):
        print("Hp is", self.hp)


enemy1 = Enemy(40, 50)
enemy1.get_attack()
enemy1.get_hp()

enemy2 = Enemy(70, 90)
enemy2.get_attack()
enemy2.get_hp()

'''
class Enemy:

    def __init__(self, attack_low, attack_high):
        self.attack_low = attack_low
        self.attack_high = attack_high

    def get_attack(self):
        print(self.attack_low)


enemy1 = Enemy(40, 50)
enemy1.get_attack()

enemy2 = Enemy(70, 90)
enemy2.get_attack()

'''


'''Class Practice
class Enemy:
    attackLow = 60
    attackHigh = 80

    def get_Attack(self):
        print(self.attackLow)


enemy1 = Enemy()
enemy1.get_Attack()


enemy2 =Enemy()
enemy2.get_Attack()
'''


'''
playerHp = 260
enemyAttackLow = 60
enemyAttackHigh = 80

#Use Continue in while loop

while playerHp > 0:
    dmg = random.randrange(enemyAttackLow, enemyAttackHigh)
    playerHp = playerHp - dmg

    if playerHp <= 30:
        playerHp = 30

    print("Enemy Strikes for", dmg, "points of damage. Current hp is", playerHp)

    if playerHp > 30:
        continue

    print("You have low health. You've been teleported to nearest location")
    break
'''

#breaking from the while loop

'''while playerHp > 0:
    dmg = random.randrange(enemyAttackLow, enemyAttackHigh)
    playerHp = playerHp - dmg

    if playerHp <= 0:
        playerHp = 0

    print("Enemy Strikes for", dmg, "points of damage. Current hp is", playerHp)

    if playerHp == 0:
        print("You have died.")


#stop while loop by break keyword

while playerHp > 0:
    dmg = random.randrange(enemyAttackLow, enemyAttackHigh)
    playerHp = playerHp - dmg

    if playerHp <= 30:
        playerHp = 30

    print("Enemy Strikes for", dmg, "points of damage. Current hp is", playerHp)

    if playerHp == 30:
        print("You have low health. You've been teleported to nearest location")
        break  '''
