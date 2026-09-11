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
        print(f"#{self.jerseyNumber} {self.name} | Position: {self.__position} | Status: {role}")


player1 = Player("Alyssa", 2, "Outside Hitter", False)
player2 = Player("Jia", 12, "Setter", True)

print("BEFORE")
player1.display_info()
player2.display_info()

print("ACTION")
player1.set_starter_status(True)

print("AFTER")
player1.display_info()
player2.display_info()