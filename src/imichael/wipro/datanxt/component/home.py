from tkinter import messagebox, ttk, X, BOTH, TOP, LEFT, RIGHT, VERTICAL, HORIZONTAL, NS, EW, NW, SE

from imichael.wipro.datanxt.model.app_models import Page
from imichael.wipro.datanxt.component.applicationwindowtemplate import ApplicationWindowTemplate
from imichael.wipro.datanxt.services.services import get_table
from imichael.wipro.datanxt.utilities import applicationutility


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

        self.home_tab.pack(expand=1, fill=BOTH)

    def build_projects_frame(self):
        ttk.Label(self.projects_tab, text="This is Projects").grid(column=0, row=0, padx=10, pady=10)

    def build_new_project_frame(self):
        ttk.Label(self.new_project_tab, text="This is New Project").grid(column=0, row=0, padx=10, pady=10)

    def build_configuration_frame(self):
        # Frames for Configuration tab
        self.config_menu_window = ttk.Frame(self.config_tab, style='Header.TFrame', borderwidth=2)
        self.config_display_window = ttk.Frame(self.config_tab, style='Content.TFrame', borderwidth=2)

        self.config_menu_window.pack(fill=X)
        self.config_display_window.pack(fill=BOTH, expand=1)

        # Build Menu Pane
        self.sys_model_btn = ttk.Button(self.config_menu_window, text=self.appconstants.SYSTEM_MODEL,
                                        command=self.show_sys_model)
        self.sys_model_btn.grid(column=0, row=0, padx=2)
        self.domains_btn = ttk.Button(self.config_menu_window, text=self.appconstants.DATA_DOMAINS,
                                      command=self.show_domains)
        self.domains_btn.grid(column=1, row=0, padx=2)
        self.dor_btn = ttk.Button(self.config_menu_window, text=self.appconstants.DOR, command=self.show_dor)
        self.dor_btn.grid(column=2, row=0, padx=2)
        self.security_btn = ttk.Button(self.config_menu_window, text=self.appconstants.SECURITY,
                                       command=self.show_security)
        self.security_btn.grid(column=3, row=0, padx=2)
        self.upgrade_btn = ttk.Button(self.config_menu_window, text=self.appconstants.UPGRADE,
                                      command=self.show_upgrade)
        self.upgrade_btn.grid(column=4, row=0, padx=2)

    def show_sys_model(self):
        self.page = Page(title=self.appconstants.SYSTEM_MODEL,
                         events=1,
                         table=self.appconstants.TABLE_SYSTEM_MODEL,
                         parent_child=1,
                         child_table=self.appconstants.TABLE_SYSTEM_MODEL_TABLE)

        self.child_page = Page(title=self.appconstants.SYSTEM_MODEL_TABLE,
                               events=1,
                               table=self.appconstants.TABLE_SYSTEM_MODEL_TABLE,
                               filter_field="sys_model_id")

        self.build_display_frame()
        # NLYEHVDCS4MSA51

    def build_display_frame(self):
        # Rebuild the display window if its already created. This is for reclick functionality
        if self.config_display_window is not None:
            self.config_display_window.destroy()
            self.config_display_window = ttk.Frame(self.config_tab, style='Content.TFrame', borderwidth=2)
            self.config_display_window.pack(fill=BOTH, expand=1)

        # Build title for display window
        config_display_title_window = ttk.Frame(self.config_display_window, style='Header.TFrame', borderwidth=2)
        title = ttk.Label(config_display_title_window, text=self.page.title, style='Header.TLabel')
        title.pack(side=TOP)
        config_display_title_window.pack(fill=X)

        config_display_title_events = None

        # Build events for the table functionality if events is enabled
        if self.page.events is not None:
            config_display_title_events = ttk.Frame(self.config_display_window, style='Header.TFrame', borderwidth=2)
            refresh = ttk.Button(config_display_title_events, text=self.appconstants.REFRESH,
                                 command=self.show_sys_model)
            refresh.pack(side=LEFT, padx=2)
            add = ttk.Button(config_display_title_events, text=self.appconstants.ADD)
            add.pack(side=LEFT, padx=2)
            edit = ttk.Button(config_display_title_events, text=self.appconstants.EDIT)
            edit.pack(side=LEFT, padx=2)
            delete = ttk.Button(config_display_title_events, text=self.appconstants.DELETE)
            delete.pack(side=LEFT, padx=2)
            config_display_title_events.pack(fill=X)

        # Fetch table data and build tree view with the data retrieved
        parent_data = get_table(self.sessiondetails, self.page)
        self.display_parent_tree = ttk.Treeview(self.config_display_window, show="headings")

        if self.page.child_table is not None:
            self.display_parent_tree.bind("<Double-1>", self.display_child_frame)
            self.config_display_child_window = ttk.Frame(self.config_display_window, style='Content.TFrame',
                                                         borderwidth=2)

        applicationutility.convert_table_result_to_tree(self.display_parent_tree, parent_data)

        # Add record count to title frame
        if config_display_title_events is None:
            config_display_title_events = ttk.Frame(self.config_display_window, style='Header.TFrame', borderwidth=2)

        records = ttk.Label(config_display_title_events, text=parent_data.record_count)
        records.pack(side=RIGHT, padx=2)
        total_records = ttk.Label(config_display_title_events, text=self.appconstants.TOTAL_LBL)
        total_records.pack(side=RIGHT)

        # Pack the contents
        self.display_parent_tree.pack(side=TOP, fill=X)

    def display_child_frame(self, event):
        item = self.display_parent_tree.identify('item', event.x, event.y)
        selected_parent = self.display_parent_tree.item(item, "text")
        print("you clicked on ", selected_parent)
        self.child_page.filter_field_value = selected_parent

        # Rebuild the display window if its already created. This is for reclick functionality
        if self.config_display_child_window is not None:
            self.config_display_child_window.destroy()
            self.config_display_child_window = ttk.Frame(self.config_display_window, style='Content.TFrame',
                                                         borderwidth=2)
            self.config_display_child_window.pack(fill=BOTH, expand=1)

        # Build title for display window
        config_display_child_title_window = ttk.Frame(self.config_display_child_window, style='Header.TFrame',
                                                      borderwidth=2)
        child_title = ttk.Label(config_display_child_title_window, text=self.child_page.title, style='Header.TLabel')
        child_title.pack(side=TOP)
        config_display_child_title_window.pack(fill=X)

        config_display_child_title_events = None

        # Build events for the table functionality if events is enabled
        if self.child_page.events is not None:
            config_display_child_title_events = ttk.Frame(self.config_display_child_window, style='Header.TFrame',
                                                          borderwidth=2)
            # refresh = ttk.Button(config_display_child_title_events, text="Refresh", command=self.display_child_frame)
            # refresh.grid(column=0, row=0, padx=2)
            add = ttk.Button(config_display_child_title_events, text=self.appconstants.ADD)
            add.pack(side=LEFT, padx=2)
            edit = ttk.Button(config_display_child_title_events, text=self.appconstants.EDIT)
            edit.pack(side=LEFT, padx=2)
            delete = ttk.Button(config_display_child_title_events, text=self.appconstants.DELETE)
            delete.pack(side=LEFT, padx=2)
            sys_model_lbl = ttk.Label(config_display_child_title_events,
                                      text=self.appconstants.SYSTEM_MODEL +": "+selected_parent, style='Header.TLabel')
            sys_model_lbl.pack(side=LEFT, padx=2)
            config_display_child_title_events.pack(fill=X)

        # Fetch table data and build tree view with the data retrieved
        # config_display_child_window = ttk.Frame(self.config_display_child_window, style='Content.TFrame', borderwidth=2)
        child_table = get_table(self.sessiondetails, self.child_page)
        self.display_child_table_tree = ttk.Treeview(self.config_display_child_window, show="headings")

        # self.display_sys_model_tree.bind("<Double-1>", self.sys_model_table)
        applicationutility.convert_table_result_to_tree(self.display_child_table_tree, child_table)

        # Add record count to title frame
        if config_display_child_title_events is None:
            config_display_child_title_events = ttk.Frame(self.config_display_child_window, style='Header.TFrame',
                                                          borderwidth=2)

        records = ttk.Label(config_display_child_title_events, text=child_table.record_count)
        records.pack(side=RIGHT, padx=2)
        total_records = ttk.Label(config_display_child_title_events, text=self.appconstants.TOTAL_LBL)
        total_records.pack(side=RIGHT)

        # Pack the contents
        self.display_child_table_tree.pack(side=TOP, fill=BOTH)

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
