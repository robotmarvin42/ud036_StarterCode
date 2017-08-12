# Class for video content
# This class provides variable for the movie class,
# and demonstrates nested classes.


class Video():
    """The base class for video records"""

    # Class Variables
    VIEWER_RATING = [1, 2, 3, 4, 5]  # 1 = Hate it. 5 = Love it.

    # init definition with base, unique attributes
    def __init__(self, title, VIEWER_RATING, length, comments):
        self.title = title
        self.rating = VIEWER_RATING
        self.length = length
        self.comments = comments

    # Append comments to comment field. Functionality to be
    # added to website at later time.
    def add(self, comment):
        self.comments.append(comment)
