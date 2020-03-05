class Solution:
    def compress(self, chars: List[str]) -> int:
        num = 1
        tmp = chars[0]
        for i in range(1,len(chars)):
            if chars[i - 1] == chars[i]:
                num +=1
                if i == len(chars) - 1:
                    tmp += str(num)
            elif chars[i - 1] != chars[i] and num != 1:
                tmp += str(num)
                tmp += chars[i]
                num = 1
            elif chars[i - 1] != chars[i] and num == 1:
                tmp += chars[i]
                num = 1
        for i in range(len(tmp)):
            chars[i] = tmp[i]
        chars = chars[:len(tmp)]
        return len(chars)


