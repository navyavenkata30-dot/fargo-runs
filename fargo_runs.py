import time
import random

def start_game():
    print("\n🏃 Welcome to FARGO RUNS 🏃")
    print("A Dungeon Runner with 10 Levels")
    print("Phases: Dark Black ▓, Medium Black ▒, Light Black ░")
    print("Character: ⚪ (White Player)")
    print("Medikits ❤️, Inhalers 💨, Grenades 💣 available")
    input("\nPress ENTER to start your run...")

def play_level(level):
    print(f"\n===== LEVEL {level} =====")
    phases = ["Dark Black ▓", "Medium Black ▒", "Light Black ░"]
    
    for phase in phases:
        print(f"\nEntering phase: {phase}")
        time.sleep(1.5)
        
        # Random events
        event = random.choice(["medikit", "inhaler", "grenade", "enemy", "nothing"])
        if event == "medikit":
            print("👉 You found a ❤️ Medikit!")
        elif event == "inhaler":
            print("👉 You found a 💨 Inhaler!")
        elif event == "grenade":
            print("👉 You found a 💣 Grenade!")
        elif event == "enemy":
            print("⚔️ Enemy attacks! You fight back and survive!")
        else:
            print("...Empty hallway, keep running.")
        time.sleep(1)

    print(f"\n✅ LEVEL {level} COMPLETED! 📞 A phone rings... unlocking next level!")

def fargo_runs():
    start_game()
    for lvl in range(1, 11):  # 10 levels
        play_level(lvl)
    print("\n🎉 YOU WON! All 10 levels of FARGO RUNS completed! 🎉")

if __name__ == "__main__":
    fargo_runs()

