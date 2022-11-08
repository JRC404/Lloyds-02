# # lists.py

# favourite_artists = ["Miley Cyrus", "Lady Gaga", "James Blunt", "Lewis Capaldi"]
# #                           0           1               2               3
# print(favourite_artists[0]) # first item
# print(favourite_artists[1]) # second item
# print(favourite_artists[2]) # third item
# print(favourite_artists[3]) # fourth item

# print("--------------")

# favourite_artists[0] = "Hannah Montana"
# print(f"First item: {favourite_artists[0]}") # first item
# print(f"Second item: {favourite_artists[1]}") # second item

# print("--------------")

# # To add to a list... we use the keyword "append"
# favourite_artists.append("Queen")
# favourite_artists.append("F.U.N")
# print(favourite_artists)

# print("--------------")
# # To remove... it couldn't be easier :-)
# favourite_artists.remove("Queen")
# # favourite_artists.remove("Mickey Bubble") # ValueError: list.remove(x): x not in list -> this means Mickey Bubble does not exist inside of the list
# print(favourite_artists)

# print("--------------")
# # To remove a specific index value... we use pop()
# favourite_artists.pop(1)
# print(favourite_artists)

# print("--------------")
# # sort and reverse sort our list
# favourite_artists.sort()
# print(favourite_artists)
# print("--------------")
# favourite_artists.reverse()
# print(favourite_artists)
# print("--------------")

# instead of pop, you can use del to remove at a specific index
# del favourite_artists[0]

# try not to do this one... unless you're sure!
# del favourite_artists
# this deletes the whole list

# if you just want to clear the list but have it still exist...
# favourite_artists.clear() # cleat the items from the list

# TODO: Create a list of either favourite cars, favourite shows, favourite companies etc...
#? 5 items to start with
#? Add 3 items using append()
#? Remove 2 items from the back of the list
#? Remove the 2nd index from the list using pop()
#? Sort in reverse order
#? print the entire list

favourite_shows = ["B99", "The Office US", "Suits", "Other show", "Another show"]

print("--------")
print(favourite_shows)
print("--------")

favourite_shows.append("Parks and Rec") # adding Parks and Rec to the end of the list
print(favourite_shows)
print("--------")

favourite_shows.append("Family Guy") # adding Family Guy to the end of the list
print(favourite_shows)
print("--------")
favourite_shows.append("I'm a Celeb") # Adding I'm a Celeb to the end of the list
print(favourite_shows)
print("--------")

favourite_shows.pop(7) # Remove I'm a Celeb
# favourite_shows.remove("I'm a Celeb")
print(favourite_shows)
print("--------")

favourite_shows.pop(6) # Remove Family Guy
print(favourite_shows)
print("--------")

favourite_shows.pop(1) # Remove The Office US
print(favourite_shows)
print("--------")

favourite_shows.reverse()
# What will be the result here?
print(favourite_shows)