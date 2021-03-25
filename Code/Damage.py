#SCENARIO: YOU ARE FIGHTING A LEVEL 87 HILICHURL
#MY FULLY BUILT LEVEL 90 C0 MONA WITH
#A LEVEL 90 EYE OF PERCEPTION

#MONA ATTACK
charATK = 287
weaponATK = 454
weaponBonus = 1 + (55.1/100)
baseATK = charATK + weaponATK

#ARTIFACTS
artiATK = 1706
attack = baseATK + artiATK

#BONUSES
abilityPercent = 60.2/100 #first auto attack
bonusDMG = 88/100



#ENEMY HILICHURL DEFENSE
monaLVL = 90
hiliLVL = 87
hiliRES = 1 - 0.1

mulDEF = (monaLVL + 100) / (monaLVL + hiliLVL + 200)

outDMG = attack * abilityPercent * (1 + bonusDMG)
inDMG = outDMG * mulDEF * hiliRES
crit = inDMG * (1 + 99.7/100)

#APPROX DAMAGE DEALT TO THE HILICHURL
print(inDMG)
print(crit)
