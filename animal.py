class Animal:

    def __init__(self, kind, age):
        self.kind = kind
        self.age = str(age) + '歳'

    def cry(self):
        print('私は' + self.kind + 'です')


class Dog(Animal):
    pass

class Cat(Animal):

    def __init__(self, kind, age, color):
        super().__init__(kind, age) # 親クラスのコンストラクタ
        self.color = color

    def cry(self):
        print('にゃーん' + self.kind + 'だにゃん。' + '色は'   + self.color + 'だにゃん')

pochi = Dog('犬', 8)
pochi.cry()

tama = Cat('三毛猫', 3, '黒')
tama.cry()