def checkio(n):
    if len(n) >=1:
        return (sum(n[0::2])) * n[-1]
    else:
        return 0
        
