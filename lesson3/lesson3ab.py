''' lesson 3 - building a movie website
build a site that hosts movie trailers and their info

steps:
    1. uses classes to make a movie blueprint
        should contain
            title
            yt_trailer
            storyline
            poster
            revies
    2. create show_trailer method
        should allow us to avatar.show_trailer() which uses yt_trailer
    3. create an html page which loads this data and allows user to click
        picture to go to trailer 


how do you design a class?
    for class movie, we know we need a title, yt_trailer and storyline at least
    it is good practice to define classes in a separate file

__init__(self)
    a constructor function
    always takes self, which is the obj being created
        brad = turtle.Turtle()      # brad is self

__doc__
    displays the docstring for the class

VOCABULARY
    Class
        ex: Movie()
        class keyword allows us to make classes
        can have data and methods/functions
    Instance
        ex: avatar, toy_story
        each of these objs have memory space for the obj's vars
    Instance Variables
        vars unique to an obj
        can be called by using self.varName defined w/in the class definition
    Instance Methods
        functions defined w/in a class definition
    Constructor
        __init__ method is called when an obj is initialized

    Class Variables
        variables defined for an entire class
        __name__
        __doc__
        __module__
    Inheritance
        class New(Old)  # class New inherits code from class Old
        Method overriding allows a subclass to have a method of the same name
            as one within the parent class

    
'''
import webbrowser
import fresh_tomatoes

def main():

    toy_story = Movie("Toy Story",
            "A story of a boy's toys",
            "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
            "https://www.youtube.com/watch?v=fPhse4WlgEA")
    
    avatar = Movie("Avatar",
            "Pocahontas in Space",
            "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
            "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
    
    school_of_rock = Movie("School of Rock",
            "Bum who shouldn't be teaching kids holds kids back an entire year",
            "",
            "")

    ratatouille = Movie("Ratatouille",
            "Boy who can't cut it as a chef hallucinates about a rat that can",
            "",
            "")

    midnight_in_paris = Movie("Midnight in Paris",
            "Hipster who can't be happy pretends love is a thing of the past",
            "",
            "")

    hunger_games = Movie("The Hunger Games",
            "Hot girl in the country is forced to babysit for her  own survival",
            "",
            "")

    # here we use instructor-provided fresh_tomatoes.py
    # this has a func open_movies_page() which takes in a list of movies and 
        # returns an html page with their pics, info and trailer links
    movies_array = [avatar, toy_story, ratatouille, school_of_rock,
            midnight_in_paris, hunger_games]

    # fresh_tomatoes.open_movies_page(movies_array)

class Video():
    def __init__(self, title, duration):
        self.title      = title
        self.duration   = duration

class Movie(Video):
    """ This class provides a blueprint for basic movie-related information"""

    # capitalized b/c Google says so, used: Movie.MPAA_RATINGS
    MPAA_RATINGS = ["G", "PG", "PG-13", "R", "NC-17"]

    # double underscores mean init is a reserved keyword
    def __init__(self, movie_title, movie_storyline, duration, poster_url, yt_trailer):
        Video.__init__(movie_title, duration)
        self.storyline      = movie_storyline
        self.poster_url     = poster_url
        self.yt_trailer_url = yt_trailer

    def show_trailer(self):
        """Opens a browser and shows the movie's trailer on YouTube"""
        webbrowser.open(self.yt_trailer_url)

class TVShowEpisode(Video):
    def __init__(self, title, duration, season, episode, tv_station)
        Video.__init__(title, duration)
        self.season     = season
        self.episode    = episode
        self.tv_station = tv_station

    def get_local_listing():
        


if __name__ == "__main__":
    main()
