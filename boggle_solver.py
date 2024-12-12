class Boggle:
    def __init__(self, board, dictionary):
        """
        Initialize the Boggle game with the provided board and dictionary.
        """
        if not self.check_grid_validity(board):
            self.board = []
            self.n = 0
        else:
            self.board = [[char.upper() for char in row] for row in board]
            self.n = len(board)

        self.dictionary = set(word.upper() for word in dictionary)
        self.prefixes = self.create_prefixes(self.dictionary)
        self.directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1),  (1, 0), (1, 1)
        ]

    def check_grid_validity(self, board):
        """
        Verify if the input grid is valid.
        """
        if not board or not all(board):
            return False
        row_lengths = {len(row) for row in board}
        return len(row_lengths) == 1  # Ensures all rows are uniform in length

    def create_prefixes(self, dictionary):
        """
        Generate a set of all possible prefixes from the dictionary.

        :param dictionary: Set of valid words.
        :return: A set with all possible prefixes.
        """
        prefixes = set()
        for word in dictionary:
            for i in range(1, len(word)):
                prefixes.add(word[:i])
        return prefixes

    def dfs(self, i, j, visited, current_word):
        """
        Perform Depth-First Search starting from cell (i, j).
        """
        if (i < 0 or i >= self.n or j < 0 or
                j >= len(self.board[i]) or visited[i][j]):
            return

        current_word.append(self.board[i][j])
        added_chars = 0

        if self.board[i][j] == 'Q':
            current_word.append('U')
            added_chars += 1

        if self.board[i][j] == 'S' and (len(current_word) < 2 or
                                        current_word[-2] != 'Q'):
            current_word.append('T')
            added_chars += 1

        word = ''.join(current_word)

        if word not in self.prefixes and word not in self.dictionary:
            for _ in range(1 + added_chars):
                if current_word:
                    current_word.pop()
            return

        if len(word) >= 3 and word in self.dictionary:
            self.found_words.add(word)

        visited[i][j] = True

        for di, dj in self.directions:
            self.dfs(i + di, j + dj, visited, current_word)

        visited[i][j] = False
        for _ in range(1 + added_chars):
            if current_word:
                current_word.pop()

    def getSolution(self):
        """
        Find all valid words on the Boggle board using the dictionary.
        """
        self.found_words = set()
        if self.n == 0:
            return []
        visited = [[False for _ in row] for row in self.board]

        for i in range(self.n):
            for j in range(len(self.board[i])):
                self.dfs(i, j, visited, [])

        return sorted(self.found_words)


def main():
    """
    Example usage of the Boggle class.
    """
    grid = [
        ['D', 'E', 'F'],
        ['E', 'A', 'B'],
        ['E', 'B', 'C'],
        ['E', 'C', 'B'],
        ['E', 'D', 'B'],
        ['E', 'F', 'B'],
        ['E', 'G', 'H'],
        ['E', 'H', 'I'],
        ['E', 'I', 'H']
    ]

    dictionary = ['DEF', 'EAB', 'EBC',
                  'ECB', 'EDB', 'EFB',
                  'EGH', 'EHI', 'EIH']
    mygame = Boggle(grid, dictionary)
    print(sorted(mygame.getSolution()))


if __name__ == "__main__":
    main()
