from project.card.card import Card
from typing import List


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards: List[Card] = []

    def add(self, card: Card):
        cards = self.find(card.name)

        if cards:
            raise ValueError(f'Card {card.name} already exists!')
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if not card:
            raise ValueError('Card cannot be an empty string!')
        card = self.find(card)

        if not card: return
        self.cards.remove(card)
        self.count -= 1

    def find(self, name):
        cards = [c for c in self.cards if c.name == name]
        if not cards: return

        return cards[0]