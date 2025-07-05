class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        move = {0: (1, 3), 1: (0, 2, 4), 2: (1, 5), 3: (0, 4), 4: (1, 3, 5), 5: (2, 4)}
        target = bytes((1, 2, 3, 4, 5, 0))
        prev_queue, queue, step = set(), {bytes(chain(*board))}, 0
        while queue:
            new_queue = set()
            for curr_board in queue:
                if curr_board == target:
                    return step
                new_board, i = bytearray(curr_board), curr_board.index(0)
                for ii in move[i]:
                    new_board[i], new_board[ii] = new_board[ii], new_board[i]
                    new_board_b = bytes(new_board)
                    if new_board_b not in prev_queue:
                        new_queue.add(new_board_b)
                    new_board[i], new_board[ii] = new_board[ii], new_board[i]
            step += 1
            prev_queue, queue = queue, new_queue
        return -1