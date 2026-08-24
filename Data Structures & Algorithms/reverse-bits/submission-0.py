class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(n.bit_length()):
            bit = ((n >> i) & 1)
            res |= (bit << (31 - i))
        return res

