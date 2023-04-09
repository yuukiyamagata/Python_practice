# hands = ['rock', 'scissor', 'paper']
# hands = {"0": "グー","1": "チョキ","2": "パー"}
# gu,choki,pa = "グー","チョキ","パー"  タプル型の分割代入
# win,draw,lose = "勝ち","あいこ","負け"
# my_hand = choki
# enemy_hand = choki

# if(my_hand == enemy_hand):
#     print(draw)
# elif (my_hand == gu and enemy_hand == choki) or \
#   (my_hand == pa and enemy_hand == gu) or \
#     (my_hand == choki and enemy_hand == pa):
#       print(win)
# else:
#     print(lose)

win,draw,lose = "勝ち","あいこ","まけ"

rules = {
    (0,0): draw, (0,1):win, (0,2):lose,
    (1,0): lose, (1,1):draw, (1, 2): win,
    (2,0): win, (2,1):lose, (2,2): draw
}
# rulesは辞書のキーにタプルを指定している
# 左側が自分の手、右側が相手の手とした時の勝敗表

my_hand = 0
enemy_hand = 2
result = rules[my_hand, enemy_hand]
print(result)