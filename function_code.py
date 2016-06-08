# code to open and sort movie ratings list
with open("u.data", encoding="latin1") as movieratings:
    ratings_table = movieratings.read()
# user id | item id | rating | timestamp
ratings_list = ratings_table.split('\n')
ratingsrow_list = []
for row in ratings_list:
    row_list = row.split('\t')
    if row_list[0] != '':
        ratingsrow_list.append(row_list)

# code to open and sort movie information
with open("u.item", encoding="latin1") as movieinformation:
    information_table = movieinformation.read()
# movie id|title|releasedate|videodate|imdb|un|act|adv|ani|child|com|crim|doc|drama|fant|
# |f-noir|horror|mus|mys|rom|syfy|thril|war|west
information_list = information_table.split('\n')
inforow_list = []
for row in information_list:
    row_list = row.split('|')
    if row_list[0] != '':
        inforow_list.append(row_list)
for row in inforow_list:
    print(row[12])

# code to open and sort user information
with open("u.user", encoding="latin1") as userinformation:
    user_table = userinformation.read()
# userid | age | gender | occupation | zip code
user_list = user_table.split('\n')
finaluser_list = []
for row in user_list:
    row_list = row.split('|')
    if row_list[0] != '':
        finaluser_list.append(row_list)
raise Exception("Process void of error")
