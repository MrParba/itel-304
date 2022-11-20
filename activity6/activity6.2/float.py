from kivy.app import App
from kivy.lang import Builder


root = Builder.load_string('''
FloatLayout:
	canvas.before:
		Color:
			rgba: 0, 0, 255, 0.3
		Rectangle:
		    # self here refers to the widget i.e Floatlayout
		    pos: self.pos
		    size: self.size
	Button:
		text:'hello world'
		size_hint: .5, .5
		pos_hint: {'center_x' :.5, 'center_y': .5}
''')

class MainApp(App):

	def build(self):
		return root

if _name__== '__main_':
	MainApp().run()
