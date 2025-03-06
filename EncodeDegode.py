from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        # Join the list of strings into a single string, separated by '#'
        return '#'.join(strs)

    def decode(self, s: str) -> List[str]:
        # Split the string 's' by '#' to get a list of strings
        return s.split('#')

# Example usage
solution = Solution()

# Testing with a list of strings
strs = ["hello", "world", "test"]

# Encode the list of strings into a single string
encoded = solution.encode(strs)
print("Encoded:", encoded)  # Expected output: "hello#world#test"

# Decode the encoded string back into a list of strings
decoded = solution.decode(encoded)
print("Decoded:", decoded)  # Expected output: ["hello", "world", "test"]
