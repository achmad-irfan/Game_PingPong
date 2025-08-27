class Hero:
    def __init__(self,name,hp,attack,skill):
        self.name=name
        self.hp=hp
        self.attack=attack
        self.skill=skill
    
    def __add__(self,other):
        
        new_name=self.name+"&"+other.name
        new_hp= self.hp+other.hp
        new_attack= self.attack+other.attack
        new_skill=self.skill+other.skill
        new_skill=list(set(new_skill))
        return Hero(new_name,new_hp,new_attack,new_skill)
    
    def __str__(self):
        return f"Hero {self.name} dengan HP: {self.hp}  punya skill {self.skill}"
    
    def __len__(self):
        return len(self.skill)
    
    def atk(self, enemies):
        enemies.hp -=  self.attack
        print(f"{self.name} menyerang {enemies.name}")
        print(f"Hp {enemies.name} tinggal {enemies.hp}")
    def islive(self):
        return True if self.hp >0 else False
    
kadita= Hero("kadita",88,12,["kick","punch"])
harley= Hero("harley",80,22,["shot","kick"])
vale= Hero("valey",477,3,["heal","splash"])
kimmy= Hero("kimmy",99,28,["kick","heal"])
enemy= Hero("enemy",44,20,["kick"])


while kimmy.islive() and vale.islive():
    kimmy.atk(vale)
    if vale.islive()==False:
        print(f"{vale.name} tewas dibantai ")
        break

    vale.atk(kimmy)
    if kimmy.islive()==False:
        print(f"{kimmy.name} tewas")
        

def battle(p1,p2):
    while p1.islive() and p2.islive():
        p1.atk(p2)
        if p2.islive()==False:
            print(f"{p2.name} tewas dibantai")
            break

        p2.atk(p1)
        if p1.islive()==False:
            print(f"{p1.name} tewas dibantai") 
            break
        
battle(kadita,vale)

