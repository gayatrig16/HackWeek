import random
import time

# Optional: ASCII art for dice faces
dice_faces = {
    1: ("+-------+",
        "|       |",
        "|   o   |",
        "|       |",
        "+-------+"),

    2: ("+-------+",
        "| o     |",
        "|       |",
        "|     o |",
        "+-------+"),

    3: ("+-------+",
        "| o     |",
        "|   o   |",
        "|     o |",
        "+-------+"),

    4: ("+-------+",
        "| o   o |",
        "|       |",
        "| o   o |",
        "+-------+"),

    5: ("+-------+",
        "| o   o |",
        "|   o   |",
        "| o   o |",
        "+-------+"),

    6: ("+-------+",
        "| o   o |",
        "| o   o |",
        "| o   o |",
        "+-------+")
}

def roll_dice():
    input("🎲 Press Enter to roll the dice...")
    
    print("Rolling", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print()

    result = random.randint(1, 6)
    print(f"\nYou rolled a {result}!\n")

    for line in dice_faces[result]:
        print(line)

if __name__ == "__main__":
    while True:
        roll_dice()
        again = input("\nRoll again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing! 🎉")
            break
