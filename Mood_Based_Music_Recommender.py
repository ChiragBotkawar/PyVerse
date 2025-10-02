import random

def recommend_songs(mood):
    playlists = {
        "happy": [
            "Happy - Pharrell Williams (Hollywood)",
            "Can't Stop the Feeling - Justin Timberlake (Hollywood)",
            "Good Vibrations - Beach Boys (Hollywood)",
            "Badtameez Dil - Yeh Jawaani Hai Deewani (Bollywood)",
            "Gallan Goodiyan - Dil Dhadakne Do (Bollywood)",
            "Kar Gayi Chull - Kapoor & Sons (Bollywood)"
        ],
        "sad": [
            "Someone Like You - Adele (Hollywood)",
            "Fix You - Coldplay (Hollywood)",
            "Stay With Me - Sam Smith (Hollywood)",
            "Channa Mereya - Ae Dil Hai Mushkil (Bollywood)",
            "Tujhe Kitna Chahne Lage - Kabir Singh (Bollywood)",
            "Agar Tum Saath Ho - Tamasha (Bollywood)"
        ],
        "angry": [
            "Break Stuff - Limp Bizkit (Hollywood)",
            "Killing in the Name - Rage Against The Machine (Hollywood)",
            "Bodies - Drowning Pool (Hollywood)",
            "Bhaag D.K. Bose - Delhi Belly (Bollywood)",
            "Jai Jai Shivshankar - War (Bollywood)",
            "Malhari - Bajirao Mastani (Bollywood)"
        ],
        "relaxed": [
            "Weightless - Marconi Union (Hollywood)",
            "Sunset Lover - Petit Biscuit (Hollywood)",
            "Clair de Lune - Debussy (Hollywood)",
            "Kabira - Yeh Jawaani Hai Deewani (Bollywood)",
            "Ilahi - Yeh Jawaani Hai Deewani (Bollywood)",
            "Tera Yaar Hoon Main - Sonu Ke Titu Ki Sweety (Bollywood)"
        ],
        "motivated": [
            "Eye of the Tiger - Survivor (Hollywood)",
            "Stronger - Kanye West (Hollywood)",
            "Don't Stop Me Now - Queen (Hollywood)",
            "Zinda - Bhaag Milkha Bhaag (Bollywood)",
            "Apna Time Aayega - Gully Boy (Bollywood)",
            "Kar Har Maidan Fateh - Sanju (Bollywood)"
        ]
    }

    if mood in playlists:
        print(f"\n🎵 Here are some {mood} songs for you:\n")
        for song in random.sample(playlists[mood], 5):  # random 5 songs
            print(f"- {song}")
    else:
        print("😕 Mood not recognized. Try: happy, sad, angry, relaxed, or motivated.")

def main():
    print("🎧 Welcome to the Mood-Based Music Recommender! 🎧")
    mood = input("How are you feeling today? ").lower()
    recommend_songs(mood)

if __name__ == "__main__":
    main()
