song={
"name_of_the_song" : "memories", 
"artist" : "maroon 5",
"album" : "memories",   
"released" : 2019,	   
"genre" : "pop"  
}

for key in song:
    print(key, ":", song[key])

def askQuestion(key,value):
    if key and value:
        if key in song and song[key] == value:
            return True 
    return False
print(askQuestion("artist","maroon 5"))
print(askQuestion("released",2020))


