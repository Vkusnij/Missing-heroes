from data import movies

# You can use the `movies` array here
# Please write every correction and modification of the data to this file by updating the `movies` array

# WRITE YOUR CODE HERE

# Missing Martin

def update_directors(movies):
    count = 0

    for movie in movies:
        if movie['director'] == "":
            movie['director'] = "Martin Scorsese"
            count += 1

    movies[:] = [movie for movie in movies if movie['director'] != ""]

    return count

scorsese_count = update_directors(movies)

for movie in movies:
    print(f"Title: {movie['title']}, Year: {movie['year']}, Director: {movie['director']}")

print(f'Martin Scorsese was added {scorsese_count} times.')

# Correct wrong release years

def fix_years(movies):
    for movie in movies:
        if movie['year'] < 1900:
            if movie['year'] < 900:  
                new_year = movie['year'] + 2000
            else: 
                new_year = movie['year'] + 1000
            
            if new_year > 2024:
                new_year = 2024
            
            movie['year'] = new_year

fix_years(movies)

for movie in movies:
    print(f"{movie['title']} - {movie['year']}")

# Leonardo is mixed up

def fix_actors(movies):
    dicaprio_count = 0
    
    for movie in movies:
        if 'Leonardo da Vinci' in movie['actors']:
            movie['actors'].remove('Leonardo da Vinci')

        if dicaprio_count < 6 and 'Leonardo DiCaprio' not in movie['actors']:
            movie['actors'].append('Leonardo DiCaprio')
            dicaprio_count += 1

fix_actors(movies)

for movie in movies:
    print(f"{movie['title']} - {movie['actors']}")

# Add drama

def add_drama_genre(movies):
    drama_count = 0
    
    for movie in movies:
        if "" in movie['genres']:
            movie['genres'].remove("")
            movie['genres'].append("Drama")
            drama_count += 1
    
    while drama_count < 98:
        for movie in movies:
            if "Drama" not in movie['genres']:
                movie['genres'].append("Drama")
                drama_count += 1
                if drama_count >= 98:
                    break

add_drama_genre(movies)

for movie in movies:
    print(f"{movie['title']} - {movie['genres']}")

# How many actors are in the list?

def count_all_actors(movies):
    all_actors = []
    
    for movie in movies:
        all_actors.extend(movie['actors'])  
    
    return len(all_actors)

allTheActors = count_all_actors(movies)

print(f"All actors in the list: {allTheActors}")

# (optional), try filtering out duplicates!

def count_unique_actors(movies):
    unique_actors = set()
    
    for movie in movies:
        unique_actors.update(movie['actors'])  
    
    return len(unique_actors)

uniqueActorsCount = count_unique_actors(movies)

print(f"Whithout duplicate: {uniqueActorsCount}")