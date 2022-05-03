



class User:
    user_count = 0

    def __init__(self, name : str):

        self.name = name
        self.file = f"{self.name}.json"
        self.high_score = None

        User.user_count += 1


    

    def __str__(self) -> str:
        if self.name[-1].upper() == "S":
            return f"{self.name}\' high score is:\n{self.high_score}"   
        else:
            return f"{self.name}\'s high score is:\n{self.high_score}"