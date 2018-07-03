# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


def setWindow(builder, window_name, tittle):

    window = builder.get_object(window_name)
    window.set_title(tittle)
    window.connect('delete-event', Gtk.main_quit)

    return window