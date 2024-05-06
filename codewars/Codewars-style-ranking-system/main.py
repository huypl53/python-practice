class User:
    VALID_RANKS = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self) -> None:
        self.__rank = -8
        self.__progress_score = 0

    @property
    def rank(self):
        return self.__rank

    @property
    def progress(self):
        return self.__progress_score

    def inc_progress(self, progress_rank):
        if progress_rank not in self.VALID_RANKS:
            raise ValueError("Invalid progress rank")

        earn_score = self.__caculate_earn_score(progress_rank)
        self.__update_rank(earn_score)
        self.__update_progress(earn_score)

    def __caculate_earn_score(self, progress_rank):
        diff_rank = 0
        try:
            diff_rank = self.VALID_RANKS.index(progress_rank) - self.VALID_RANKS.index(
                self.__rank
            )
        except Exception:
            print(f"Invalid rank {progress_rank}")

        score = 0
        if diff_rank < -1:
            return score
        match diff_rank:
            case -1:
                score = 1
            case 0:
                score = 3
            case _:
                score = 10 * diff_rank**2
        return score

    def __update_rank(self, earn_score):
        earn_rank = (self.__progress_score + earn_score) // 100

        if self.VALID_RANKS.index(self.__rank) + earn_rank > len(self.VALID_RANKS) - 1:
            self.__rank = self.VALID_RANKS[-1]
            return
        self.__rank = self.VALID_RANKS[self.VALID_RANKS.index(self.__rank) + earn_rank]
        pass

    def __update_progress(self, earn_score):
        if self.__rank == self.VALID_RANKS[-1]:
            self.__progress_score = 0
            return
        self.__progress_score = (self.__progress_score + earn_score) % 100
        pass
