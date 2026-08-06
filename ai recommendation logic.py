recommendations = {
    "technology": [
        "Learn Python Programming",
        "Artificial Intelligence Basics",
        "Web Development Bootcamp",
        "Data Structures and Algorithms"
    ],

    "sports": [
        "Football Training",
        "Cricket Coaching",
        "Basketball Skills",
        "Badminton Practice"
    ],

    "music": [
        "Learn Guitar",
        "Piano for Beginners",
        "Music Production",
        "Singing Classes"
    ],

    "movies": [
        "Inception",
        "Interstellar",
        "The Dark Knight",
        "Avengers: Endgame"
    ],

    "books": [
        "Atomic Habits",
        "Rich Dad Poor Dad",
        "The Alchemist",
        "Think and Grow Rich"
    ],

    "gaming": [
        "Minecraft",
        "Valorant",
        "Free Fire",
        "PUBG"
    ],

    "fitness": [
        "Morning Workout",
        "Yoga Basics",
        "Home Cardio",
        "Strength Training"
    ]
}


def show_categories():
    print("\nAvailable Categories:")
    for category in recommendations:
        print("-", category)


def recommend():
    print("=" * 45)
    print("      AI Recommendation System")
    print("=" * 45)

    show_categories()

    user_input = input("\nEnter your interests (comma separated): ")
    interests = user_input.lower().split(",")

    found = False

    print("\nRecommended Items:")
    print("-" * 30)

    for interest in interests:
        interest = interest.strip()

        if interest in recommendations:
            found = True
            print("\nBased on:", interest.capitalize())

            for item in recommendations[interest]:
                print("->", item)

    if not found:
        print("Sorry, no recommendations found.")
        print("Try categories shown above.")


def main():
    while True:
        recommend()

        choice = input("\nDo you want another recommendation? (yes/no): ")

        if choice.lower() != "yes":
            print("\nThank you for using the AI Recommendation System.")
            break


main()