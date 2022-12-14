from tkinter import *
from Model.Model import Model
from View.View import View
from Controller.Controller import Controller

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter MVC Demo')

        #create a model
        model = Model('hello@pythontutorial.net')

        # create a view and place it on the root window
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # create a controller
        controller = Controller(model, view)

        # set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()