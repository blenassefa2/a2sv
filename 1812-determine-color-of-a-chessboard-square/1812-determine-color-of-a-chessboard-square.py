class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if ord(coordinates[0]) % 2:
            return int(coordinates[1]) %2 == 0
        
        return int(coordinates[1])%2 != 0