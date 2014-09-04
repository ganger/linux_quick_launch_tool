#! /usr/bin/python
# -*- coding: utf-8 -*-

# 
# Author:     Ganger <ganger695988290@gmail.com>
# Maintainer: Ganger <ganger695988290@gmail.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from Xlib import display
from Xlib.ext import record
from Xlib import X, XK
from Xlib.protocol import rq
import subprocess

        
local_dpy = display.Display()
record_dpy = display.Display()
def record_event(record_callback):
    ctx = record_dpy.record_create_context(
        0,
        [record.AllClients],
        [{
                'core_requests': (0, 0),
                'core_replies': (0, 0),
                'ext_requests': (0, 0, 0, 0),
                'ext_replies': (0, 0, 0, 0),
                'delivered_events': (0, 0),
                'device_events': (X.KeyPress, X.MotionNotify),
                'errors': (0, 0),
                'client_started': False,
                'client_died': False,
                }])
         
    record_dpy.record_enable_context(ctx, record_callback)
    record_dpy.record_free_context(ctx)

def get_event_data(data):
    return rq.EventField(None).parse_binary_value(data, record_dpy.display, None, None)
    
def get_keyname(event):
    keysym = local_dpy.keycode_to_keysym(event.detail, 0)
    for name in dir(XK):
        if name[:3] == "XK_" and getattr(XK, name) == keysym:
            return name[3:]
    return "[%d]" % keysym
     
def check_valid_event(reply):
    if reply.category != record.FromServer:
        return 
    if reply.client_swapped:
        return
    if not len(reply.data) or ord(reply.data[0]) < 2:
        return

def delete_selection():
    subprocess.Popen("xsel -c", shell=True).wait()
        
