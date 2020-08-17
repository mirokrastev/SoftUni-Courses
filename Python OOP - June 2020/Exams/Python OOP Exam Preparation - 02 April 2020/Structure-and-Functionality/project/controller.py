from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository
from project.battle_field import BattleField


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, type, username):
        if type == 'Beginner':
            new = Beginner(username)
        else:
            new = Advanced(username)

        self.player_repository.add(new)
        return f'Successfully added player of type {type} with username: {username}'

    def add_card(self, type, name):
        if type == 'Magic':
            new = MagicCard(name)
        else:
            new = TrapCard(name)

        self.card_repository.add(new)
        return f'Successfully added card of type {type}Card with name: {name}'

    def add_player_card(self, username, card_name):
        card = self.card_repository.find(card_name)
        player = self.player_repository.find(username)

        if not card or not player: return

        player.card_repository.add(card)
        return f'Successfully added card: {card.name} to user: {username}'

    def fight(self, attack_name, enemy_name):
        attacker = self.player_repository.find(attack_name)
        enemy = self.player_repository.find(enemy_name)

        if not attacker or not enemy: return
        BattleField.fight(attacker, enemy)

        return f'Attack user health {attacker.health} - Enemy user health {enemy.health}'

    def report(self):
        result = f''

        for player in self.player_repository.players:
            result += f'Username: {player.username} - Health: {player.health} - ' \
                      f'Cards {player.card_repository.count}\n'

            result += "".join(f'### Card: {card.name} - Damage: {card.damage_points}\n'
                              for card in player.card_repository.cards)

        return result
