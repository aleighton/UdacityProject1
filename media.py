import webbrowser


class Movie():
    """Constructor for Class Movie
    Takes 5 arguments:
    self
    movie_title --- supplied as a string
    movie_storyline --- supplied as a string
    poster_image --- should be supplied as a url
    trailer_youtube --- should be supplied as a url

    show_trailer() is a class method of Movie.
    The youtube url supplied to the constructor
    is passed to the method and a browser window is opened with the link.

    """
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
