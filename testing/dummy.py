#
# hsl3dummy - dummy hsl3 framework
#   Written by Ralf Dragon <hypnotoad@lindra.de>
#   Copyright (C) 2026 Ralf Dragon
#
# This program is freely distributable per the following license:
#
#  Permission to use, copy, modify, and distribute this software and its
#  documentation for any purpose and without fee is hereby granted,
#  provided that the above copyright notice appears in all copies and that
#  both that copyright notice and this permission notice appear in
#  supporting documentation.
#
#  I DISCLAIM ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING ALL
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO EVENT SHALL I
#  BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY
#  DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS,
#  WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION,
#  ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
#  SOFTWARE.

import copy
import logging
import json
import threading

class DebugSection:
    def log(self, text):
        logging.debug("debug section: {}".format(text))
    
class Hsl3Framework:
    def __init__(self, configfile):
        with open(configfile) as f:
            self.config = json.load(f)["module"]
        self.debug = DebugSection()
        self.inputs = self.interfaces_to_dict(self.config["inputs"])
        self.outputs = self.interfaces_to_dict(self.config["outputs"])
        self.timers = self.interfaces_to_dict(self.config["timers"])
        self.module = None
        self.is_mock = True
        self.lock = threading.Lock()

    def set_module(self, module):
        # needed to simulate timer callbacks
        self.module = module
        
    def interfaces_to_dict(self, interface_list):
        return {item["identifier"]: item for item in interface_list}
        
    def create_debug_section(self):
        return self.debug

    def get_module_id(self):
        return self.config["id"]

    def run_in_context(self, func, *args):
        func(*args[0])

    def set_output(self, key, value):
        assert key in self.outputs
        if self.outputs[key]["type"] == "string":
            assert type(value) == bytes
        else:
            assert type(value) == float or type(value) == int
        self.output_state[key] = value
        logging.debug("output[{}] := {}".format(key, value))

    def set_timer(self, key, interval_s):
        assert key in self.timers
        assert self.module is not None

        with self.lock:
            self.timers[key] = Hsl3Slot(interval_s)
        
        def timer_finished():
            with self.lock:
                t = copy.deepcopy(self.timers)
            t[key].changed = True
            self.module.on_timer(t)

        if interval_s:
            threading.Timer(interval_s, timer_finished).start()
            
        
class Hsl3Slot:
    def __init__(self, value):
        self.value = value
        self.changed = False

class Hsl3Slots:
    def __init__(self, elements):
        self.elements = {key: Hsl3Slot(value) for key, value in elements.items()}

    def __getitem__(self, key):
        return self.elements[key]
        

