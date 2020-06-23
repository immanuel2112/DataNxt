from tkinter import messagebox, ttk

from datanxt.application_constants import ApplicationConstants


class ApplicationWindowTemplate:
    def __init__(self, master):
        self.master = master
        self.error = ""
        self.info = ""
        self.warning = ""
        self.header_message_lbl = ""
        self.session_details = None
        self.app_constants = ApplicationConstants()

        # Styles
        style = ttk.Style()
        style.configure('Header.TFrame',
                        background=self.app_constants.APPLICATION_HEADER_FRAME_BGCOLOR)
        style.configure('Header.TLabel',
                        font=self.app_constants.APPLICATION_HEADER_LABEL_FONT,
                        foreground=self.app_constants.APPLICATION_HEADER_LABEL_FGCOLOR,
                        background=self.app_constants.APPLICATION_HEADER_LABEL_BGCOLOR)
        style.configure('Content.TFrame',
                        background=self.app_constants.APPLICATION_CONTENT_FRAME_BGCOLOR)
        style.configure('Content.TLabel',
                        font=self.app_constants.APPLICATION_CONTENT_LABEL_FONT,
                        foreground=self.app_constants.APPLICATION_CONTENT_LABEL_FGCOLOR,
                        background=self.app_constants.APPLICATION_CONTENT_LABEL_BGCOLOR)
        style.configure('Content.TRadiobutton',
                        foreground=self.app_constants.APPLICATION_CONTENT_LABEL_FGCOLOR,
                        background=self.app_constants.APPLICATION_CONTENT_LABEL_BGCOLOR)
        style.configure('ContentRTop.TFrame',
                        background=self.app_constants.APPLICATION_CONTENT_FRAME_BGCOLOR)
        style.configure('ContentMenuFrame.TFrame',
                        background=self.app_constants.APPLICATION_CONTENT_MENU_FRAME_BG_COLOR)
        style.configure('ContentDisplayFrame.TFrame',
                        background=self.app_constants.APPLICATION_CONTENT_DISPLAY_FRAME_BG_COLOR)

        # style.theme_create( "MyStyle", parent="alt", settings={
        #     "Header.TFrame": {"configure": {"background": self.appconstants.APPLICATION_HEADER_FRAME_BGCOLOR}},
        #     "Content.TFrame": {"configure": {"background": self.appconstants.APPLICATION_CONTENT_FRAME_BGCOLOR}},
        #     "ContentRTop.TFrame": {"configure": {"background": self.appconstants.APPLICATION_CONTENT_FRAME_BGCOLOR}},
        #     "ContentMenuFrame.TFrame": {"configure": {"background": self.appconstants.APPLICATION_CONTENT_MENU_FRAME_BGCOLOR}},
        #     "ContentDisplayFrame.TFrame": {"configure": {"background": self.appconstants.APPLICATION_CONTENT_DISPLAY_FRAME_BGCOLOR}},
        #
        #     "Header.TLabel": {"configure": {"font": self.appconstants.APPLICATION_HEADER_LABEL_FONT,
        #                                     "foreground": self.appconstants.APPLICATION_HEADER_LABEL_FGCOLOR,
        #                                     "background": self.appconstants.APPLICATION_HEADER_LABEL_BGCOLOR,}},
        #
        #     "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        #     "TNotebook.Tab": {"configure": {"padding": [100, 100] },}})
        #
        # style.theme_use("MyStyle")

        # Define Frames
        self.header = ttk.Frame(self.master, style='Header.TFrame')

    def show_header_message(self, text):
        # Build Header Frame
        self.header_message_lbl = ttk.Label(self.header, text=text, style='Header.TLabel')
        self.header_message_lbl.pack()

    def show_error(self):
        messagebox.showerror(self.app_constants.APPLICATION_MESSAGEBOX_TYPE_ERROR, self.error)

    def show_info(self):
        messagebox.showinfo(self.app_constants.APPLICATION_MESSAGEBOX_TYPE_INFO, self.info)

    def show_warning(self):
        messagebox.showwarning(self.app_constants.APPLICATION_MESSAGEBOX_TYPE_ERROR, self.warning)

    def reset_to_default(self):
        self.error = ""
        self.info = ""
        self.warning = ""

    def func_configuration(self):
        pass

    # adding a tag to a part of text specifying the indices
    def highlight_text(self, tag_name, line_no, start_char, end_char, bg_color=None, fg_color=None):
        log = self.session_details.getLog()
        log['state'] = 'normal'
        log.tag_add(tag_name, f'{line_no}.{start_char}', f'{line_no}.{end_char}')
        log.tag_config(tag_name, background=bg_color, foreground=fg_color)
        log['state'] = 'disabled'
