from collections import Counter
def solution(board, nums):
    answer = 0
    bingo_coordinates = set(nums)
    N = len(board)

    bingo_col = [0 for _ in range(N)]
    bingo_row = [0 for _ in range(N)]
    bingo_cross1 = 0
    bingo_cross2 = 0

    for row in range(N):
        for col in range(N):
            if board[row][col] in bingo_coordinates: #
                bingo_col[col] += 1
                bingo_row[row] += 1

                if row == col:
                    bingo_cross1 += 1

                if row + col == N-1:
                    bingo_cross2 += 1

    col_answer = Counter(bingo_col)[N]
    row_answer = Counter(bingo_row)[N]

    answer += col_answer
    answer += row_answer
    answer += bingo_cross1 == N
    answer += bingo_cross2 == N


    return answer

if __name__ == '__main__':
  board = [[11,13,15,16],[12,1,4,3],[10,2,7,8],[5,14,6,9]]
  nums = [14,3,2,4,13,1,16,11,5,15]
  print(solution(board, nums)) # 3
