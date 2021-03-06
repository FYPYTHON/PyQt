# coding=utf-8

from tkinter import *
#from Tkinter.ttk import *
# from tkinter.messagebox import showerror
# from tkinter.font import Font
# from tkinter import ttk
from tkinter.ttk import Treeview
from ui.searchtextdialog import *
from tkinter import Listbox, StringVar



class MainWindowUI:
    """
    rows and columns divide the widget region
    (row,column)
    ------------------------------------------------
    0 toolbar    filepath
    ------------------------------------------------
    1 0 filetree | 1 scrbar | 2 lineno| 3 TextArea|
    -------------|----------| --------|-----------|
    """

    # Rows
    toolBarRow = 0
    fileTreeRow = 1
    filePathLabelsRow = 0
    searchTextRow = 1
    uniScrollbarRow = lineNumbersRow = textAreasRow = 2
    horizontalScrollbarRow = 3

    # Columns
    fileTreeCol = 0
    fileTreeScrollbarCol = 1
    leftFilePathLabelsCol = 3
    leftLineNumbersCol = 2
    # leftLineNumbersCol = leftFilePathLabelsCol = 3    # should span at least two columns

    leftTextAreaCol = leftHorizontalScrollbarCol = 4
    uniScrollbarCol = 5
    rightLineNumbersCol = rightFilePathLabelsCol = 6  # should span at least two columns
    rightTextAreaCol = rightHorizontalScrollbarCol = 7

    leftLineButtonsCol = 3
    rightLineButtonscol = 9

    # Colors
    whiteColor = '#ffffff'
    redColor = '#ffc4c4'
    darkredColor = '#ff8282'
    grayColor = '#dddddd'
    lightGrayColor = '#eeeeee'
    greenColor = '#c9fcd6'
    darkgreenColor = '#50c96e'
    yellowColor = '#f0f58c'
    darkYellowColor = '#ffff00'

    def __init__(self, window):
        self.main_window = window
        self.main_window.grid_rowconfigure(self.toolBarRow,weight=0)
        self.main_window.grid_rowconfigure(self.filePathLabelsRow, weight=0)
        self.main_window.grid_rowconfigure(self.searchTextRow, weight=0)
        self.main_window.grid_rowconfigure(self.textAreasRow, weight=1)

        self.main_window.grid_columnconfigure(self.fileTreeCol, weight=0)
        self.main_window.grid_columnconfigure(self.fileTreeScrollbarCol, weight=0)
        self.main_window.grid_columnconfigure(self.leftLineNumbersCol, weight=0)
        self.main_window.grid_columnconfigure(self.leftLineButtonsCol, weight=0)   # left buttons col
        self.main_window.grid_columnconfigure(self.leftTextAreaCol, weight=1)
        self.main_window.grid_columnconfigure(self.uniScrollbarCol, weight=0)
        self.main_window.grid_columnconfigure(self.rightLineNumbersCol, weight=0)
        self.main_window.grid_columnconfigure(self.rightLineButtonscol, weight=0)  # right buttons col
        self.main_window.grid_columnconfigure(self.rightTextAreaCol, weight=1)
        self.menubar = Menu(self.main_window)
        self.menus = {}
        self.text_area_font = 'TkFixedFont'

    # Center window and set its size
    def center_window(self):
        sw = self.main_window.winfo_screenwidth()
        sh = self.main_window.winfo_screenheight()

        w = 0.7 * sw
        h = 0.7 * sh

        x = (sw - w)/2
        y = (sh - h)/2

        self.main_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.main_window.minsize(int(0.3 * sw), int(0.3 * sh))

    # Menu bar
    def add_menu(self, menuName, commandList):
        self.menus[menuName] = Menu(self.menubar,tearoff=0)
        for c in commandList:
            if 'separator' in c: self.menus[menuName].add_separator()
            else: self.menus[menuName].add_command(label=c['name'], command=c['command'],
                                                   accelerator=c['accelerator'] if 'accelerator' in c else '')
        self.menubar.add_cascade(label=menuName, menu=self.menus[menuName])
        self.main_window.config(menu=self.menubar)

    # Labels
    def create_file_path_labels(self):
        self.leftFileLabel = Label(self.main_window, anchor='center', width=1000, background=self.lightGrayColor)
        self.leftFileLabel.grid(row=self.filePathLabelsRow, column=self.leftFilePathLabelsCol, columnspan=2)
        self.rightFileLabel = Label(self.main_window, anchor='center', width=1000, background=self.lightGrayColor)
        self.rightFileLabel.grid(row=self.filePathLabelsRow, column=self.rightFilePathLabelsCol, columnspan=2)

    # Search text entnry
    def create_search_text_entry(self, searchButtonCallback):
        self.searchTextDialog = SearchTextDialog(self.main_window, [self.leftFileTextArea, self.rightFileTextArea], searchButtonCallback)
        self.searchTextDialog.grid(row=self.searchTextRow, column=self.leftFilePathLabelsCol, columnspan=5, sticky=EW)

        self.searchTextDialog.grid_remove()

    # File treeview
    def create_file_treeview(self):
        self.fileTreeView = Treeview(self.main_window)
        self.fileTreeYScrollbar = Scrollbar(self.main_window, orient='vertical', command=self.fileTreeView.yview)
        self.fileTreeXScrollbar = Scrollbar(self.main_window, orient='horizontal', command=self.fileTreeView.xview)
        self.fileTreeView.configure(yscroll=self.fileTreeYScrollbar.set, xscroll=self.fileTreeXScrollbar.set)

        self.fileTreeView.grid(row=self.fileTreeRow, column=self.fileTreeCol, sticky=NS, rowspan=3)
        self.fileTreeYScrollbar.grid(row=self.fileTreeRow, column=self.fileTreeScrollbarCol, sticky=NS, rowspan=3)
        self.fileTreeXScrollbar.grid(row=self.horizontalScrollbarRow, column=self.fileTreeCol, sticky=EW)

        self.fileTreeView.tag_configure('red', background=self.redColor)
        self.fileTreeView.tag_configure('green', background=self.greenColor)
        self.fileTreeView.tag_configure('yellow', background=self.yellowColor)

        # hide it until needed
        self.fileTreeView.grid_remove()
        self.fileTreeYScrollbar.grid_remove()
        self.fileTreeXScrollbar.grid_remove()

    # Line buttons
    def create_tree_buttons(self):
        # self.leftLinebuttons = Treeview(self.main_window)
        # self.leftLinebuttons.grid(row=self.lineNumbersRow, column=self.leftLineButtonsCol, sticky=NS, rowspan=1)
        # self.leftLinebuttons.tag_configure('green', background=self.greenColor)
        #
        # self.rightLinebuttons = Treeview(self.main_window)
        # self.rightLinebuttons.grid(row=self.lineNumbersRow, column=self.rightLineButtonscol, sticky=NS, rowspan=1)
        # self.rightLinebuttons.tag_configure('green', background=self.greenColor)
        #
        # self.leftLinebuttons.insert('', 'end', text="test", open=True, tags=('green', 'simple'))
        # self.rightLinebuttons.insert('', 'end', text="test", open=True, tags=('green', 'simple'))
        #
        # # disable the line numbers
        # self.leftLinebuttons.grid_remove()
        # self.rightLinebuttons.grid_remove()
        self.leftLinebuttons = Text(self.main_window, width=1, padx=5, pady=5, height=1, bg=self.lightGrayColor)
        self.leftLinebuttons.grid(row=self.lineNumbersRow, column=self.leftLineButtonsCol, sticky=NS)
        self.leftLinebuttons.config(font=self.text_area_font)
        self.leftLinebuttons.tag_configure('line', justify='right')
        self.leftLinebuttons.tag_configure('green', background=self.greenColor)

        # self.rightLinebuttons = Text(self.main_window, width=1, padx=5, pady=5, height=1, bg=self.lightGrayColor)
        # self.rightLinebuttons.grid(row=self.lineNumbersRow, column=self.leftLineButtonsCol, sticky=NS)
        # self.rightLinebuttons.config(font=self.text_area_font)
        # self.rightLinebuttons.tag_configure('line', justify='right')
        # self.rightLinebuttons.tag_configure('green', background=self.greenColor)

        ops1 = StringVar()
        ops1.set((11, 22, 33, 44, 55))
        self.rightLinebuttons = Listbox(self.main_window
                                        , listvariable=ops1)
        self.rightLinebuttons.grid(row=self.lineNumbersRow, column=self.rightLineButtonscol, sticky=NS,
                                   padx=1, ipadx=1)
        self.rightLinebuttons.config(font=self.text_area_font)
        # self.rightLinebuttons.bindtags('line', justify='right')
        # self.rightLinebuttons.bindtags('green', background=self.greenColor)

        self.leftLinenumbers.config(state=DISABLED)
        self.rightLinenumbers.config(state=DISABLED)



    # Text areas
    def create_text_areas(self):
        self.leftFileTextArea = Text(self.main_window, padx=5, pady=5, width=1, height=1, bg=self.grayColor)
        self.leftFileTextArea.grid(row=self.textAreasRow, column=self.leftTextAreaCol, sticky=NSEW)
        self.leftFileTextArea.config(font=self.text_area_font)
        self.leftFileTextArea.config(wrap='none')

        self.rightFileTextArea = Text(self.main_window, padx=5, pady=5, width=1, height=1, bg=self.grayColor)
        self.rightFileTextArea.grid(row=self.textAreasRow, column=self.rightTextAreaCol, sticky=NSEW)
        self.rightFileTextArea.config(font=self.text_area_font)
        self.rightFileTextArea.config(wrap='none')

        # configuring highlight tags
        self.leftFileTextArea.tag_configure('red', background=self.redColor)
        self.leftFileTextArea.tag_configure('darkred', background=self.darkredColor)
        self.leftFileTextArea.tag_configure('gray', background=self.grayColor)
        self.leftFileTextArea.tag_configure('search', background=self.darkYellowColor)
        self.rightFileTextArea.tag_configure('green', background=self.greenColor)
        self.rightFileTextArea.tag_configure('darkgreen', background=self.darkgreenColor)
        self.rightFileTextArea.tag_configure('gray', background=self.grayColor)
        self.rightFileTextArea.tag_configure('search', background=self.darkYellowColor)

        # disable the text areas
        self.leftFileTextArea.config(state=DISABLED)
        self.rightFileTextArea.config(state=DISABLED)

    # Line numbers
    def create_line_numbers(self):
        self.leftLinenumbers = Text(self.main_window, width=3, padx=5, pady=5, height=1, bg=self.lightGrayColor)
        self.leftLinenumbers.grid(row=self.lineNumbersRow, column=self.leftLineNumbersCol, sticky=NS)
        self.leftLinenumbers.config(font=self.text_area_font)
        self.leftLinenumbers.tag_configure('line', justify='right')

        self.rightLinenumbers = Text(self.main_window, width=3, padx=5, pady=5, height=1, bg=self.lightGrayColor)
        self.rightLinenumbers.grid(row=self.lineNumbersRow, column=self.rightLineNumbersCol, sticky=NS)
        self.rightLinenumbers.config(font=self.text_area_font)
        self.rightLinenumbers.tag_configure('line', justify='right')

        # disable the line numbers
        self.leftLinenumbers.config(state=DISABLED)
        self.rightLinenumbers.config(state=DISABLED)

    # Scroll bars
    def scrollBoth(self, action, position, type=None):
        self.leftFileTextArea.yview_moveto(position)
        self.rightFileTextArea.yview_moveto(position)
        self.leftLinenumbers.yview_moveto(position)
        self.rightLinenumbers.yview_moveto(position)

    def updateScroll(self, first, last, type=None):
        self.leftFileTextArea.yview_moveto(first)
        self.rightFileTextArea.yview_moveto(first)
        self.leftLinenumbers.yview_moveto(first)
        self.rightLinenumbers.yview_moveto(first)
        self.uniScrollbar.set(first, last)

    def create_scroll_bars(self):
        self.uniScrollbar = Scrollbar(self.main_window)
        self.uniScrollbar.grid(row=self.uniScrollbarRow, column=self.uniScrollbarCol, sticky=NS)
        self.uniScrollbar.config(command=self.scrollBoth)
        self.leftFileTextArea.config(yscrollcommand=self.updateScroll)
        self.rightFileTextArea.config(yscrollcommand=self.updateScroll)
        self.leftLinenumbers.config(yscrollcommand=self.updateScroll)
        self.rightLinenumbers.config(yscrollcommand=self.updateScroll)

        leftHorizontalScrollbar = Scrollbar(self.main_window, orient=HORIZONTAL)
        leftHorizontalScrollbar.grid(row=self.horizontalScrollbarRow, column=self.leftHorizontalScrollbarCol, sticky=EW)
        leftHorizontalScrollbar.config(command=self.leftFileTextArea.xview)
        self.leftFileTextArea.config(xscrollcommand=leftHorizontalScrollbar.set)

        rightHorizontalScrollbar = Scrollbar(self.main_window, orient=HORIZONTAL)
        rightHorizontalScrollbar.grid(row=self.horizontalScrollbarRow, column=self.rightHorizontalScrollbarCol, sticky=EW)
        rightHorizontalScrollbar.config(command=self.rightFileTextArea.xview)
        self.rightFileTextArea.config(xscrollcommand=rightHorizontalScrollbar.set)
