def circ_vis():
    circuits = {
        # \\ or // = not
    'P^Q': """
    P--------\\
            AND----\\ Output
    Q--NOT---/   
             
    """,

    'P^_Q': """
    P----\\
        AND----\\ Output

    Q----/    
             
    """,
    '¬P AND Q': """
    P----\\
        AND----\\
    Q----/    
             Output
    """,
    '¬P AND ¬Q': """
    P----\\
        AND----\\
    Q----/    
             Output
    """,
    'P OR Q': """
    P----\\
        OR----\\
    Q----/    
             Output
    """,
    'P OR ¬Q': """
    P----\\
        OR----\\
    Q----/    
             Output
    """,
    '¬P OR Q': """
    P----\\
        OR----\\
    Q----/    
             Output
    """,
    '¬P OR ¬Q': """
    P----\\
        OR----\\
    Q----/    
             Output
    """,
    'P XOR Q': """
    P----\\
        XOR----\\
    Q----/    
             Output
    """,
    'P XOR ¬Q': """
    P----\\
        XOR----\\
    Q----/    
             Output
    """,
    '¬P XOR Q': """
    P----\\
        XOR----\\
    Q----/    
             Output
    """,
    '¬P XOR ¬Q': """
    P----\\
        XOR----\\
    Q----/    
             Output
    """,
    'P AND Q': """
    P----\\
        AND----\\
    Q----/    
             Output
    """
    }

    print(circuits['P^Q'])

if __name__ == "__main__":
    circ_vis()



