#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import setGui as sg
import Functions as fce
import os

def getWidgetName(widget):
    return Gtk.Buildable.get_name(widget)


class GUI:
    def __init__(self):
        glade_file = 'Gui/Main.glade'

        self.builder = Gtk.Builder()
        self.builder.add_from_file(glade_file)
        self.builder.connect_signals({
                                    'b_exit': Gtk.main_quit,
                                    'b_load_files': self.loadFiles,
                                    'b_files_browser': self.getFilePath,
                                    'b_change': self.pathChange,
                                    'b_dialog_close': self.dialogClose,
                                    'b_save_path': self.savePath,
                                    })

        self.window = sg.setWindow(self.builder, 'win_main', 'Main window')
        self.window.show()
        self.file_dialog = self.builder.get_object('chooser')


        self.path = ''

    def pathChange(self, textbox):
        self.path = self.builder.get_object(getWidgetName(textbox)).get_text()

    def savePath(self, widget):
        path = self.file_dialog.get_current_folder()
        self.builder.get_object('te_files_path').set_text(path)
        self.file_dialog.hide()


    def dialogClose(self, widget):
        self.file_dialog.hide()

    def loadFiles(self, button):
        if len(self.path) > 0:
            data = fce.loadFiles(self.path, '.py')
            try:
                self.setTreeView(data)
            except TypeError:
                msg = 'Empty folder path or incorrect path format.'
                self.setTreeView([[msg]])
        else:
            self.setTreeView([['No folder selected.']])


    def getFilePath(self, button):
        self.file_dialog.set_current_folder(__file__.replace('gui.py', ''))
        self.file_dialog.run()
        self.file_dialog.hide()

    def setTreeView(self, data):
        view = self.builder.get_object('tree_files')
        store = Gtk.ListStore(str)
        for d in data:
            store.append(d)

        view.set_model(store)

        if len(view.get_columns()) < 1:
            render = Gtk.CellRendererText()
            col = Gtk.TreeViewColumn('Files:', render, text=0)
            view.append_column(col)



if __name__ == '__main__':
    gui = GUI()
    Gtk.main()
