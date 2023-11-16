class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        vowel_positions = [i for i, char in enumerate(s) if char in vowels]

        sorted_vowels = sorted([char for char in s if char in vowels])

        result = list(s)
        for position, vowel in zip(vowel_positions, sorted_vowels):
            result[position] = vowel

        return ''.join(result)