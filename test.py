# test.py
from Entity.Hero import Warrior, Mage, Thief
from Entity.Enemy import Wolf, Skeleton, Bandit, Boss
from Battle.Fight import Fight
from Inventory.Item import start_equipment

# Créer le héros
hero = Warrior("Alyssa")

print("\n" + "="*50)
print("📊 STATS AVANT ÉQUIPEMENT")
print("="*50)
print(f"❤️  HP: {hero.pv}")
print(f"⚔️  Attack: {hero.attack}")
print(f"🛡️  Defense: {hero.defense}")
print(f"⚡ Agility: {hero.agility}")
print(f"💥 Critical Rate: {hero.critical_rate * 100}%")

start_equipment(hero)

print("\n" + "="*50)
print("📊 STATS APRÈS ÉQUIPEMENT")
print("="*50)
print(f"❤️  HP: {hero.pv}")
print(f"⚔️  Attack: {hero.attack} (+5 de l'Épée de Fer)")  
print(f"🛡️  Defense: {hero.defense}")
print(f"⚡ Agility: {hero.agility}")
print(f"💥 Critical Rate: {hero.critical_rate * 100}%")

print("\n" + "="*50)
print("🎒 INVENTAIRE")
print("="*50)
for item in hero.equipement:
    print(f"  • {item}")
    if hasattr(item, 'stat_bonus'):
        print(f"    Bonus: {item.stat_bonus}")

print("\n" + "="*50)
print("⚔️ COMBAT TEST")
print("="*50)

enemy = Wolf()
fight = Fight(hero, enemy)
fight.fight_enemy()
