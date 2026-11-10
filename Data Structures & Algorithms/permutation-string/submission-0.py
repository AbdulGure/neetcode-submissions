class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        frequency = {}
        for char in s1:
            frequency[char] = frequency.get(char, 0) + 1

        window = {}
        for char in s2[:len(s1)]:
            window[char] = window.get(char, 0) + 1

        if window == frequency:
            return True

        for i in range(len(s2) - len(s1)):
            leaving = s2[i]
            entering = s2[i + len(s1)]

            window[leaving] -= 1
            if window[leaving] == 0:
                del window[leaving]
            window[entering] = window.get(entering, 0) + 1

            if window == frequency:
                return True

        return False