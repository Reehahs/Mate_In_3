import moveGen

board = moveGen.Board("6r1/p3p1rk/1p1pPp1p/q3n2R/4P3/3BR2P/PPP2QP1/7K w")

moves = list(board.legal_moves)
solutions = 0

def search(b, m, d, who):
    #Search too deep
    if d > 5:
        return False

    #Create the new node
    temp = b.copy()

    #Do a move from the list
    s = str(m.pop())
    
    temp.push_san(s)

    """Stop if you find a checkmate"""
    if temp.is_checkmate() and who == 0:
        print(temp, "<--\n")
        global solutions
        solutions += 1
        return b

    # Iterate through all items in the list
    # of possible moves
    elif len(m) > 0:
        #print(temp)
        x = search(b, m, d, who)
        if x != False:
            #return x.append(b)
            print(x, "\n")

    moves = list(temp.legal_moves)
    
    if temp.is_check() and who == 0: 
        x = search(temp, moves, d + 1, 1)
        if x != False:
            print(x, "\n")
            return x.append(b)
    elif who == 1:
        x = search(temp, moves, d + 1, 0)
        if x != False:
            print(x, "\n")
            return x.append(b)
    
    return False


# Start search 
print(search(board, list(board.legal_moves), 0,0))
print("There was,", solutions, "checkmate scenario's")



