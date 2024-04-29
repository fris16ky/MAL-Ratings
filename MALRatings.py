from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

#This code will be getting the names of the animes I've watched (have to be on MyAnimeList), as well as what rating I gave them. 
#To this extent, I have/will be rating every Anime season (it goes by Season for shows that have finished a season - not One Piece!)
#I still have to go back and rate some of the early shows I watched and don't remember the specifics of what happened in the season
#(to get the most accurate rating), but yeah. 
#Main idea is to rate every season of anime/anime as a whole when applicable, and then return a sorted output by rating 
#(All anime's I've rated 5/10, 6/10, and so on). 

#Consider Adding in Manga? Or at least some shows that don't count on MAL (Arcane, Avatar come to mind)

#Website is https://myanimelist.net/animelist/Fris16ky

from selenium import webdriver
from selenium.webdriver.common.by import By

#Create a new instance of the Chrome driver
driver = webdriver.Chrome()
#Navigate to my MyAnimeList page
driver.get("https://myanimelist.net/animelist/Fris16ky")

anime_names = []
anime_ratings = [] #Could maybe use a dict instead? Like I did for the college project

#Wait 10 seconds for the page to load
driver.implicitly_wait(10)
#Get the page source/all of it's code
html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

# Find all tbody elements with class "list-item"
tbody_elements = soup.find_all("tbody", class_="list-item")

for tbody in tbody_elements:
    # Find the first tr element with class "list-table-data" within the tbody
    tr_element = tbody.find("tr", class_="list-table-data")
    if tr_element:
        # Find the td element with class "data title clearfix" within the tr element
        td_title = tr_element.find("td", class_="data title clearfix")
        if td_title:
            # Find the anchor tag within the td element and print its text
            anchor_tag = td_title.find("a")
            if anchor_tag:
                anime_name = anchor_tag.text.strip()
                anime_names.append({"Name": anchor_tag.text, "Rating": ""})
    
    #Find all ratings, still using tr_element (also under list-table-data)
    if tr_element: 
        td_score = tr_element.find("td", class_="data score")
        if td_score: 
            anc_tag = td_score.find("a")
            if anc_tag: 
                score = anc_tag.find("span")
                rating = score.text.strip()
                for anime in anime_names: 
                    if anime["Name"] == anime_name: 
                        anime["Rating"] = rating
        
print(anime_names)
#Works!



                
#Can't deal with special characters. i.e. é and à in deja vu and Pokemon. So it comes up with a question mark. Need to find a fix for that frfrfs
#BUT - we have the names of the shows. Now, just need to make/add them to a dictionary and do the sorting. Take the comments from this below code and 
#morph to this up here. Good ideas, but didn't work bc I ruined it by going one by one instead of all at once (find_all)                


# if tbody_element:
#     tr_elements = tbody_element.find_all("tr", class_="list-table-data")  # Find all tr elements with the specified class

#     for tr in tr_elements:
#         td_element = tr.find("td", class_="title")  # Find the td element with the specified class
#         if td_element:
#             #If the row has a title
#             anchor_tag = td_element.find_next_sibling("a")  # Find the next sibling anchor tag
#             if anchor_tag:
#                 #If there's a link under the 'title' td (table data) - which there should be/is for every item/anime - get the text and add it to the array for names
#                 anime_names.append(anchor_tag.text)  # Append the text of the anchor tag to the anime_names array after stripping whitespace

#and anchor_tag.text.strip() != "-" use this later for grabbing the actual score/seeing if there's a score yet. Maybe add a section (once I get this working D:) for
#anime's that I haven't rated yet!

#Not printing names

driver.quit()

# for name in anime_names: 
#     print(name)

#td className of data score. Has an anchor tag, then Span with class of 'score-label' followed by the score (i.e. 'score-label score-10')
#If it matters, before the td, there's a tr class of 'list-table-data', and tbody class of list-item

#This is how I got the anchor tags for all of the One Piece shows; can't use that in this case though
# elements = driver.find_elements(By.XPATH, '//a[contains(text(), "One Piece")]')
# for element in elements:
#     #Adding the links to the movie_links array; adding the string names to the movie_names array
#     movie_links.append(element.get_attribute("href"))
#     movie_names.append(element.text)
