# A set of examples to demonstrate using APIs ( application programmed interfaces )
# See http://apislist.com for more examples

# import libraries
# mylib is your own personal library of functions, which you create
import libs_chris as lib


#get random user from randomuser.me
# use our own lib function


print ("######## people ########")
response = lib.get_url("https://randomuser.me/api/")

# we receive an array of data, so only process the first entry
json = response.json()['results'][0]

#print name and the picture information from the data
print(json["name"],json['picture'])

#use mylib to get data about astronausts in space
print("######## Astronausts in space #########")
response = lib.get_url("http://api.open-notify.org/astros")

#print the information
print(response.json())

#get movie information
print("######## Movie ########")
).json()

# create empty lists to save the results
Popularity = []
Vote_count = []
Orignal_lang = []
Titles = []
Vote_avg = []
Overview = []
Release_Data = []

for i in response['results']:
 
    #collect all the titles into 1 list
    # append() adds the title to the list of Titles
    Titles.append(i['title'])

    
    Popularity.append(i['popularity'])
    Vote_count.append(i['vote_count'])
    Orignal_lang.append(i['original_language'])

    Vote_avg.append(i['vote_average'])
    Overview.append(i['overview'])
    Release_Data.append(i['release_date'])

print(Titles)

#get some harry potter characters
#response = mylib.get_url("https://api.potterdb.com/v1/characters")
#print(response.json())

# get taylor swift lyrics
url = "https://songsexcerpt.mohd.app/api/v1/getRandomExcerpt?artists=597"
x = 2
for i in range(x):
    response = lib.get_url(url)
    print(response.json())





