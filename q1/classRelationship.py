class Player:
    def __init__(self, name: str, jersey_number: int, position: str, is_starter: bool):
        self.name = name
        self.jerseyNumber = jersey_number
        self.__position = position
        self.__isStarter = is_starter

    def get_position(self):
        return self.__position

    def set_starter_status(self, status: bool):
        self.__isStarter = status
        print(f"Update: {self.name}'s starter status is now {self.__isStarter}.")

    def display_info(self):
        role = "Starter" if self.__isStarter else "Substitute"
        print(f"  - #{self.jerseyNumber} {self.name} | Position: {self.__position} | Status: {role}")

class Team:
    def __init__(self, team_name: str, coach_name: str):
        self.team_name = team_name
        self.coach_name = coach_name
        self.roster = []

    def add_player(self, player: Player):
        self.roster.append(player)
        print(f"Added {player.name} to {self.team_name}.")

    def display_roster(self):
        print(f"{self.team_name} Roster (Head Coach: {self.coach_name})")
        if not self.roster:
            print("No players currently on the roster.")
        else:
            for player in self.roster:
                player.display_info()

if __name__ == "__main__":
    print("--- BEFORE RELATIONSHIP ---")
    ReneKarasuno = Team("ReneKarasuno Palo", "Tab Baldwin")
    
    player1 = Player("Rene", 58, "Outside Hitter", False)
    player2 = Player("Bater", 68, "Setter", True)
    player3 = Player("Bonia", 67, "Outside Hitter", True)

    player1.display_info()
    player2.display_info()
    player3.display_info()

    print("BUILDING RELATIONSHIP")
    ReneKarasuno.add_player(player1)
    ReneKarasuno.add_player(player2)
    ReneKarasuno.add_player(player3)

    print("AFTER RELATIONSHIP")
    ReneKarasuno.display_roster()