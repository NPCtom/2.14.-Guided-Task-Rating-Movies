#Movie Ratings
#2 Mar 2022
#Copyright 2022 Winz Tom

from tkinter import *
from tkinter.scrolledtext import *
class Movie:
  def __init__(self, name):
    self.name = name
    self.rating = "No Rating" # default setting

class MovieRater:
  def __init__(self, parent):
    # make a list of Movie objects
    movie_names = ["The Hobbit", "SkyFall", "Any movie with Adam Sandler in it",
"Monsters Inc", "The Incredibles", "King Kong", "The Avengers",
"Thor", "Captain America"]
    self.movies = []
    for m in movie_names:
       movie = Movie(m)
       self.movies.append(movie)

    # index will be used for keeping track of current movie in movies list
    self.index = 0
    #GUI set up
    self.rating_var = StringVar()
    self.rating_var.set("No Rating") # initial setting rating radiobuttons

    self.search_var = StringVar()
    self.search_var.set("*") # initial setting search radiobuttons : no valid value, so none set
    self.rating_frame = Frame(parent, width = 350, height = 320, bg = "chartreuse")
    self.rating_frame.grid_propagate(0) # to reserve space required for frame
    self.summary_frame = Frame(parent, width = 350, height = 320, bg = "orchid")
    self.summary_frame.grid_propagate(0)
    # widgets for summary_frame
    # This is being placed in the same position as the rating frame
    # The call to show_rating_frame at the end of init will sort this out.
    self.summary_frame.grid(row = 0, columnspan = 6, padx = 50)
    self.summ_label = Label(self.summary_frame, bg = "orchid", wraplength = 280)
    self.scrolled_display = ScrolledText(self.summary_frame, width = 30, height = 10)
    self.rating_btn = Button(self.summary_frame, text = "Back to Rating",
    command = self.show_rating_frame)
    self.summ_label.grid(row = 0, column = 0,padx = 20, sticky = W)
    self.scrolled_display.grid(row = 1, column = 0, sticky = W, padx = 20,pady = 20)
    self.rating_btn.grid(row = 2, column = 0, sticky = SE, padx = 20, pady = 20)
    # widgets for rating_frame
    # This is being placed in the same position as the summary frame
    # The call to show_rating_frame at the end of init will sort this out.
    self.rating_frame.grid(row = 0, columnspan = 6, padx = 50)
    movie_label = Label(self.rating_frame, text = "Please Rate: ", bg = "chartreuse")
    movie_label.grid(row = 0, column = 0, sticky = W, padx = 25, pady = 10)
    self.current_movie = Label(self.rating_frame, wraplength = 100, height = 3,
    text = self.movies[self.index].name, bg = "chartreuse")
    self.current_movie.grid(row = 0, column = 1, sticky = W)
    rating_label = Label(self.rating_frame, text = "Your rating: ", bg = "chartreuse")
    rating_label.grid(row = 1, column = 0, sticky = W, padx = 25)
    self.rb0 = Radiobutton(self.rating_frame, text = "No Rating", value = "No Rating",
    variable = self.rating_var, command = self.enter_rating, bg = "chartreuse")
    self.rb1 = Radiobutton(self.rating_frame, text = "Forget it", value = "Forget it",
    variable = self.rating_var, command = self.enter_rating, bg = "chartreuse")
    self.rb2 = Radiobutton(self.rating_frame, text = "2", value = "2",
    variable = self.rating_var, command = self.enter_rating, bg = "chartreuse")
    self.rb3 = Radiobutton(self.rating_frame, text = "3", value ="3",
    variable = self.rating_var, command = self.enter_rating, bg = "chartreuse")
    self.rb4 = Radiobutton(self.rating_frame, text = "4", value ="4",
    variable = self.rating_var, command = self.enter_rating, bg = "chartreuse")
    self.rb5 = Radiobutton(self.rating_frame, text = "Must See", value = "Must See",
    variable = self.rating_var, command = self.enter_rating, bg = "chartreuse")
    self.rb0.grid(row = 1, column = 1, sticky = W)
    self.rb1.grid(row = 2, column = 1, sticky = W)
    self.rb2.grid(row = 3, column = 1, sticky = W)
    self.rb3.grid(row = 4, column = 1, sticky = W)
    self.rb4.grid(row = 5, column = 1, sticky = W)
    self.rb5.grid(row = 6, column = 1, sticky = W)
    self.previous_btn = Button(self.rating_frame, text = "Previous", underline = 0,
    command = self.previous_movie)
    self.previous_btn.grid(row = 7, column = 0, sticky = SW, padx = 50, pady = 10)
    self.next_btn = Button(self.rating_frame, text = "Next", underline = 0, width = 7,
    command = self.next_movie)
    self.next_btn.grid(row = 7, column = 1, sticky = SW, padx = 50, pady = 10)
    # widgets for searching
    self.search_label = Label(parent, text = "Search for movies with a rating of:")
    self.search_label.grid(row = 1, columnspan = 6)
    self.rba = Radiobutton(parent, text = "No Rating",value = "No Rating",
    variable = self.search_var, command = self.show_search_results)
    self.rbb = Radiobutton(parent, text = "Forget it", value = "Forget it",
    variable = self.search_var, command = self.show_search_results)
    self.rbc = Radiobutton(parent, text = "2", value ="2", variable = self.search_var,
    command = self.show_search_results)
    self.rbd = Radiobutton(parent, text = "3", value ="3", variable = self.search_var,
    command = self.show_search_results)
    self.rbe = Radiobutton(parent, text = "4", value = "4", variable = self.search_var,
    command = self.show_search_results)
    self.rbf = Radiobutton(parent, text = "Must See", value = "Must See",
    variable = self.search_var,command = self.show_search_results)
    self.rba.grid(row = 2, column = 0, padx = 5)
    self.rbb.grid(row = 2, column = 1, padx = 5)
    self.rbc.grid(row = 2, column = 2, padx = 5)
    self.rbd.grid(row = 2, column = 3, padx = 5)
    self.rbe.grid(row = 2, column = 4, padx = 5)
    self.rbf.grid(row = 2, column = 5, padx = 5)
    # This removes the summary frame and ensures the rating frame is in place on the grid
    self.show_rating_frame()
  def enter_rating(self):
    """ store movie rating in Movie object at current index of movies list """
    self.movies[self.index].rating = self.rating_var.get()


  def next_movie(self):
    self.index += 1 # keep a track of which Movie in the list we are looking at
    #update movie name

    if(self.index >= len(self.movies)): self.index = 0

    self.current_movie.configure(text = self.movies[self.index].name)
    # update the rating radiobutton showing as selected
    self.rating_var.set(self.movies[self.index].rating)


  def previous_movie(self):
    self.index -= 1 # keep a track of which Movie in the list we are looking at
    #update movie name

    if(self.index < 0): self.index = len(self.movies)-1

    self.current_movie.configure(text = self.movies[self.index].name)
    # update the rating radiobutton showing as selected
    self.rating_var.set(self.movies[self.index].rating)

  def show_search_results(self):
    """ Removes the rating frame and grids the summary frame. Establishes the rating
 being searched and clears the scrolled display.The method then searches the
 list of movies for those with a rating matching the rating being searched for and
 inserts each title into the scrolled display"""
    self.rating_frame.grid_remove()
    self.summary_frame.grid()
    root.update_idletasks() # necessary on some Op. Systems to refresh the screen properly
    search_rating = self.search_var.get()

    self.scrolled_display.delete('1.0', END) # clear any previous content
    self.summ_label.configure(text = "You have given the following movies a rating of " +
    search_rating + ": ", bg = "plum")
    for m in self.movies:
      if m.rating == search_rating:
         self.scrolled_display.insert(END, m.name + "\n" )

  def show_rating_frame(self):
    """ Toggles back to the rating frame """
    self.summary_frame.grid_remove()
    self.rating_frame.grid() # return rating_frame to its original grid position
    root.update_idletasks() # to refresh the screen properly
    self.search_var.set("*")

#main routine
if __name__ == "__main__":
 root = Tk()
 root.title("Movie Ratings")
 rater = MovieRater(root)
 root.mainloop()
