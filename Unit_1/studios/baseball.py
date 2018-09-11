# A baseball player has a name and a jersey number. Most players hit either right or left,
# but some can hit either way. This object should be able to react when a player completes
# a game, recording how many hits and RBIs the player earned in that game. A player has a
# Certain number of runs and RBIs he or she has recorded over all games played.
# A player has a certain number of games he or she has played.


class BaseballPlayer:

    def __init__(self, player_name, jersey_number, hit):
        self.name = player_name
        self.number = jersey_number
        self.hit = hit

    def __repr__(self):
        return 'Player is %s and his jersey number is %d and he hits from %s side' % (self.name, self.number, self.hit)


class Stats(BaseballPlayer):

    def __init__(self, player_name, jersey_number, hit):
        self.hits = 0
        self.rbi = 0
        self.game_hits = 0
        self.game_rbi = 0

        super().__init__(player_name, jersey_number, hit)

    def overall_stats(self, hits, rbi):

        self.hits = int(self.hits) + int(hits)
        self.rbi = int(self.rbi) + int(rbi)

        return (self.hits, self.rbi)

    def game_finished(self, hits, rbi):
        self.game_hits = hits
        self.game_rbi = rbi
        Stats.overall_stats(self, self.game_hits, self.game_rbi)
        return ('%s had %d hits and %d RBIs in todays game!' % (self.name, self.hits, self.rbi))


john = Stats('John DOe', 26, 'left')

print(john.game_finished(3, 2))
# print(john.overall_stats())
print(Stats.overall_stats(john))
