# Python program to solve N Queen 
# Problem using backtracking


print ("Enter the number of queens")
N = int(input())

def printSolution(board):
	for i in range(N):
		for j in range(N):
			print board[i][j],
		print


# A utility function to check if a queen can
# be placed on board[row][col]. Note that this
# function is called when "col" queens are
# already placed in columns from 0 to col -1.
# So we need to check only left side for
# attacking queens
def isSafe(board, i, j):

    #checking if there is a queen in row or column
    for k in range(0,N):
        #row and column
            if board[i][k]=='Q' or board[k][j]=='Q':
                    return True
    #checking diagonals
    for k in range(0,N):
            for l in range(0,N):
                    if (k+l==i+j) or (k-l==i-j):
                            if board[k][l]=='Q':
                                    return True
    return False

def solveNQUtil(board, col):
	# base case: If all queens are placed
	# then return true
	if col >= N:
		return True

	# Consider this column and try placing
	# this queen in all rows one by one
	for i in range(N):

		if not(isSafe(board, i, col)):
			# Place this queen in board[i][col]
			board[i][col] = 'Q'

			# recur to place rest of the queens
			if solveNQUtil(board, col+1) == True:
				return True

			# If placing queen in board[i][col
			# doesn't lead to a solution, then
			# queen from board[i][col]
			board[i][col] = '.'

	# if the queen can not be placed in any row in
	# this colum col then return false
	return False

# This function solves the N Queen problem using
# Backtracking. It mainly uses solveNQUtil() to
# solve the problem. It returns false if queens
# cannot be placed, otherwise return true and
# placement of queens in the form of 1s.
# note that there may be more than one
# solutions, this function prints one of the
# feasible solutions.
def solveNQ():
	board = [['.']*N for _ in range(N)]

	if solveNQUtil(board, 0) == False:
		print "Solution does not exist"
		return False

	printSolution(board)
	return True

# driver program to test above function
solveNQ()


