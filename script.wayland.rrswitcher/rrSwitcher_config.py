import xbmc
import xbmcaddon

defautlMonitorName = ""
defaultResolution = ""
defaultRefreshRate = 60.0
currentRefreshRate = 0.0
isPrimaryMonitor = True
additionalConfig = ""


def getCurrentRefreshRate():
    global currentRefreshRate
    return "{:.3f}".format(currentRefreshRate)

def getDefaultRefreshRate():
    global defaultRefreshRate
    return "{:.3f}".format(defaultRefreshRate)

def initSettings():
    global defaultRefreshRate, defaultResolution, defautlMonitorName, isPrimaryMonitor, additionalConfig
    addonSettings = xbmcaddon.Addon('script.wayland.rrswitcher').getSettings()
    try:
        defautlMonitorName = addonSettings.getString('MonitorName')
    except:
        xbmc.log("[RRSwitcher]: Error while reading setting MonitorName, using default value", level=xbmc.LOGWARNING)
    try:
        defaultResolution = addonSettings.getString('Resolution')
    except:
        xbmc.log("[RRSwitcher]: Error while reading setting Resolution, using default value", level=xbmc.LOGWARNING)
    try:
        defaultRefreshRate = addonSettings.getNumber('RefreshRate')
    except:
        xbmc.log("[RRSwitcher]: Error while reading setting RefreshRate, using default value", level=xbmc.LOGWARNING)
    try:    
        isPrimaryMonitor = addonSettings.getBool('PrimaryMonitor')
    except:
        xbmc.log("[RRSwitcher]: Error while reading setting PrimaryMonitor, using default value", level=xbmc.LOGWARNING)
    try:    
        additionalConfig = addonSettings.getString('AdditionalConfig')
    except:
        xbmc.log("[RRSwitcher]: Error while reading setting AdditionalConfig, using default value", level=xbmc.LOGWARNING)
    
    xbmc.log("[RRSwitcher]: Config updated" , level=xbmc.LOGINFO)
