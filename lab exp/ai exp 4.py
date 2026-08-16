from itertools import permutations

def solve_cryptarithm():
    # Unique letters in SEND + MORE = MONEY
    letters = "SENDMORY"

    # Letters S and M cannot be zero
    for digits in permutations(range(10), len(letters)):
        values = dict(zip(letters, digits))

        if values['S'] == 0 or values['M'] == 0:
            continue

        SEND = (
            values['S'] * 1000 +
            values['E'] * 100 +
            values['N'] * 10 +
            values['D']
        )

        MORE = (
            values['M'] * 1000 +
            values['O'] * 100 +
            values['R'] * 10 +
            values['E']
        )

        MONEY = (
            values['M'] * 10000 +
            values['O'] * 1000 +
            values['N'] * 100 +
            values['E'] * 10 +
            values['Y']
        )

        if SEND + MORE == MONEY:
            print("Solution Found!")
            print("SEND  =", SEND)
            print("MORE  =", MORE)
            print("MONEY =", MONEY)
            print("\nLetter - Digit Mapping:")

            for letter, digit in values.items():
                print(letter, "=", digit)

            return

    print("No solution found.")


solve_cryptarithm()
