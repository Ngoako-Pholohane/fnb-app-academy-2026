while True:
    score = input("Enter game score: ").strip().lower()

    if score == "stop":
        print("Game session ended!\n")
        break
    else:
        score = int(score)
        if score > 100:
            print("Wow! That’s a new high score!\n")
        else:
            print("Good try, keep playing\n")
