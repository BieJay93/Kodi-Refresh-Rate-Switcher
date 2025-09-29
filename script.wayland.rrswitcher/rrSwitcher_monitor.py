import xbmc
import rrSwitcher_config as rrsconfig

class rrsMonitor(xbmc.Monitor):

    def __init__(self):
        super(xbmc.Monitor, self).__init__()

    def onSettingsChanged(self):
        rrsconfig.initSettings()