#Breaking out of while loops

import random

playerHp = 260
enemyAttackLow = 60
enemyAttackHigh = 80

while playerHp > 0:
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
        print("You have low health. You've  been teleported to nearest location")
        break
