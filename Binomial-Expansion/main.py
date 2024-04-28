from math import comb


def expand(expr: str) -> str:
    """
    Expand `(ax+b)^n` to ax^b+cx^d+ex^f+...
    """
    hat_sign = "^"
    oprt, n = expr.split(hat_sign)
    n = int(n)

    valid_operators = ["+", "-"]
    oprt = oprt[1:-1]
    if n == 0:
        return "1"
    if n == 1:
        return oprt

    i = len(oprt) - 1

    b_str_arr = []
    x = "x"
    a_str = ""

    while i > -1:
        current_c = oprt[i]
        b_str_arr.append(current_c)

        if current_c in valid_operators:
            x = oprt[i - 1]
            a_str = oprt[: i - 1]
            break

        i -= 1
    b_str = "".join(b_str_arr[::-1])
    b = int(b_str)

    a = 1
    if len(a_str):
        if a_str == "-":
            a = -1
        else:
            a = int(a_str)

    if b == 0:
        result = f"{str(a^n)}{x}{hat_sign}{n}"
        return result

    res_str_arr = []

    for i in range(n, -1, -1):
        ai = 1 if i == 0 else a**i
        bni = 1 if n - i == 0 else b ** (n - i)

        a_n = comb(n, n - i) * ai * bni
        # CHEAT: ignore a_n = 0
        if a_n == 1:
            a_n_str = ""
        elif a_n == -1:
            a_n_str = "-"
        else:
            a_n_str = str(a_n)

        if i == 1:
            op_str = f"{a_n_str}{x}"
        elif i == 0:
            if a_n == 1:
                op_str = "1"
            else:
                op_str = f"{a_n_str}"

        else:
            op_str = f"{a_n_str}{x}{hat_sign}{i}"

        if i < n:
            if a_n > 0:
                op_str = f"+{op_str}"

        # if i == 0:
        #     op_str = op_str[:-2]

        res_str_arr.append(op_str)

    return "".join(res_str_arr)


if __name__ == "__main__":
    tests = ["(x+1)^1", "(-x+1)^2"]
    print(expand(tests[1]))
