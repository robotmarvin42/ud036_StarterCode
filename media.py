#This class defines movies and their attributes
import webbrowser
from video import Video

class Movie(Video):
    """This class provides a way to store movie related information"""
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__ (self, title, VIEWER_RATING, length, comments, VALID_RATINGS, movie_storyline, poster_image, trailer_youtube): 
        Video.__init__(self, title, VIEWER_RATING, length, comments)
        self.movie_rating = VALID_RATINGS
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    

