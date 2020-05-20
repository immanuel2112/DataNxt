from tkinter import messagebox, ttk

from imichael.wipro.sapdmdq.component.applicationwindowtemplate import ApplicationWindowTemplate


class Home(ApplicationWindowTemplate):
    def __init__(self, master, sessiondetails):
        # Build Frame from Parent
        super().__init__(master)
        self.home_tab = ttk.Notebook(self.master)
        self.projects_tab = ttk.Frame(self.home_tab)
        self.newproject_tab = ttk.Frame(self.home_tab)
        self.config_tab = ttk.Frame(self.home_tab)
        self.about_tab = ttk.Frame(self.home_tab)

        self.sessiondetails = sessiondetails
        self.content.destroy()

        # Build Content Frame Structure
        self.show_content_frame()

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.master.destroy()

        self.master.geometry(self.appconstants.APPLICATION_HOME_GEOMETRY)
        self.master.title(self.appconstants.APPLICATION_TITLE)
        self.master.protocol("WM_DELETE_WINDOW", on_closing)
        self.master.mainloop()

    def show_content_frame(self):
        self.home_tab.add(self.projects_tab, text=self.appconstants.HOME_TAB_PROJECTS)
        self.home_tab.add(self.newproject_tab, text=self.appconstants.HOME_TAB_NEWPROJECT)
        self.home_tab.add(self.config_tab, text=self.appconstants.HOME_TAB_CONFIGURATION)
        self.home_tab.add(self.about_tab, text=self.appconstants.HOME_TAB_ABOUT)

        self.build_projects_frame()
        self.build_new_project_frame()
        self.build_configuration_frame()
        self.build_about_frame()

        self.home_tab.pack(expand=1, fill="both")

    def build_projects_frame(self):
        ttk.Label(self.projects_tab, text="This is Projects").grid(column=0, row=0, padx=10, pady=10)

    def build_new_project_frame(self):
        ttk.Label(self.newproject_tab, text="This is New Project").grid(column=0, row=0, padx=10, pady=10)

    def build_configuration_frame(self):
        ttk.Label(self.config_tab, text="This is Configuration").grid(column=0, row=0, padx=10, pady=10)

    def build_about_frame(self):
        ttk.Label(self.about_tab, text="This is About").grid(column=0, row=0, padx=10, pady=10)