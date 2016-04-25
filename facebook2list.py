#Kivy Imports
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

#Regular Imports
from os.path import isfile


class MainWindow(GridLayout):
    def __init__(self):
        super(MainWindow, self).__init__(self)

	def parse(self):
		text = self.ids.post.text
	    pass #when I see how the post looks I will continue this, should return a string

	def update(self):
		if isfile("fb_posts.txt"):
			f = open("fb_posts.txt", 'r+')
	    else:
            f = open("fb_posts.txt", "w+")

        f.write(self.parse())
        f.close()


class Facebook2listApp(App):
    def build(self):
        return MainWindow()