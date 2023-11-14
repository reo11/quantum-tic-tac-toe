# quantum-tic-tac-toe
量子五目並べ
https://www.youtube.com/watch?v=mitAxA3f4U4

## ゲームの始め方
```
python main.py
```

## 注意点
- ゲームを中断しようすると無限ループが発生するので注意

## 決着例
```
x: Black, o: White
  A B C D E F G H I J
1 1 9 1 9
2 1   1
3   9     9
4 9   1   9
5       9 9 1
6         9
7           9
8             9
9
10
Player Black's turn
Enter the coordinates of the stone you want to place. (ex. A1)
E2
Enter the value between 1 to 9 (White 1 ... 9 Black
9
Player Black placed 9 at E2
Do you want to make an observation? (y/n)
y
x: Black, o: White
  A B C D E F G H I J
#### Observed Board ####
1 o o o x
2 o   x   x
3   x     x
4 x   o   x
5       x x o
6         x
7           x
8             x
9
10
#### Observed Board End ####
Black win
```
