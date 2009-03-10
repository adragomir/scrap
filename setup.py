from distutils.core import setup
import py2app

NAME = 'Scrap'
SCRIPT = 'scrap.py'
VERSION = '0.1'
ICON = 'scrap'
ID = 'org.adragomir.scrap'
COPYRIGHT = 'Copyright 2009 Andrei Dragomir'
DATA_FILES = ['English.lproj', 'data', 'scrap_menu.gsmarkup', 'scrap_window.gsmarkup']

plist = dict(
    CFBundleIconFile            = ICON,
    CFBundleName                = NAME,
    CFBundleShortVersionString  = ' '.join([NAME, VERSION]),
    CFBundleGetInfoString       = NAME,
    CFBundleExecutable          = NAME,
    CFBundleIdentifier          = ID, 
    NSHumanReadableCopyright    = COPYRIGHT
)


app_data = dict(script=SCRIPT, plist=plist)
py2app_opt = dict(frameworks=['Renaissance.framework', 'WebKit.framework'],)
options = dict(py2app=py2app_opt,)

setup(
  data_files = DATA_FILES,
  app = [app_data],
  options = options,
)
