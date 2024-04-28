# from preloaded import ACTIONS

_actions = [
    lambda x: x + 1,
    lambda x: 0,
    lambda x: x / 2,
    lambda x: x * 100,
    lambda x: x % 2,
]


ACTIONS = lambda: _actions


class Machine:
    def __init__(self):
        self._actions = ACTIONS()
        self._cmd_action = dict()
        self._curr_cmd = None

    def command(self, cmd, num):
        self._curr_cmd = cmd
        if cmd in self._cmd_action.keys():
            id = self._cmd_action[cmd]["id"]
            return self._actions[id](num)
        else:
            self._cmd_action[cmd] = {"id": 0}
            return self._actions[0](num)
            pass
        pass

    def response(self, res):
        if res:
            pass
        else:
            self._cmd_action[self._curr_cmd]["id"] += 1
        pass


if __name__ == "__main__":
    import random

    tests = [
        (0, 100, 101, "Should apply the num + 1 action to the command 0"),
        (1, 100, 0, "Should apply the num * 0 action to the command 1"),
        (2, 100, 50, "Should apply the num / 2 action to the command 2"),
        (3, 1, 100, "Should apply the num * 100 action to the command 3"),
        (4, 100, 0, "Should apply the num % 2 action to the command 4"),
    ]

    machine = Machine()
    for i in range(0, 200):
        number = random.randint(0, 100)
        num = machine.command(i % 5, number)
        machine.response(_actions[i % 5](number) == num)

    for t in tests:

        def test_it():
            num = machine.command(t[0], t[1])
            assert num == t[2]
