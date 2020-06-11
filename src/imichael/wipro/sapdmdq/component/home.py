from tkinter import messagebox, ttk, X, BOTH, VERTICAL

from imichael.wipro.sapdmdq.component.applicationwindowtemplate import ApplicationWindowTemplate


class Home(ApplicationWindowTemplate):
    def __init__(self, master, sessiondetails):
        # Build Frame from Parent
        super().__init__(master)
        self.home_tab = ttk.Notebook(self.master)
        self.projects_tab = ttk.Frame(self.home_tab)
        self.new_project_tab = ttk.Frame(self.home_tab)
        self.config_tab = ttk.Frame(self.home_tab)
        self.admin_tab = ttk.Frame(self.home_tab)
        self.about_tab = ttk.Frame(self.home_tab)

        self.sessiondetails = sessiondetails

        # Build Content Frame Structure
        self.show_content_frame()

        self.header.pack(fill=X)

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.master.destroy()

        self.master.geometry(self.appconstants.APPLICATION_HOME_GEOMETRY)
        self.master.title(self.appconstants.APPLICATION_TITLE)
        self.master.protocol("WM_DELETE_WINDOW", on_closing)
        self.master.mainloop()

    def show_content_frame(self):
        self.home_tab.add(self.projects_tab, text=self.appconstants.HOME_TAB_PROJECTS)
        self.home_tab.add(self.new_project_tab, text=self.appconstants.HOME_TAB_NEWPROJECT)
        self.home_tab.add(self.config_tab, text=self.appconstants.HOME_TAB_CONFIGURATION)
        self.home_tab.add(self.admin_tab, text=self.appconstants.HOME_TAB_ADMIN)
        self.home_tab.add(self.about_tab, text=self.appconstants.HOME_TAB_ABOUT)

        self.build_projects_frame()
        self.build_new_project_frame()
        self.build_configuration_frame()
        self.build_admin_frame()
        self.build_about_frame()

        self.home_tab.pack(expand=1, fill="both")

    def build_projects_frame(self):
        ttk.Label(self.projects_tab, text="This is Projects").grid(column=0, row=0, padx=10, pady=10)

    def build_new_project_frame(self):
        ttk.Label(self.new_project_tab, text="This is New Project").grid(column=0, row=0, padx=10, pady=10)

    def build_configuration_frame(self):
        self.config_menu_tab = ttk.Frame(self.config_tab)
        self.config_display_tab = ttk.Frame(self.config_tab)
        self.config_menu_tab.grid(column=0, row=0)
        self.config_display_tab.grid(column=1, row=0)

        self.sys_model_btn = ttk.Button(self.config_menu_tab, text="System Model")
        self.sys_model_btn.pack(fill=X)

    def build_admin_frame(self):
        ttk.Label(self.admin_tab, text="This is Admin").grid(column=0, row=0, padx=10, pady=10)

    def build_about_frame(self):
        ttk.Label(self.about_tab, text="This is About").grid(column=0, row=0, padx=10, pady=10)