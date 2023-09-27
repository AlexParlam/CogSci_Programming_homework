import random #to make randome function below

# we create the bank of words for haiku
nouns = ["moon", "cat", "flower", "tree", "rain", "ocean", "mountain", "bird", "star", "river"]
adjectives = ["silent", "gentle", "lonely", "vivid", "distant", "serene", "majestic", "fragrant", "radiant", "mystic"]
verbs = ["whispers", "sleeps", "blossoms", "dances", "falls", "sparkles", "soars", "sings", "glistens", "envelops"]


def main():
    print("welcome to the Haiku generator")
    print("if you duno what is Haiku press 1, if you want Haiku press 2")
    instruciton = input("your answer: ")
    if instruciton == "1":
        print("A haiku is a traditional form of Japanese poetry that consists of three lines with a syllable pattern of 5-7-5. It typically focuses on capturing a brief moment in nature, conveying deep emotions, or evoking a sense of contemplation. Haikus often emphasize simplicity, clarity, and the beauty of the natural world.")
    elif instruciton == "2":
        print("")
        haiku = generate_haiku()
        for line in haiku:
            print(line)           
    else:
        print("please check instructions again :) ")


def generate_haiku(): #generating haiku
    line1 = random.choice(adjectives) + " " + random.choice(nouns)
    line2 = random.choice(adjectives) + " " + random.choice(verbs) + " " + random.choice(nouns)
    line3 = random.choice(adjectives) + " " + random.choice(nouns)
    
    return line1, line2, line3


main()