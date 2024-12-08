## Solution 1

At each position in the string, **record the cumulative counts of 1s and 0s up to that point**. Then iterate through the string again. If the current char is 0, calculate **the product of the number** of 1s before and after it. Same for char 1.

Complexity: O(2n)

## Solution2

Iterate through the string while **keeping track of** the counts of 1s, 0s, 10s, 01s. For each character:
- If 0, **add the counts of 01s to** the number of valid ways, **increment the counts of 10s by the count** of 1s, and increment the counts of 0s by 1
- Same if 1

Complexity: O(n)
