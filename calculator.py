# -----------------------------------------------------------------------------
# Christian Ricardo Solís Cortés
# A01063685
# Artificial Intelligence
# Demo Assignment for AlphaGrader:
# Build a calculator that adds two numbers.
# -----------------------------------------------------------------------------

try:
    while True:
        a = input()
        b = input()
        c = int(a) + int(b)
        print(c)
except EOFError:
    pass
