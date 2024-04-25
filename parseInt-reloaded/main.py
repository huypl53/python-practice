from typing import Iterable, List, Tuple


def read_pattern(pattern: str) -> Iterable[int]:  # -> Union[str, None]:
    if pattern in IntStringParser.NUM_DICT.keys():
        yield IntStringParser.NUM_DICT[pattern]
    elif "-" in pattern:
        for sub_pattern in pattern.split("-"):
            s = read_pattern(sub_pattern)
            yield from s
    else:
        return


class IntStringParser:
    NUM_DICT = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
    }

    SCALES = {"hundred": int(1e2), "thousand": int(1e3), "million": int(1e6)}

    def __init__(self) -> None:
        self.__int_value = 0
        self.__patterns: List[str] = []

        pass

    @property
    def intValue(self):
        return self.__int_value

    def parse(self, int_string: str):
        self.__preprocess()
        self.__patterns = int_string.split()

        current_scale = 1
        max_scale = 1
        int_value = 0
        for pattern in self.__patterns[::-1]:
            if pattern in self.SCALES.keys():
                current_scale = self.SCALES[pattern]
                if current_scale > max_scale:
                    max_scale = current_scale

                continue
            add_amount = sum(list(read_pattern(pattern)))
            if current_scale < max_scale:
                add_amount *= current_scale * max_scale
            else:
                add_amount *= current_scale

            int_value += add_amount

        self.__int_value = int_value

    def __preprocess(self):
        pass


def parse_int(string: str) -> int:
    parser = IntStringParser()
    parser.parse(string)
    return parser.intValue
