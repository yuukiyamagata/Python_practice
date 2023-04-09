import random

hands = ['グー','チョキ','パー']
win,draw,lose = '勝ち','あいこ','負け'

rules = {
    (0,0): draw, (0,1):win, (0,2):lose,
    (1,0): lose, (1, 1): draw, (1, 2): win,
    (2, 0): win, (2, 1): lose, (2, 2): draw
}


while True:

  my_hand = int(input('0~2の数字を入力してください。\n0:グー, 1:チョキ, 2:パー \n>>>'))
  enemy_hand = random.randint(0, 2)

  my_hand_str = hands[my_hand]
  enemy_hand_str = hands[enemy_hand]

  result = rules[(my_hand, enemy_hand)]
  print(result)
  print('自分 :' + my_hand_str + ' 相手 :' + enemy_hand_str)

  if enemy_hand != my_hand:
    break

