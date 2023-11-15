from Turing import TuringMachine as M, L, R

Q = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
E = ['a', 'b']
G = ['a', 'b', 'X', '_']
d = {
    ('A','a'): ('B','_', R),
    ('A','b'): ('I','_', R),
    ('A','X'): ('I','_', R),
    ('A','_'): ('A','_', R),

    ('B','a'): ('B','a', R),
    ('B','b'): ('C','X', R),
    ('B','X'): ('B','X', R),
    ('B','_'): ('I','_', R),

    ('C','a'): ('I','_', R),
    ('C','b'): ('D','b', L),
    ('C','X'): ('I','_', R),
    ('C','_'): ('G','_', L),

    ('D','a'): ('E','a', L),
    ('D','b'): ('I','_', R),
    ('D','X'): ('D','X', L),
    ('D','_'): ('I','_', R),

    ('E','a'): ('E','a', L),
    ('E','b'): ('I','_', R),
    ('E','X'): ('F','X', R),
    ('E','_'): ('F','_', R),

    ('F','a'): ('B','X', R),
    ('F','b'): ('I','_', R),
    ('F','X'): ('I','_', R),
    ('F','_'): ('I','_', R),

    ('G','a'): ('I','_', R),
    ('G','b'): ('I','_', R),
    ('G','X'): ('G','X', L),
    ('G','_'): ('H','_', R)
}

turing = M(Q, E, G, d, 'A', 'H', 'I')

print("Caso 1: Aceptacion")
turing.execute('aabb')

print("\nCaso 2: Rechazo")
turing.execute('aabbb')

print("\nCaso 3: Bucle")
turing.execute("_")

