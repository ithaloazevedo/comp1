
def safe_pawns(pawns: set) -> int:
    safe_no=0
    for pawn in pawns:
        p1=chr(ord(pawn[0])-1)+str(int(pawn[1])-1)
        p2=chr(ord(pawn[0])+1)+str(int(pawn[1])-1)
        safe_no += p1 in pawns or p2 in pawns
    return safe_no
