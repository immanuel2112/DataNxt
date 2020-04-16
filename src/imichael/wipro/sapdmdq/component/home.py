from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from imichael.wipro.sapdmdq.component.applicationwindowtemplate import ApplicationWindowTemplate


class Home(ApplicationWindowTemplate):
    def __init__(self, master, sessiondetails):
        # Build Frame from Parent
        super().__init__(master)
        self.sessiondetails = sessiondetails

        # Build Header Frame Label with Message
        self.show_header_message(self.appconstants.APPLICATION_HOME_HEADER_FRAME_LABEL)

        # Build Content Frame Structure
        self.show_content_frame()

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.master.destroy()

        self.master.geometry(self.appconstants.APPLICATION_HOME_GEOMETRY)
        self.master.title(self.appconstants.APPLICATION_TITLE)
        self.master.iconbitmap(self.appconstants.APPLICATION_ICON)
        self.master.geometry(self.appconstants.APPLICATION_HOME_GEOMETRY)
        self.master.protocol("WM_DELETE_WINDOW", on_closing)
        self.master.mainloop()

    def show_content_frame(self):
        # Place Frames
        self.contentleft.pack(side=LEFT)
        self.contentright.pack(fill=BOTH, expand=True)

        # Place widgets and contents in Frames
        self.projects = Button(self.contentleft, text="Projects", bg=self.appconstants.APPLICATION_BUTTON_BGCOLOR,
                               fg=self.appconstants.APPLICATION_BUTTON_FGCOLOR,
                               font=self.appconstants.APPLICATION_BUTTON_FONT_UNDERLINE)
        self.projects.grid(row=1, column=0, sticky=E + W)
        self.newproject = Button(self.contentleft, text="New Project", bg=self.appconstants.APPLICATION_BUTTON_BGCOLOR,
                                 fg=self.appconstants.APPLICATION_BUTTON_FGCOLOR,
                                 font=self.appconstants.APPLICATION_BUTTON_FONT_UNDERLINE)
        self.newproject.grid(row=2, column=0, sticky=E + W)
        self.configuration = Button(self.contentleft, text="Configuration",
                                    bg=self.appconstants.APPLICATION_BUTTON_BGCOLOR,
                                    fg=self.appconstants.APPLICATION_BUTTON_FGCOLOR,
                                    font=self.appconstants.APPLICATION_BUTTON_FONT_UNDERLINE,
                                    command=self.func_configuration)
        self.configuration.grid(row=3, column=0, sticky=E + W)
        self.configuration = Button(self.contentleft, text="About", bg=self.appconstants.APPLICATION_BUTTON_BGCOLOR,
                                    fg=self.appconstants.APPLICATION_BUTTON_FGCOLOR,
                                    font=self.appconstants.APPLICATION_BUTTON_FONT_UNDERLINE)
        self.configuration.grid(row=4, column=0, sticky=E + W)

    def func_configuration(self):
        # Place Frames
        self.contentrighttop.pack(fill=X)

        # Place widgets and contents in Frames
        self.projects = ttk.Button(self.contentrighttop, text="System Models")
        self.projects.grid(row=1, column=1, sticky=W)
        self.newproject = ttk.Button(self.contentrighttop, text="Data Domain")
        self.newproject.grid(row=1, column=3, sticky=W)
        self.configuration = ttk.Button(self.contentrighttop, text="Data Object Registry")
        self.configuration.grid(row=1, column=5, sticky=W)
