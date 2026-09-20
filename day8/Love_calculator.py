def calculate_love_score(name1, name2):
        combined_names = name1 + name2

        score1 = 0
        for char in 'TRUE':
            # print(f"{char} : {combined_names.lower().count(char.lower())}")
            score1 += combined_names.lower().count(char.lower())

        score2 = 0
        for char in 'LOVE':
            score2 += combined_names.lower().count(char.lower())

        print(int(str(score1) + str(score2)))


# print(calculate_love_score("Angela Yu", "Jack Bauer"))
calculate_love_score("Kanye West", "Kim Kardashian")










# name1 = "John"
# name2 = "Doeeeee"
# combined_names = name1 + name2
# score2 = 0
# for char in 'LOVE':
#     score2 += combined_names.lower().count(char.lower())

# print(score2)