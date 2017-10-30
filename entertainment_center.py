import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story about a boy and his toys who come to life", "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg", "https://youtu.be/KYz2wyBy3kc")
avatar = media.Movie("Avatar", "A disabled marine on an alien planet, gets frisky with a local, blows up some stuff", "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg","https://youtu.be/5PSNL1qE6VY")
inception = media.Movie("Inception", "a onioned dreamscape of french horn sounds", "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg", "https://youtu.be/d3A3-zSOBT4")
love_actually = media.Movie("Love Actually", "A story around christmas, following a variety of relationships and exploring the different facets of Love","https://images-na.ssl-images-amazon.com/images/M/MV5BMTY4NjQ5NDc0Nl5BMl5BanBnXkFtZTYwNjk5NDM3._V1_UX182_CR0,0,182,268_AL_.jpg","https://youtu.be/fOS-HMiVejo")
five_hundred_days = media.Movie("500 Days of Summer", "An offbeat romantic comedy about a woman who doesn't believe true love exists, and the young man who falls for her.","https://images-na.ssl-images-amazon.com/images/M/MV5BMTk5MjM4OTU1OV5BMl5BanBnXkFtZTcwODkzNDIzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg","https://youtu.be/PsD0NpFSADM")
donnie_darko = media.Movie("Donnie Darko","A troubled teenager is plagued by visions of a man in a large rabbit suit who manipulates him to commit a series of crimes, after he narrowly escapes a bizarre accident.","https://images-na.ssl-images-amazon.com/images/M/MV5BZjZlZDlkYTktMmU1My00ZDBiLWFlNjEtYTBhNjVhOTM4ZjJjXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://youtu.be/rPeGaos7DB4")
#print(toy_story.storyline)
#avatar.show_trailer()
movies = [toy_story, avatar, inception, love_actually, five_hundred_days, donnie_darko]
fresh_tomatoes.open_movies_page(movies)
