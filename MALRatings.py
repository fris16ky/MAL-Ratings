from bs4 import BeautifulSoup
from selenium import webdriver

#This code will be getting the names of the animes I've watched (have to be on MyAnimeList - which I routinely update), as well as what rating I gave them. 
#To this extent, I have/will be rating every Anime season (it goes by Season for shows that have finished a season - not One Piece!)
#Main idea is to rate every season of anime/anime as a whole when applicable, and then return a sorted output by rating 
#(All anime's I've rated 5/10, 6/10, and so on). 

#Website is https://myanimelist.net/animelist/Fris16ky

import unicodedata #To deal with accented characters like é and à
def normalize_string(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

#Create a new instance of the Chrome driver
driver = webdriver.Chrome()
#Navigate to my MyAnimeList page
driver.get("https://myanimelist.net/animelist/Fris16ky")

anime_list = []
anime_ratings = [] 

#Wait 10 seconds for the page to load
driver.implicitly_wait(10)
#Get the page source/all of it's code
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# Find all table body elements with class "list-item"
tbody_elements = soup.find_all("tbody", class_="list-item")

for tbody in tbody_elements:
    # Find the first table row element (class of list-table-data) to start taking the row's values!
    tr_element = tbody.find("tr", class_="list-table-data")
    if tr_element:
        # Find the table data element with class "data title clearfix" within the tr element
        td_title = tr_element.find("td", class_="data title clearfix")
        if td_title:
            #Find the anchor tag within the td element - the Names of each anime is the text of the Anchor tag. 
            anchor_tag = td_title.find("a")
            if anchor_tag:
                anime_name = anchor_tag.text.strip()
                anime_list.append({"Name": anchor_tag.text, "Rating": ""})
    
    #Find all ratings, still using tr_element (also under list-table-data)
    if tr_element: 
        td_score = tr_element.find("td", class_="data score")
        if td_score: 
            anc_tag = td_score.find("a")
            if anc_tag: 
                score = anc_tag.find("span")
                rating = score.text.strip()
                #append (add) anime rating to the dictionary located by Name
                for anime in anime_list: 
                    if anime["Name"] == anime_name: 
                        anime["Rating"] = rating

#Sort anime list by rating - the "== "-"" part is because that's what MAL puts for Un-rated Animes
sorted_anime_list = sorted(anime_list, key=lambda x: int(x["Rating"])  if x["Rating"].isdigit() else (0 if x["Rating"] == "-" else -1))


#Manually replacing Oshi No Ko to get rid of the brackets that MyAnimeList puts on it!
anime.update({'Name': "[Oshi No Ko]", 'Name': "Oshi No Ko"})

print("Here are all of my currently unrated anime: ", end="") #end is so that it doesn't print each name on a new line
unrated_anime_count = 0

#Dealing with the special/annoying characters (�)
for anime in sorted_anime_list: 
    #Normalize/replace non ASCII characters, (Pok�mon -> Pokmon), and then manually replacing Pokmon with Pokemon (accents not working, but that's fine!)
    normalized_name = normalize_string(anime["Name"])
    anime["Name"] = normalized_name.replace("Pokmon", "Pokémon") #Originally had the Stein's Gate Deja Vu here (Dj to Déjà), but that messed with Django, and the accents didn't show up anyways!
    
    #If it's an unrated anime, add to the count and specially format to add a comma for ease of reading
    if anime["Rating"] == "-":
        if unrated_anime_count > 0: #runs before the printing so that for the last name it won't print a comma after. Won't print a comma before the first name either since count = 0
            print(", ", end="")
        print(anime["Name"], end="")
        unrated_anime_count += 1
print("." if unrated_anime_count > 0 else "") #Printing this out last to add a period after the last anime. 

#Repeated block of code to print out the Names of Animes at each rating (1 through 10), or that I don't have any if applicable. 
print() 
print("1/10 Animes: ", end="")
one_anime_count = 0
for anime in sorted_anime_list: 
    if anime["Rating"] == "1": #one is the lowest rating
        if one_anime_count > 0: 
            print(", ", end="")
        print(anime["Name"], end="")
        one_anime_count += 1
print("." if one_anime_count > 0 else "I do not have any thankfully!")  

print()
print("2/10 Animes: ", end="")
two_anime_count = 0
for anime in sorted_anime_list: 
    if anime["Rating"] == "2":
        if two_anime_count > 0: 
            print(", ", end="")
        print(anime["Name"], end="")
        two_anime_count += 1    
print("." if two_anime_count > 0 else "I do not have any thankfully!") 

print()
print("3/10 Animes: ", end="")
three_anime_count = 0
for anime in sorted_anime_list: 
    if anime["Rating"] == "3":
        if three_anime_count > 0: 
            print(", ", end="")
        print(anime["Name"], end="")
        three_anime_count += 1
print("." if three_anime_count > 0 else "I do not have any thankfully!") 

print()
print("4/10 Animes: ", end="")
four_anime_count = 0
for anime in sorted_anime_list: 
    if anime["Rating"] == "4":
        if four_anime_count > 0:
            print(", ", end="")
        print(anime["Name"], end="")
        four_anime_count += 1
print("." if four_anime_count > 0 else "I do not have any thankfully!") 

print()
print("5/10 Animes: ", end="")
five_anime_count = 0
for anime in sorted_anime_list: 
    if anime["Rating"] == "5":
        if five_anime_count > 0: 
            print(", ", end="")
        print(anime["Name"], end="")
        five_anime_count += 1
print("." if five_anime_count > 0 else "I do not have any thankfully!") 

print()
print("6/10 Animes: ", end="")
six_anime_count = 0
for anime in sorted_anime_list: 
    if anime["Rating"] == "6":
        if six_anime_count > 0: 
            print(", ", end="")
        print(anime["Name"], end="")
        six_anime_count += 1
print("." if six_anime_count > 0 else "I do not have any thankfully!") #last else here, since I definitely have animes rated 7-10. 

print()
print("7/10 Animes: ", end="")
seven_anime_count = 0
for anime in sorted_anime_list: 
    if anime["Rating"] == "7":
        if seven_anime_count > 0: 
            print(", ", end="")
        print(anime["Name"], end="")
        seven_anime_count += 1
print("." if seven_anime_count > 0 else "")  

print()
print("8/10 Animes: ", end="")
eight_anime_count = 0
for anime in sorted_anime_list: 
    if anime["Rating"] == "8":
        if eight_anime_count > 0: 
            print(", ", end="")
        print(anime["Name"], end="")
        eight_anime_count += 1
print("." if eight_anime_count > 0 else "") 

print()
print("9/10 Animes: ", end="")
nine_anime_count = 0
for anime in sorted_anime_list: 
    if anime["Rating"] == "9":
        if nine_anime_count > 0: 
            print(", ", end="")
        print(anime["Name"], end="")
        nine_anime_count += 1
print("." if nine_anime_count > 0 else "") 

print()
print("10/10 PEAK Animes: ", end="")
ten_anime_count = 0
for anime in sorted_anime_list: 
    if anime["Rating"] == "10":
        if ten_anime_count > 0: 
            print(", ", end="")
        print(anime["Name"], end="")
        ten_anime_count += 1
print("." if ten_anime_count > 0 else "") 

print("\nHere are how many Anime I have per Rating: ")
print(f"1/10: {one_anime_count}, 2/10: {two_anime_count}, 3/10: {three_anime_count}, 4/10: {four_anime_count}, 5/10: {five_anime_count}, 6/10: {six_anime_count}, 7/10: {seven_anime_count}, 8/10: {eight_anime_count}, 9/10: {nine_anime_count}, 10/10: {ten_anime_count}")
