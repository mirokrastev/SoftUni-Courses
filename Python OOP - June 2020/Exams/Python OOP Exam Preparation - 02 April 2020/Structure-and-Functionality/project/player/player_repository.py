from project.player.player import Player
from typing import List


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players: List[Player] = []

    def add(self, player: Player):
        player_names = self.find(player.username)
        if player_names:
            raise ValueError(f'Player {player.username} already exists!')
        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        if not player:
            raise ValueError('Player cannot be an empty string!')
        player = self.find(player)
        if not player: return

        self.players.remove(player)
        self.count -= 1

    def find(self, username):
        players = [p for p in self.players if p.username == username]
        if not players: return

        return players[0]