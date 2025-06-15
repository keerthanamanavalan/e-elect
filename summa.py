def gameOfLife(board):
    m, n = len(board), len(board[0])
    directions = [
        (-1, -1), (-1, 0), (-1, 1), 
        (0, -1),        (0, 1), 
        (1, -1), (1, 0), (1, 1)
    ]
    next_state = [[0] * n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            live_neighbors = 0
            
            for direction in directions:
                ni, nj = i + direction[0], j + direction[1]
                if 0 <= ni < m and 0 <= nj < n:
                    live_neighbors += board[ni][nj]
            
            if board[i][j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    next_state[i][j] = 0
                else:
                    next_state[i][j] = 1
            else:
                if live_neighbors == 3:
                    next_state[i][j] = 1
    
    for i in range(m):
        for j in range(n):
            board[i][j] = next_state[i][j]
    
    return board

