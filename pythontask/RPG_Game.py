import random as r # 몬스터 공격

# Object 클래스
class Object:
    # status = 1
    def __init__(self,name,hp, attack_damage):
        self.name = name
        self.hp = hp
        self.attack_damage = attack_damage
        self.status = 1

    # 공통적인 특성인 이름, hp, 공격력
    def info(self):
        print('이름 =>', self.name,
              ', 체력 =>', self.hp,
              ', 공격력 =>', self.attack_damage)

    # 공통적인 메서드인 공격
    def attack(self, target):
        target.hp -= self.attack_damage
        print(self.name, "이/가", target.name, '을/를 공격했고',
              target.name, "의 체력은", target.hp, "만큼 남았습니다.")
        if target.hp <= 0:
            print(f'{target.name}은 죽었습니다!')
            target.status = 0
            return target.status


#------------------------------------------------------------------------

# Player 클래스
class Player(Object):
    def magic(self,target):
        target.hp -= 50
        print(self.name, "이/가", target.name, '을/를 공격했고',
        target.name, "의 체력은", target.hp, "만큼 남았습니다.")

        if target.hp <= 0:
            print(f'{target.name}은 죽었습니다!')
            Monsters.remove(target)


#------------------------------------------------------------------------

# Monster 클래스
class Monster(Object):
    def wait(self):
        print(self.name,"이/가 대기했습니다.")

    def heal(self):
        print(self.name,"이/가", "10만큼 회복했습니다.")
        self.hp += 10
#------------------------------------------------------------------------
#함수

# 체력 값 표현 함수
def hp_info(name):
    if name.status == 1:
        print(f'{name.name}: {name.hp}')



# 플레이어 순서 함수
def player_turn(Monsters):
    attack = input("공격 과 마법 중 무얼 하시겠습니까? ")
    for i, name in enumerate(Monsters):
        print(f'{i}. {name.name}')
    target = int(input("누구를 공격하시겠습니까? 번호로 말해주세요:"))

    if attack == "공격" :
       p1.attack(Monsters[target]) # 미니고블린으로 입력받을 수는 없나?
    elif attack == "마법":
        p1.magic(Monsters[target])

# 몬스터 순서 함수
def monster_turn(monster):
    t = r.randrange(0,3)
    if t == 0:
        monster.attack(p1) # 전사를 공격
    elif t == 1:
        monster.heal()
    else:
        monster.wait()

# 플레이어가 죽었을 때
def player_death(player):
    if player.hp <= 0:
        print('몬스터 승리!')
        status = 0
        return status

# 몬스터가 죽었을 때
def monster_death(Monsters):
    if len(Monsters) ==0:
        status = 0
        print('몬스터를 다 쓰러뜨렸다!')
        print('플레이어 승리!')
        return status

p1 = Player("전사", 100, 10) # p1 = Player("전사", 100, 10)

mini = Monster('미니고블린', 10, 10)
goblin = Monster('고블린', 30, 30)
super = Monster('슈퍼고블린', 50, 50)
Monsters = [mini, goblin, super]

while True:
    print("-----hp info-----")
    hp_info(p1)
    print("----- -----")
    for m in Monsters:
        hp_info(m)
    print("-----플레이어 턴-----")
    player_turn(Monsters)
    if monster_death(Monsters) == 0:
        break
    print("-----몬스터 턴-----")
    for m in Monsters:
        monster_turn(m)
    if player_death(p1) == 0:
        break
