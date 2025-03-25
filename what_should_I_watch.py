import random
file_name = 'Animelist.md'
mode = 'r'

anime_list = []

with open(file_name, mode) as file:
    lines = file.readlines()
    for line in lines[2:]:
        anime_serie = line.strip("\n | ").split("|")
        anime_serie = [element.strip() for element in anime_serie ]
        anime_list.append(anime_serie)

print("What mood are you in right now?")
mood = input("Enter your mood: ")
matching_anime = [anime[0] for anime in anime_list if anime[2] == mood ]
if matching_anime:
                                                                                            # print(f"{mood} anime: {', '.join(matching_anime)}")
    print(f"Matches Anime: {len(matching_anime)}")
    random_anime = random.choice(matching_anime)
    print(f"I have a suggestion: {random_anime}")
    reroll_answer = input("Would you like to watch this anime? (Press enter for another suggestion)")
    while reroll_answer != "yes":
        matching_anime.remove(random_anime)
        print(f"Matches Anime: {len(matching_anime)}")
        if not matching_anime:
            print("I'm sorry, I couldn't find any more anime in your mood right now")
            break
        random_anime = random.choice(matching_anime)
        print(random_anime)
        reroll_answer = input("Would you like to watch this anime? (Press enter for another suggestion)")  
else:
    print(f"I'm sorry, I couldn't find any anime in your mood right now '{mood}'. ")  
    