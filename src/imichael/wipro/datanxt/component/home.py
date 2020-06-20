from tkinter import messagebox, ttk, X, BOTH, TOP, LEFT, RIGHT
from PIL import ImageTk

from imichael.wipro.datanxt.model.app_models import Page
from imichael.wipro.datanxt.component.application_window_template import ApplicationWindowTemplate
from imichael.wipro.datanxt.services.services import get_table
from imichael.wipro.datanxt.utilities import application_utility


class Home(ApplicationWindowTemplate):
    def __init__(self, master, session_details):
        # Build Frame from Parent
        super().__init__(master)
        self.home_tab = ttk.Notebook(self.master)
        self.projects_tab = ttk.Frame(self.home_tab)
        self.new_project_tab = ttk.Frame(self.home_tab)
        self.config_tab = ttk.Frame(self.home_tab)
        self.admin_tab = ttk.Frame(self.home_tab)
        self.about_tab = ttk.Frame(self.home_tab)
        self.session_details = session_details

        self.header.destroy()

        # Build Content Frame Structure
        self.show_content_frame()

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.master.destroy()

        self.master.geometry(self.app_constants.APPLICATION_HOME_GEOMETRY)
        self.master.title(self.app_constants.APPLICATION_TITLE)
        self.master.protocol("WM_DELETE_WINDOW", on_closing)
        self.master.mainloop()

    def show_content_frame(self):
        self.home_tab.add(self.projects_tab, text=self.app_constants.HOME_TAB_PROJECTS)
        self.home_tab.add(self.new_project_tab, text=self.app_constants.HOME_TAB_NEW_PROJECT)
        self.home_tab.add(self.config_tab, text=self.app_constants.HOME_TAB_CONFIGURATION)
        self.home_tab.add(self.admin_tab, text=self.app_constants.HOME_TAB_ADMIN)
        self.home_tab.add(self.about_tab, text=self.app_constants.HOME_TAB_ABOUT)

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
        self.sys_model_btn = ttk.Button(self.config_menu_window, text=self.app_constants.SYSTEM_MODEL,
                                        command=self.show_sys_model)
        self.sys_model_btn.grid(column=0, row=0, padx=2)
        self.domains_btn = ttk.Button(self.config_menu_window, text=self.app_constants.DATA_DOMAINS,
                                      command=self.show_domains)
        self.domains_btn.grid(column=1, row=0, padx=2)
        self.dor_btn = ttk.Button(self.config_menu_window, text=self.app_constants.DOR, command=self.show_dor)
        self.dor_btn.grid(column=2, row=0, padx=2)
        self.security_btn = ttk.Button(self.config_menu_window, text=self.app_constants.SECURITY,
                                       command=self.show_security)
        self.security_btn.grid(column=3, row=0, padx=2)
        self.upgrade_btn = ttk.Button(self.config_menu_window, text=self.app_constants.UPGRADE,
                                      command=self.show_upgrade)
        self.upgrade_btn.grid(column=4, row=0, padx=2)

    def show_sys_model(self):
        self.page = Page(title=self.app_constants.SYSTEM_MODEL,
                         events=1,
                         table=self.app_constants.TABLE_SYSTEM_MODEL,
                         parent_child=1,
                         child_table=self.app_constants.TABLE_SYSTEM_MODEL_TABLE)

        self.child_page = Page(title=self.app_constants.SYSTEM_MODEL_TABLE,
                               events=1,
                               table=self.app_constants.TABLE_SYSTEM_MODEL_TABLE,
                               filter_field="sys_model_id")

        self.build_display_frame()
        # NLYEHVDCS4MSA51

    def show_domains(self):
        print("show domains")
        self.page = Page(title=self.app_constants.DATA_DOMAINS,
                         events=1,
                         table=self.app_constants.TABLE_DATA_DOMAIN)

        self.build_display_frame()

    def show_dor(self):
        self.page = Page(title=self.app_constants.DOR,
                         events=1,
                         table=self.app_constants.TABLE_DOR)

        self.build_display_frame()

    def show_security(self):
        print("show security")

    def show_upgrade(self):
        print("show upgrade")

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
            self.build_display_events_pane(self.config_display_window, self.page)

        # Fetch table data and build tree view with the data retrieved
        parent_data = get_table(self.session_details, self.page)
        self.display_parent_tree = ttk.Treeview(self.config_display_window, show="headings")

        if self.page.child_table is not None:
            self.display_parent_tree.bind("<Double-1>", self.display_child_frame)
            self.config_display_child_window = ttk.Frame(self.config_display_window, style='Content.TFrame',
                                                         borderwidth=2)

        application_utility.convert_table_result_to_tree(self.display_parent_tree, parent_data)

        # Add record count to title frame
        if config_display_title_events is None:
            config_display_title_events = ttk.Frame(self.config_display_window, style='Header.TFrame', borderwidth=2)

        records = ttk.Label(config_display_title_events, text=parent_data.record_count)
        records.pack(side=RIGHT, padx=2)
        total_records = ttk.Label(config_display_title_events, text=self.app_constants.TOTAL_LBL)
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
            self.build_display_events_pane(self.config_display_child_window, self.child_page, is_child=True)

        # Fetch table data and build tree view with the data retrieved
        child_table = get_table(self.session_details, self.child_page)
        self.display_child_table_tree = ttk.Treeview(self.config_display_child_window, show="headings")

        # self.display_sys_model_tree.bind("<Double-1>", self.sys_model_table)
        application_utility.convert_table_result_to_tree(self.display_child_table_tree, child_table)

        # Add record count to title frame
        if config_display_child_title_events is None:
            config_display_child_title_events = ttk.Frame(self.config_display_child_window, style='Header.TFrame',
                                                          borderwidth=2)

        records = ttk.Label(config_display_child_title_events, text=child_table.record_count)
        records.pack(side=RIGHT, padx=2)
        total_records = ttk.Label(config_display_child_title_events, text=self.app_constants.TOTAL_LBL)
        total_records.pack(side=RIGHT)

        # Pack the contents
        self.display_child_table_tree.pack(side=TOP, fill=BOTH)

    # NLYEHVDCS4MSA51

    def build_admin_frame(self):
        ttk.Label(self.admin_tab, text="This is Admin").grid(column=0, row=0, padx=10, pady=10)

    def build_about_frame(self):
        ttk.Label(self.about_tab, text="This is About").grid(column=0, row=0, padx=10, pady=10)

    def build_display_events_pane(self, window, page, is_child=False):
        config_display_title_events = ttk.Frame(window, style='Header.TFrame', borderwidth=2)
        if not is_child:
            refresh_image = ImageTk.PhotoImage(file=self.app_constants.IMAGE_REFRESH)
            refresh = ttk.Button(config_display_title_events,
                                 image=refresh_image, compound=LEFT)
            refresh.bind("<Button-1>", self.refresh)
            refresh.myId = page.title
            refresh.image = refresh_image
            refresh.pack(side=LEFT, padx=2)

        add_image = ImageTk.PhotoImage(file=self.app_constants.IMAGE_ADD)
        add = ttk.Button(config_display_title_events,
                         image=add_image, compound=LEFT)
        add.bind("<Button-1>", self.add)
        add.myId = page.title
        add.image = add_image
        add.pack(side=LEFT, padx=2)

        edit_image = ImageTk.PhotoImage(file=self.app_constants.IMAGE_EDIT)
        edit = ttk.Button(config_display_title_events,
                          image=edit_image, compound=LEFT)
        edit.bind("<Button-1>", self.edit)
        edit.myId = page.title
        edit.image = edit_image
        edit.pack(side=LEFT, padx=2)

        delete_image = ImageTk.PhotoImage(file=self.app_constants.IMAGE_DELETE)
        delete = ttk.Button(config_display_title_events,
                            image=delete_image, compound=LEFT)
        delete.bind("<Button-1>", self.delete)
        delete.myId = page.title
        delete.image = delete_image
        delete.pack(side=LEFT, padx=2)

        config_display_title_events.pack(fill=X)

    def add(self, event):
        event_name = str(event.widget.myId)
        print("You clicked: " + event_name)
        if event_name == self.app_constants.SYSTEM_MODEL:
            print("You clicked: " + event_name)
        elif event_name == self.app_constants.SYSTEM_MODEL_TABLE:
            print("You clicked: " + event_name)
        elif event_name == self.app_constants.DATA_DOMAINS:
            print("You clicked: " + event_name)
        elif event_name == self.app_constants.DOR:
            print("You clicked: " + event_name)

    def edit(self, event):
        event_name = str(event.widget.myId)
        print("You clicked: " + event_name)
        if event_name == self.app_constants.SYSTEM_MODEL:
            print("You clicked: " + event_name)
        elif event_name == self.app_constants.SYSTEM_MODEL_TABLE:
            print("You clicked: " + event_name)
        elif event_name == self.app_constants.DATA_DOMAINS:
            print("You clicked: " + event_name)
        elif event_name == self.app_constants.DOR:
            print("You clicked: " + event_name)

    def delete(self, event):
        event_name = str(event.widget.myId)
        print("You clicked: " + event_name)
        if event_name == self.app_constants.SYSTEM_MODEL:
            print("You clicked: " + event_name)
        elif event_name == self.app_constants.SYSTEM_MODEL_TABLE:
            print("You clicked: " + event_name)
        elif event_name == self.app_constants.DATA_DOMAINS:
            print("You clicked: " + event_name)
        elif event_name == self.app_constants.DOR:
            print("You clicked: " + event_name)

    def refresh(self, event):
        event_name = str(event.widget.myId)
        print("You clicked: " + event_name)
        if event_name == self.app_constants.SYSTEM_MODEL:
            self.show_sys_model()
        elif event_name == self.app_constants.SYSTEM_MODEL_TABLE:
            print("You clicked: " + event_name)
        elif event_name == self.app_constants.DATA_DOMAINS:
            self.show_domains()
        elif event_name == self.app_constants.DOR:
            self.show_dor()