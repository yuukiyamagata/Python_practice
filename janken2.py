import random

hands = ["グー","チョキ","パー"]

# i = random.randint(0, 2)
# hand = hands[i]
# print(hand)

i = int(input("0~2の数字を入力してください>>>>"))
# input inputに代入された引数がコマンドラインで表示されて、ユーザーからの入力を待つ
hand = hands[i]
print(hand)