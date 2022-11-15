class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
    
    def top_scorers_by_nationality(self, nationality):
        print("Oliot:")
        return sorted(filter(lambda x: x.nationality == nationality, self.reader.get_players()), key=lambda y: y.goals + y.assists, reverse=True)