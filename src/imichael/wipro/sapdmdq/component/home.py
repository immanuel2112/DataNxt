from tkinter import messagebox, ttk, X, BOTH, TOP

from imichael.wipro.sapdmdq.component.applicationwindowtemplate import ApplicationWindowTemplate
from imichael.wipro.sapdmdq.services.services import get_sys_models

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

        # Frames for Configuration tab
        self.config_menu_window = ttk.Frame(self.config_tab, style='Header.TFrame', borderwidth=2)
        self.config_display_window = ttk.Frame(self.config_tab, style='Content.TFrame', borderwidth=2)
        self.config_display_title_window = ttk.Frame(self.config_tab, style='Header.TFrame', borderwidth=2)
        self.config_display_output_window = ttk.Frame(self.config_tab, style='Content.TFrame', borderwidth=2)

        self.sessiondetails = sessiondetails

        self.header.destroy()

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
        self.config_menu_window.pack(fill=X)
        self.config_display_window.pack(fill=BOTH, expand=1)

        self.build_configuration_menu_window()

    def build_configuration_menu_window(self):
        self.sys_model_btn = ttk.Button(self.config_menu_window, text=self.appconstants.SYSTEM_MODEL, command=self.show_sys_models)
        self.sys_model_btn.grid(column=0, row=0, padx=5)
        self.domains_btn = ttk.Button(self.config_menu_window, text=self.appconstants.DATA_DOMAINS, command=self.show_domains)
        self.domains_btn.grid(column=1, row=0, padx=5)
        self.dor_btn = ttk.Button(self.config_menu_window, text=self.appconstants.DOR, command=self.show_dor)
        self.dor_btn.grid(column=2, row=0, padx=5)
        self.security_btn = ttk.Button(self.config_menu_window, text=self.appconstants.SECURITY, command=self.show_security)
        self.security_btn.grid(column=3, row=0, padx=5)
        self.upgrade_btn = ttk.Button(self.config_menu_window, text=self.appconstants.UPGRADE, command=self.show_upgrade)
        self.upgrade_btn.grid(column=4, row=0, padx=5)

    def show_sys_models(self):
        self.config_display_title_window.pack(fill=X)
        self.title = ttk.Label(self.config_display_title_window, text=self.appconstants.SYSTEM_MODEL, style='Header.TLabel')
        self.title.pack()

        sys_models_data = get_sys_models(self.sessiondetails)
        header_columns = sys_models_data["header"]
        print(header_columns)

        self.config_display_output_window.pack(fill=BOTH, expand=1)
        # self.sys_model_btn.state()
        # NLYEHVDCS4MSA51

    def show_domains(self):
        print("show domains")

    def show_dor(self):
        print("show dor")

    def show_security(self):
        print("show security")

    def show_upgrade(self):
        print("show upgrade")

    def build_admin_frame(self):
        ttk.Label(self.admin_tab, text="This is Admin").grid(column=0, row=0, padx=10, pady=10)

    def build_about_frame(self):
        ttk.Label(self.about_tab, text="This is About").grid(column=0, row=0, padx=10, pady=10)