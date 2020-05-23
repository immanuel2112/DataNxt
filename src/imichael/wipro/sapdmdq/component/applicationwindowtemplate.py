from tkinter import messagebox, ttk

from imichael.wipro.sapdmdq.utilities.applicationconstants import ApplicationConstants


class ApplicationWindowTemplate(object):
    def __init__(self, master):
        self.master = master
        self.error = ""
        self.info = ""
        self.warning = ""
        self.headermessagelbl = ""
        self.sessiondetails = None
        self.appconstants = ApplicationConstants()

        #Styles
        style = ttk.Style()
        style.configure('Header.TFrame',
                        background=self.appconstants.APPLICATION_HEADER_FRAME_BGCOLOR)
        style.configure('Header.TLabel',
                        font=self.appconstants.APPLICATION_HEADER_LABEL_FONT,
                        foreground=self.appconstants.APPLICATION_HEADER_LABEL_FGCOLOR,
                        background=self.appconstants.APPLICATION_HEADER_LABEL_BGCOLOR)
        style.configure('Content.TFrame',
                        background=self.appconstants.APPLICATION_CONTENT_FRAME_BGCOLOR)
        style.configure('Content.TLabel',
                        font=self.appconstants.APPLICATION_CONTENT_LABEL_FONT,
                        foreground=self.appconstants.APPLICATION_CONTENT_LABEL_FGCOLOR,
                        background=self.appconstants.APPLICATION_CONTENT_LABEL_BGCOLOR)
        style.configure('Content.TRadiobutton',
                        foreground=self.appconstants.APPLICATION_CONTENT_LABEL_FGCOLOR,
                        background=self.appconstants.APPLICATION_CONTENT_LABEL_BGCOLOR)
        style.configure('ContentRTop.TFrame',
                        background=self.appconstants.APPLICATION_CONTENT_FRAME_BGCOLOR)

        # Define Frames
        self.header = ttk.Frame(self.master, style='Header.TFrame')


    def show_header_message(self, text):
        # Build Header Frame
        self.headermessagelbl = ttk.Label(self.header, text=text, style='Header.TLabel')
        self.headermessagelbl.pack()

    def show_error(self):
        messagebox.showerror(self.appconstants.APPLICATION_MESSAGEBOX_TYPE_ERROR, self.error)

    def show_info(self):
        messagebox.showinfo(self.appconstants.APPLICATION_MESSAGEBOX_TYPE_INFO, self.info)

    def show_warning(self):
        messagebox.showwarning(self.appconstants.APPLICATION_MESSAGEBOX_TYPE_ERROR, self.warning)

    def reset_to_default(self):
        self.error = ""
        self.info = ""
        self.warning = ""

    def func_configuration(self):
        pass

    # adding a tag to a part of text specifying the indices
    def highlight_text(self, tag_name, lineno, start_char, end_char, bg_color=None, fg_color=None):
        log = self.sessiondetails.getLog()
        log['state'] = 'normal'
        log.tag_add(tag_name, f'{lineno}.{start_char}', f'{lineno}.{end_char}')
        log.tag_config(tag_name, background=bg_color, foreground=fg_color)
        log['state'] = 'disabled'
