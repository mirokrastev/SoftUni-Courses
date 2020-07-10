from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.guild = []

    def assign_player(self, player: Player):
        if player in self.guild:
            return f'Player {player.name} is already in the guild.'
        if player.guild == 'Unaffiliated':
            self.guild.append(player)
            player.guild = self.name
            return f'Welcome player {player.name} to the guild {self.name}'
        return f'Player {player.name} is in another guild.'

    def kick_player(self, player_name):
        players = list(range(len(self.guild)))
        for i in range(len(players)):
            if self.guild[i].name == player_name:
                self.guild[i].guild = 'Unaffiliated'
                self.guild.pop(i)
                return f'Player {player_name} has been removed from the guild.'
        return f'Player {player_name} is not in the guild.'

    def guild_info(self):
        result = f'Guild: {self.name}\n'
        for i in self.guild:
            result += i.player_info()

        return result