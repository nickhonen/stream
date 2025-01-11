# I suck at leetcode
# I am cramming for an interview tomorrow
# I thought streaming might be able to help me focus

# problems 1/9/25: contains duplicate, pangram,count prefix and suffix pairs 1, valid parens

# I am open to any music suggestions and playlists

from collections import Counter
class Solution:
    def containsDuplicate(self, nums):
        # you can use sets in python to not have duplicates
        # if the length of nums is != len of the set
        # sets only have unique values
        nums_set = set(nums)
        return len(nums) != len(nums_set)

    def pangram(self, sentence):
        # hash table to count occurrences of letters
        # dont need to worry about cases or ascii
        # counter_obj = Counter(sentence)
        # return len(counter_obj) >= 26
        d = {}
        for char in sentence:
            lower = char.lower()
            if d.get(char, 0) == 0:
                d[char] = 1
            else:
                d.get(char)
            count += 1
            d[char] = count
        return len(d.keys())

    



if __name__ == '__main__':
    sol = Solution()
    test1 = "TheQuickBrownFoxJumpsOverTheLazyDog"
    test2 = "This is not a pangram"
    test3 = "abcdef"
    test4 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    print(sol.pangram(test1))
    print(sol.pangram(test2))
    print(sol.pangram(test3))
    print(sol.pangram(test4))
