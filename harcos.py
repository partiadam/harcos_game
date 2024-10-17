"""Feladat: Harcos játék

Készíts egy Python programot, amely egy harcos küzdelmet szimulál. A program követelményei a következők:



1. Harcos osztály
Hozz létre egy Warrior nevű osztályt, amely tartalmazza a harcos tulajdonságait és metódusait:
__init__(self, name, health, attack_power): Inicializálja a harcos nevét, életerejét és támadási erejét.
attack(self, other_warrior): Ez a metódus csökkenti az ellenfél életerejét a támadási erővel.
is_alive(self): Ez a metódus visszatér True értékkel, ha a harcos életereje nagyobb mint 0, és False-al, ha nem.

Védekezés mechanika: A harcosok védekezhetnek is, ami csökkenti a támadások által okozott sebzést.

Random sebzés: A támadások ne legyenek mindig fix erejűek, hanem véletlenszerűen változhassanak egy adott tartományon belül.

Speciális képesség: Minden harcosnak legyen egy speciális képessége, amit véletlenszerűen aktiválhatnak a csatában (pl. kritikus sebzés vagy extra védelem).

Körök számlálása: Legyen nyomon követve, hány kör után győz valaki.

2. Játékmenet

Hozz létre két harcost, akik felváltva támadják egymást, míg egyikük életereje el nem éri a nullát.
Minden körben jelenítsd meg, hogy melyik harcos támad, és mennyi életereje van az ellenfelének a támadás után.
Ha egy harcos életereje eléri a nullát, a játék véget ér, és a másik harcos nyer.


3. Hibakezelés
Használj try-except blokkokat arra az esetre, ha valamilyen váratlan hiba lépne fel a harcosok tulajdonságainak beállítása vagy a támadások során.
"""

import random


korok = 0

class Warrior:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        
    def attack(self, other_warrior):
        health = self.health - self.attack_power
        
        
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
        

hos1 = Warrior("peti", 100, 10)
hos2 = Warrior("robi", 100, 10)


melyik_kezdjen = int(input("Melyik harcos kezdjen? (1. vagy 2.)?: "))

while True:
    korok += 1
    print(f"Körök száma: {korok}")
    
    if hos1.health == 0:
        break
    
    
    
    
    
    
    
    
