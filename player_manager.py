from database import Database

class PlayerManager:
    def __init__(self):
        self.db = Database()

    def get_players(self):
        return self.db.queryview('SELECT playerID, name, wins, losses, ties, (wins + losses + ties) AS Games FROM Player ORDER BY wins DESC')

    def add_player(self, name, wins, losses, ties):
        self.db.querymod('INSERT INTO Player (name, wins, losses, ties) VALUES (?, ?, ?, ?)', (name, wins, losses, ties))

    def delete_player(self, name):
        self.db.querymod('DELETE FROM Player WHERE name = ?', (name,))

    def player_exists(self, name):
        result = self.db.queryview('SELECT COUNT(*) FROM Player WHERE name = ?', (name,))
        return result[0][0] > 0

    def update_player(self, name, wins, losses, ties):
        self.db.querymod('UPDATE Player SET wins = ?, losses = ?, ties = ? WHERE name = ?', (wins, losses, ties, name))
