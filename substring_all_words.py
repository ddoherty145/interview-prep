# Imagine you’re a detective in a word puzzle game, and your mission is to find hidden messages in a long
# string of text. The string is like a secret code, and you’re given a list of specific words that must appear
# together, in any order, to form a valid message. These words are like puzzle pieces, all the same length,
# and you need to find where in the text they fit together perfectly, with no extra letters in between, using
# each word exactly as many times as it appears in the list. Your job is to report the starting positions of
# these hidden messages.

# 30. Substring with Concatenation of All Words
# You are given a string s and an array of strings words of the same length.
# Return all starting indices of substring(s) in s that is a concatenation of each word
# in words exactly once, in any order, and without any intervening characters.
# You can return the answer in any order.

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # Handle edge cases
        if not s or not words:
            return []
        
        # Initialize variables
        word_length = len(words[0])
        word_count = len(words)
        total_length = word_length * word_count
        word_map = {}
        
        # Build the frequency map for the words
        for word in words:
            word_map[word] = word_map.get(word, 0) + 1
        
        # Initialize the result list
        result = []
        
        # Slide window and check for valid concatenations
        for i in range(len(s) - total_length + 1):
            seen = {}
            j = 0
            while j < word_count:
                word_index = i + j * word_length
                word = s[word_index:word_index + word_length]
                
                if word not in word_map:
                    break
                
                seen[word] = seen.get(word, 0) + 1
                
                if seen[word] > word_map[word]:
                    break
                
                j += 1
            
            if j == word_count:
                result.append(i)
        
        return result