#imports
import media
import fresh_tomatoes

#----------------------------------------------------------------------------------------------------------------

#For reference, to create a movie, list: Title of the Movie, Viewer's Rating, Length (minutes), comments, Rating, What the movie is about, Poster, and Trailer

#Movie 1
rogue_one = media.Movie("Rogue One",
                        1,
                        161,
                        "Rouge 1 Comment",
                        "PG-13",
                        "How the rebels got the Death Star plans",
                        "http://alienbee.net/wp-content/uploads/2016/07/rogue-one-poster.jpg",
                        "https://www.youtube.com/watch?v=frdj1zb9sMY")
#Movie 2
boondock = media.Movie("Boondock Saints",
                        2,
                        162,
                        "Boondock Comment",
                        "R",
                        "Two brothers think they're righteous",
                        "http://www.movieposter.com/posters/archive/main/100/MPW-50330",
                        "https://www.youtube.com/watch?v=ydXojYfCF3I")

#Movie 3
matrix = media.Movie("Matrix",
                        3,
                        163,
                        "Matrix Comment",
                        "PG-13",
                        "A hacker wakes up to reality",
                        "http://2.bp.blogspot.com/-2F8gEE3lENI/UEFvWy-MCLI/AAAAAAAAMkA/P5O9gKXKLbs/s1600/The+Matrix+(1999)+1.jpg",
                        "https://www.youtube.com/watch?v=m8e-FF8MsqU")

#Movie 4
memento = media.Movie("Memento",
                        4,
                        164,
                        "Rouge 1 Comment",
                        "R",
                        "How to solve a murder with a 5 minute memory",
                        "https://13movies.files.wordpress.com/2014/01/memento-poster.jpg",
                        "https://www.youtube.com/watch?v=0vS0E9bBSL0")

#Movie 5
fight_club = media.Movie("Fight Club",
                        5,
                        165,
                        "Rouge 1 Comment",
                        "R",
                        "The first two rules prohibit me answering this question",
                        "http://www.flore-maquin.com/wp-content/uploads/Fight_club_RVB_72.jpg",
                        "https://www.youtube.com/watch?v=SUXWAEX2jlg")

#Movie 6
snatch = media.Movie("Snatch",
                        5,
                        166,
                        "Snatch Comment",
                        "R",
                        "Oh the places a diamond will go!",
                        "http://images.moviepostershop.com/snatch-movie-poster-2001-1020274908.jpg",
                        "https://www.youtube.com/watch?v=Q8jbt0wBkMI")

#Assigning all instances to an array.
movies = [rogue_one, boondock, matrix, memento, fight_club, snatch]

#Sending above array to fresh_tomatoes to generate website.
fresh_tomatoes.open_movies_page(movies)


#---------------------------------------------------
#Print statements to show all instance attributes are functional, instance attributes are unique, and class variable are used.
print(snatch.title) #Video Class
print(snatch.rating) #Video Class
print(snatch.length) #Video Class
print(snatch.comments) #Video Class
print(snatch.movie_rating) #Movie Class
print(snatch.storyline) #Movie Class
print(snatch.poster_image_url) #Movie Class
print(snatch.trailer_youtube_url) #Movie Class


