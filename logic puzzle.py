# Define the knowledge bases for each puzzle
knowledge0 = [('A', "I am both a knight and a knave.")]
knowledge1 = [
    ('A', "We are both knaves."),
    ('B', "")  # B says nothing
]
knowledge2 = [
    ('A', "We are the same kind."),
    ('B', "We are of different kinds.")
]
knowledge3 = [
    ('A', "I am a knight or I am a knave."),
    ('B', "A said 'I am a knave.'"),
    ('B', "C is a knave."),
    ('C', "A is a knight.")
]

def is_knight(knowledge_base, person):
    # Helper function to check if a person is a knight based on the knowledge base
    for speaker, claim in knowledge_base:
        if speaker == person:
            if person == 'A':
                return claim == "I am a knight or I am a knave."
            else:
                return claim == "I am a knight."
    return False

def is_knave(knowledge_base, person):
    # Helper function to check if a person is a knave based on the knowledge base
    return not is_knight(knowledge_base, person)

def solve_puzzle(knowledge_base):
    # List to store the solution(s) found
    solutions = []

    # Check all possible combinations of knights and knaves for each person
    for a_knight in [True, False]:
        for b_knight in [True, False]:
            for c_knight in [True, False]:
                # Apply the knowledge base to check consistency
                if (
                    is_knight(knowledge_base, 'A') == a_knight and
                    is_knight(knowledge_base, 'B') == b_knight and
                    is_knight(knowledge_base, 'C') == c_knight
                ):
                    # Check if there is exactly one knight in the group
                    if sum([a_knight, b_knight, c_knight]) == 1:
                        solution = {
                            'A': 'Knight' if a_knight else 'Knave',
                            'B': 'Knight' if b_knight else 'Knave',
                            'C': 'Knight' if c_knight else 'Knave',
                        }
                        solutions.append(solution)

    return solutions

if __name__ == "__main__":
    # Solve each puzzle and print the solutions
    print("Puzzle 0:")
    for solution in solve_puzzle(knowledge0):
        print(solution)

    print("\nPuzzle 1:")
    for solution in solve_puzzle(knowledge1):
        print(solution)

    print("\nPuzzle 2:")
    for solution in solve_puzzle(knowledge2):
        print(solution)

    print("\nPuzzle 3:")
    for solution in solve_puzzle(knowledge3):
        print(solution)
