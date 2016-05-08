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
		text = self.ids.post.text.split('\n')
	    output = []
        output[0] = (text[0], [line for line in text[2:text.index('LikeShow more reactions\n')]], text[1])
        i = text.index('LikeShow more reactions\n')
        while i < len(text):






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