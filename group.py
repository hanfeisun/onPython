def group (source, n):
    """
    group([1,2,3,4],2) -> [[1, 2], [3, 4]]
    group([1,2,3,4],3) -> [[1, 2, 3], [4]]
    """
    acc = []
    rest = source
    
    if not n:
        return []

    while rest:
        acc.append(source[:n])
        rest = source[n:]
        source = rest        
    return acc
    
        
    
    
