from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave." (A ∨ B) ∧ ¬ (A ∧ B)
knowledge0 = And(
    And(Or(AKnave,AKnight), Not(And(AKnave,AKnight))),
    Implication(AKnave,Not(And(AKnight,AKnave))),
    Implication(AKnight,(And(AKnight,AKnave)))
)
# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Implication(AKnight, And(AKnave,BKnave)),
    Or(And(AKnight,BKnave), And(AKnight,BKnight), And(AKnave,BKnave), And(AKnave,BKnight)),
    Implication(AKnave, Not(And(AKnave,BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Implication(AKnight, Or(And(AKnight,BKnight),And(AKnave,BKnight))),
    Implication(BKnight, Or(And(AKnight,BKnave),And(AKnave,BKnight))),
    Or(And(AKnight,BKnave), And(AKnight,BKnight), And(AKnave,BKnave), And(AKnave,BKnight)),
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave,BKnave)))),
    Implication(BKnave, Not(Or(And(AKnight,BKnave), And(AKnave,BKnight))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
# knowledge3 = And(

#     Implication(BKnight, CKnave),
#     Implication(BKnave, CKnight),
#     Implication(CKnight, AKnight),
#     Implication(BKnight, CKnave),
#     Implication(BKnave, CKnight),
#     Implication(CKnave, Not(AKnight)),
#     Implication(AKnave, Not(AKnight)),
#     Or(AKnight,AKnave),Or(BKnight, BKnave), Or(CKnight,CKnave),
#     Or(And(AKnight,BKnight,CKnight),
#        And(AKnight,BKnight,CKnave),
#        And(AKnight,BKnave, CKnight),
#        And(AKnight,BKnave,CKnave),
#        And(AKnave,BKnave,CKnave),
#        And(AKnave,BKnave,CKnave),
#        And(AKnave,BKnight,CKnight),
#        And(AKnave,BKnave,CKnight),
#        And(AKnave,BKnight,CKnave)
#     )

#)

knowledge3 = And( And(Or(AKnave,AKnight), 
            Not(And(AKnave,AKnight))), 
            And(Or(BKnave,BKnight), Not(And(BKnave,BKnight))), 
            And(Or(CKnave,CKnight), Not(And(CKnave,CKnight))), 
            Implication(BKnave,Not(CKnave)), 
            Implication(BKnight,CKnave), 
            Implication(CKnave,Not(AKnight)), 
            Implication(CKnight,AKnight), 
            Implication(AKnave,Not(Or(AKnight,AKnave))), 
            Implication(AKnight,Or(AKnight,AKnave)))


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
