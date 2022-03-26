
import imdb #import the IMDB module

class ImdbRating(): # class for IMDB rating 

  #method to find the rating of the movie based on the movie code
  def findRating(self, movieName): 
    im = imdb.IMDb() #create object of the IMDb method

    foundMovie = im.search_movie(movieName) #search for the movie
    
    print('Following are the Movie ids associated with the movies ')
    for movie in foundMovie:
      print(movie, "--->", movie.movieID) # print the movies with common names found in the search

    mCode = input('Please enter the movie code from the above list: ')

    movieCode = im.get_movie(mCode)
    print("'Rating of the movie is: {}".format(movieCode.data['rating']))

  def enterMovie(self):
    movieName = input('Enter the movie name:')
    self.findRating(movieName)

obj = ImdbRating() #create the object of ImdbRating class
obj.enterMovie()
