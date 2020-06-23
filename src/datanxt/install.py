from tkinter import messagebox, ttk, X, BOTH, Text

from datanxt.application_window_template import ApplicationWindowTemplate
from datanxt.services import install


class Install(ApplicationWindowTemplate):
    def __init__(self, master, sessiondetails):
        # Build Frame from Parent
        super().__init__(master)
        self.sessiondetails = sessiondetails

        # Build Header Frame Label with Message
        self.show_header_message(self.app_constants.APPLICATION_INSTALL_HEADER_FRAME_LABEL)

        self.install_frame = ttk.Frame(self.master, style='Content.TFrame')
        self.log = Text(self.install_frame, state='disabled')

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
        # Place Frames
        self.install_frame.pack(fill=X)
        self.install = ttk.Button(self.install_frame, text="Install", command=self.on_install)
        self.install.pack(fill=X)
        self.log.pack(fill=BOTH, expand=True)

    def on_install(self):
        if messagebox.askokcancel("Confirmation",
                                  "This will install SAP Data Migration DQ components in the logged in database server. "
                                  "Do you wish to proceed?"):
            self.sessiondetails.setLog(self.log)
            self.install.config(state='disabled')
            self.sessiondetails.writeToLog(msg="Invoking installation procedure: ")
            install(self.sessiondetails)
            error_lines = self.sessiondetails.getError_Lines()
            for i in error_lines:
                self.highlight_text(tag_name='tag'+str(error_lines[i-1]),
                                    line_no=error_lines[i-1],
                                    start_char=1,
                                    end_char=5,
                                    fg_color='red')