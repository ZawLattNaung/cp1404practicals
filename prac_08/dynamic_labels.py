from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def build(self):
        self.title = "Dynamic Labels Example"
        self.root = Builder.load_file('dynamic_labels.kv')

        # a list of names
        names = ["Zaw", "Wai", "Myo", "Min", "Khant"]

        #Add Label for each name
        for name in names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)

        return self.root


if __name__ == '__main__':
    DynamicLabelsApp().run()
