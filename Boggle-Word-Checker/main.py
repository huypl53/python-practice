from typing import List, Tuple, Union


class BoggleChar:
    """
    index[int, int]: (y, x) in board
    char[str]: char representation
    """

    def __init__(self, char: str, index: Tuple[int, int]) -> None:
        self._data = char
        self._y, self._x = index
        self._checked = False

    @property
    def checked(self):
        return self._checked

    @checked.setter
    def checked(self, value):
        self._checked = value

    @property
    def data(self):
        return self._data

    @property
    def index(self):
        return self._x, self._y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __str__(self) -> str:
        return self.data

    def __eq__(self, value: Union[str, "BoggleChar"]) -> bool:
        if type(value) == str:
            return value == self.data
        if type(value) == BoggleChar:
            return value.data == self.data
        raise Exception(f"value type {type(value)} must be type str or {type(self)}")

        pass

    def is_neighbor(self, bc: "BoggleChar"):
        dx = abs(self.x - bc.x)
        dy = abs(self.y - bc.y)
        if dx + dy == 1 or dx * dy == 1:
            return True
        return False

    def match_group(self, group_chars: List["BoggleChar"]):
        if len(group_chars) == 0:
            return True
        # for c in group_chars:
        #     if self.is_neighbor(c):
        #         return True
        if self.is_neighbor(group_chars[-1]):
            return True
        return False


def find_word(board: List[List[str]], word: str) -> bool:
    chars: List[BoggleChar] = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] in word:
                chars.append(BoggleChar(board[i][j], (i, j)))

    if len(chars) < len(word):  # Lack of chars
        return False

    def find_chars(
        bag_chars: List[BoggleChar], chars: List[BoggleChar], word_chars: List[str]
    ) -> bool:
        word_char = word_chars.pop()
        for i, char in enumerate(chars):
            if char.checked:
                continue
            if word_char == char:

                char.checked = True
                if char.match_group(bag_chars):
                    bag_chars.append(char)
                    if len(word_chars) == 0:
                        return True

                    if find_chars(bag_chars, chars, word_chars):
                        return True
                    bag_chars.pop()
                pass
                char.checked = False

        word_chars.append(word_char)
        return False

    bag_chars: List[BoggleChar] = []
    word_chars: List[str] = list(word)[::-1]

    return find_chars(bag_chars, chars, word_chars)


if __name__ == "__main__":
    testBoard = [
        ["E", "A", "R", "A"],
        ["N", "L", "E", "C"],
        ["I", "A", "I", "S"],
        ["B", "Y", "O", "R"],
    ]
    test = [
        "C",
        "EAR",
        "EARS",
        "BAILER",
        "RSCAREIOYBAILNEA",
        "CEREAL",
        "ROBES",
    ]

    for t in test:
        print(t, find_word(testBoard, t))
