from Foundation import *
from AppKit import *
from Renaissance import *

import WebKit

import random

class AppDelegate(NSObject):

    documentArea = None
    searchField = None
    bottomBar = None

    def windowWillClose_(self, notification):
        NSApp().terminate_(self)

    def quit_(self, notification):
        NSApp().terminate_(self)

    def close_(self, notification):
        NSApp().terminate_(self)

    def applicationDidFinishLaunching_(self, notification):
        NSLog("before loading scrap_window")
        NSBundle.loadGSMarkupNamed_owner_('scrap_window', self)
        NSLog("after loading scrap_window")

        # modify some things
        self.bottomBar.setStringValue_("bottom bar")
        self.searchField.cell().setPlaceholderString_("search here")

        url = NSURL.alloc().init()
        self.documentArea.mainFrame().loadHTMLString_baseURL_("<div>it works !!!</div>", url)

    def bundleDidLoadGSMarkup_(self, notification):
        NSLog("bindleDidLoadGSMarkup")
    
    def open_(self, notification):
        filetypes = ['scrap']
        panel = NSOpenPanel.openPanel()
        result = panel.runModalForDirectory_file_types_(None, None, filetypes)
        if result == NSOKButton:
            self.pathname = panel.filenames()[0]
            NSLog('Loading ' + self.pathname)

    # application delegate functions


def main():
    app = NSApplication.sharedApplication()
    # create an app delegate
    delegate = AppDelegate.alloc().init()
    app.setDelegate_(delegate)
    NSBundle.loadGSMarkupNamed_owner_('scrap_menu', delegate)
    NSApp().run()

if __name__ == '__main__':
    main()
