import collections  # 这个模块实现了特定目标的容器，以提供Python标准内建容器 dict , list , set , 和 tuple 的替代选择。
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])  # 创建命名元组子类的工厂函数


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FrenchDeck()
print(choice(deck))

for card in deck:  # 由于__getitem_方法，这一摞纸牌变成可迭代的了
    print(card)

for card in reversed(deck):  # 也可以反向迭代
    print(card)
