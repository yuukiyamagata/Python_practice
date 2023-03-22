# データ型
基本的なPythonのデータ型は以下の4つ。type()で値の型を調べることができる
1. int型(整数型)...整数を表す英単語「integer」の略(例: 「1」, 「-5」)
2. float型(浮動小数点型)...「浮くもの」を意味する英単語「float」(例: 「0.01」)。小数のこと
   int型とfloat型を合わせて「数値型」という
3. str型(文字列型)...「ひも」「糸」「列」を意味する「string」の略
   「文字列」を表す(例: 「'Hi!'」「"こんにちは!"」)
4. bool型(ブール型)...「真偽」を表す「boolean」の略(「True」と「False」)

# print...「印刷する」と言う意味の英単語
print(値)で「値」を出力することができる
・()の中を「,」で区切ることで複数の値を出力することができる
  例: print('こんにちは', '太郎さん')
・()の中で演算を行うこともできる
  例; print(1 + 2)

# 数値型
1. int型(整数)とfloat型(浮動小数点数)の2つがある
2. 主に以下の演算を行うことが可能
   + 加算
   - 減算
   * 乗算
   ** 冪乗
   / 徐算
   // 徐算(小数点切り捨て)
   % 剰余算

計算の中にint型とfloat型が混在していると結果はfloat型で返却される
intにfloat型を入れると小数点は切り捨てられる

# 文字列型
* シングルクォーテーション('')かダブルクォーテーション("")で囲む
* 「\n」「"""」を使うことで改行が可能
  例: print('こんいちは, \n太郎さん')
* 数値型と同じように「+」と「*」で文字列の連結や繰り返しが可能(同じ文字列を繰り返した新しい文字列を作成することが可能)
  例: print('こんにちは' + '太郎さん')
* '数値'またはstr(数値)で数値型をstr型に変換できる
  例: print("2"), print(str(2))

文字列[x:y]...Slice。文字列のindex番号xからyまで(yは含まない)を新しい文字列にして返す



# リスト(mutable)



# タプル (imutable)
複数の値を「(値1, 値2,)」のように複数の値を一つの入れものにまとめて入れておく時に使う
インデックス(整数)を指定することで値を取得することができる
タプルの中にタプルを入れることも可能
リストと異なり、追加、削除、書き換えなどの操作ができない
**()よりも重要なのはカンマの方**
numbers = 1,2,3,4
は numbers = (1,2,3,4)を意味する
(0,1) + (2,3)
=> ((0,1), (2,3))

# 辞書型 (mutable)
複数のキー、値の組みを波括弧で[{key1: value1, key2: value2}]のようにまとめて入れておく時に使う
辞書を意味するdictionaryから「dict」型とも呼ばれる
インデックスではなく、キーを指定して値を取得する
リスト型と同じく、追加や削除、書き換えが可能


# 集合型
重複を取り除いて考えたいとき非常に有用な考え方
和集合.... A | B
積集合.... A & B
差集合.... A - B (Aの集合からBの集合を取り除く)


# range
範囲 引数に与えられた数値まで繰り返す(その数は含まない)

# enumerate
enumerate オブジェクトを返します。 iterable は、シーケンスか iterator か、あるいはイテレーションをサポートするその他のオブジェクトでなければなりません。 enumerate() によって返されたイテレータの __next__() メソッドは、 (デフォルトでは 0 となる start からの) カウントと、 iterable 上のイテレーションによって得られた値を含むタプルを返します。
引数で渡したリストをタプル型で渡す関数
第二引数でタプルの添字の開始を指定できる。iterable(反復可能オブジェクト)に対して実行できる

# zip
複数のイテラブルを並行に反復処理し、各イテラブルの要素からなるタプルを生成します。
iterable(反復可能オブジェクト)に対して実行できる
二つのiterableオブジェクトから同時に値を取り出して、繰り返し処理をしたい時に便利
複数の要素が渡された時、個数が合わない時は一番数が少ないものに合わせる

# リスト内方表記
リスト型のオブジェクトを作成する時に用いる
例
nums = [i for i in range(10)]
1~10までのiを入れる -> iをリストの値にする

nums = [i*i for in range(10) if i % 2 == 0]
forの後にifを入れると、その条件に合致したものだけを取り出すことができる

nums=[i  if i % 2 == 0 else i*i for i in range(10)]
iが2で割ることができれば、そのまま初期化してください。
そうでなければiを二乗したものでリストを初期化してください
```
リスト内方表記を使用しないパターン
nums = []

for i in range(10):
  if i % 2 == 0:
    nums.append(i)
  else:
    nums.append(i*i)

print(nums)

```

# map
function を iterable の全ての要素に適用して結果を生成 (yield) するイテレータを返します。追加の iterables 引数が渡された場合、 function は渡されたイテラブルと同じ数の引数を取らなければならず、関数は全てのイテラブルから並行して得られた要素の組に対して適用されます。複数のイテラブルが渡された場合、そのうちで最も短いイテラブルが使い尽くされた段階で止まります。関数の入力が引数タプルとして単一のイテラブルの形で整理されている場合は、 itertools.starmap() を参照してください。


# iterableなオブジェクト
listに変換することができる


# filter
Construct an iterator from those elements of iterable for which function is true. iterable may be either a sequence, a container which supports iteration, or an iterator. If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed.

# lambda式
defを使用しないで関数を定義する。無名関数

```

def is_even(num):
    return num % 2 == 0

nums = map(int, ["1", "2" , "3"])

even_nums = filter(lambda x: x % 2 == 0, nums)

print(list(even_nums))

```


# クラスとオブジェクト
Object...「もの」を表す英単語
Pythonでは数値や文字列などのデータはもちろん、関数なども型を持つオブジェクトととして扱われる(オブジェクト指向プログラミング)
オブジェクトに属性やメソッドを保持させて使用する

比較
== 値として等しいかどうか
is Objectととして等しいかどうか
=> PythonでObjectを作成した時はidが振られる。id関数によって確認可能
値が格納されている"箱"としては別のイメージ

# クラス
Class..「同じようなものの集まり」を表す英単語
オブジェクトを作るための設計図、鋳型のようなもの
インスタンス(instance)...「例」という意味の英単語
クラスからつくられた一つ一つのオブジェクト
例:
「動物」クラスから「ポチ」という名前の動物を作る
自分でオブジェクトを作成したい時に用いる、オブジェクトの設計図、テンプレートのようなもの

