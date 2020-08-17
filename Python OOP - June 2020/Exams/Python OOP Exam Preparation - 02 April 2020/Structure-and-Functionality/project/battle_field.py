from project.player.player import Player


class BattleField:
    @staticmethod
    def fight(attacker: Player, enemy: Player):
        players = (attacker, enemy)
        for player in players:
            if BattleField.check_dead(player):
                raise ValueError('Player is dead!')

            BattleField.increase_health(player)

            if player.__class__.__name__ == 'Beginner':
                BattleField.beginner_bonuses(player)

        inx = 1

        for attacker in players:
            BattleField.attack(attacker, players[inx])

            inx -= 1

    @staticmethod
    def attack(attacker: Player, enemy: Player):
        for card in attacker.card_repository.cards:
            enemy.take_damage(card.damage_points)

            if BattleField.check_dead(enemy):
                raise ValueError('Player is dead!')

    @staticmethod
    def check_dead(player):
        return player.is_dead

    @staticmethod
    def increase_health(player):
        bonus_health = sum([c.health_points for c in player.card_repository.cards])
        player.health += bonus_health

    @staticmethod
    def beginner_bonuses(player):
        player.health += 40

        for card in player.card_repository.cards:
            card.damage_points += 30