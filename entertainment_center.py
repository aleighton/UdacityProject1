import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story about a boy and his toys who come to life", "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg", "https://youtu.be/KYz2wyBy3kc")
avatar = media.Movie("Avatar", "A marine on an alien planet, gets frisky with a local, blows up some shit", "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg","https://youtu.be/5PSNL1qE6VY")
inception = media.Movie("Inception", "a onioned dreamscape of french horn sounds", "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg", "https://youtu.be/d3A3-zSOBT4")
#print(toy_story.storyline)
#avatar.show_trailer()
movies = [toy_story, avatar, inception]
fresh_tomatoes.open_movies_page(movies)
