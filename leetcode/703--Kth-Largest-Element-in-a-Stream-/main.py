from typing import List

max_i = int(1e4)


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.counters = [0] * (2 * (max_i + 1))
        max_n = -max_i
        for n in nums:
            self.counters[n + max_i] += 1
            if n > max_n:
                max_n = n
        self.max_n = max_n
        self.k = k

    def add(self, val: int) -> int:
        checked = 0
        self.counters[val + max_i] += 1
        self.max_n = max(val, self.max_n)
        pos = self.max_n + max_i
        # print(pos, self.k, self.max_n, self.counters)
        checked += self.counters[pos]
        while checked < self.k:
            pos -= 1
            checked += self.counters[pos]
        return pos - max_i


if __name__ == "__main__":

    # Your KthLargest object will be instantiated and called as such:
    data = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
    k = data[0][0]
    nums = data[0][1]
    obj = KthLargest(k, nums)
    for v in data[1:]:
        param = obj.add(v[0])
        print(f"Add {v[0]}, get k-score {param}")
