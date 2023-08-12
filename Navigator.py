from PIL import Image, ImageTk
from io  import BytesIO

import base64
import tkinter as tk

class Navigator:
    '''
    The Navigator class provides an interactive slideshow for viewing a list of questions, charts, and code snippets. 
    It uses the tkinter library for its GUI to create a visually appealing interface for navigating through the analysis.

    Attributes:
        slides         (List[dict]) : A list of slides, each containing a title, question, chart, and code.
        current_index  (int)        : The index of the currently active slide.

    Methods:
        create_buttons    : Creates navigation buttons and binds the appropriate actions to them.
        update_display    : Updates the display to show the current question, chart, and code snippet.
        go_to_first       : Navigates to the first slide in the list.
        go_to_previous    : Navigates to the previous slide in the list.
        toggle_code       : Toggles the visibility of the code snippet.
        go_to_next        : Navigates to the next slide in the list.
        go_to_last        : Navigates to the last slide in the list.
        pack_components   : Packs the labels, chart, and buttons into the tkinter window.
        __call__          : Displays the initial slide and starts the tkinter main loop.
    '''

    def __init__(self, slides: list):
        self.slides        = slides
        self.current_index = 0

        self.root = tk.Tk()
        self.root.title('Analysis Navigator')
        self.root.configure(bg='black')

        self.frame                 = tk.Frame(self.root, bg   = "black")
        self.question_number_label = tk.Label(self.root, font = ("Menlo", 20, "bold"),   bg = "black", fg = "white")
        self.question_label        = tk.Label(self.root, font = ("Menlo", 14, "italic"), bg = "black", fg = "white")
        self.chart_label           = tk.Label(self.root, bg   = "black")
        self.code_text             = tk.Text(self.root,  wrap = tk.WORD, font = ("Courier New", 12), bg = "black", fg = "white")
        self.buttons               = self.create_buttons()

    def create_buttons(self):
        '''
        Creates navigation buttons and binds the appropriate actions to them. 
        The actions include navigating to the previous or next question, toggling code visibility, and jumping to the beginning or end.
        '''

        self.props = {"⇤" : {"side" : "left",  "key" : "<Up>",    "command" : self.go_to_first},
                      "←" : {"side" : "left",  "key" : "<Left>",  "command" : self.go_to_previous},
                      "↕" : {"side" : "left",  "key" : "<space>", "command" : self.toggle_code},
                      "⇥" : {"side" : "right", "key" : "<Down>",  "command" : self.go_to_last},
                      "→" : {"side" : "right", "key" : "<Right>", "command" : self.go_to_next}}

        buttons = []
        for k, v in self.props.items():
            self.root.bind(v['key'], lambda _, command = v['command']: command())
            button = tk.Button(self.frame if k == "↕" else self.root, 
                                text = k, font = ("Menlo", 30), command = v['command'], fg = "black")
            buttons.append(button)

        return buttons

    def update_display(self):
        '''
        Updates the display to show the current question, chart, and code snippet.
        '''

        current_slide = self.slides[self.current_index]

        self.question_number_label.config(text = current_slide['title'])
        self.question_label.config(text = current_slide['question'])

        # Decode the base64 image data
        image_data  = base64.b64decode(current_slide['chart'])
        image       = Image.open(BytesIO(image_data))
        photo_image = ImageTk.PhotoImage(image)

        self.chart_label.config(image = photo_image)
        self.chart_label.image = photo_image

        self.code_text.delete(1.0, tk.END)
        self.code_text.insert(tk.END, current_slide['code'])

    def go_to_first(self):
        '''
        Navigates to the first question in the list.
        '''

        self.current_index = 0
        self.update_display()

    def go_to_previous(self):
        '''
        Navigates to the previous question in the list.
        '''

        self.current_index = max(0, self.current_index - 1)
        self.update_display()

    def toggle_code(self):
        '''
        Toggles the visibility of the code snippet.
        '''

        if self.code_text.winfo_viewable():
            self.code_text.pack_forget()
        else:
            self.code_text.pack(fill = tk.BOTH, expand = True)

    def go_to_next(self):
        '''
        Navigates to the next question in the list.
        '''

        self.current_index = min(len(self.slides) - 1, self.current_index + 1)
        self.update_display()

    def go_to_last(self):
        '''
        Navigates to the last question in the list.
        '''

        self.current_index = len(self.slides) - 1
        self.update_display()

    def pack_components(self):
        '''
        Packs the labels, chart, and buttons into the tkinter window.
        '''

        self.question_number_label.pack()
        self.question_label.pack()
        self.chart_label.pack()

        for button in self.buttons: button.pack(side = self.props[button.cget('text')]['side'])
        self.frame.pack()

    def __call__(self):
        '''
        Displays the initial slide and starts the tkinter main loop.
        '''

        self.update_display()
        self.pack_components()
        self.root.mainloop()