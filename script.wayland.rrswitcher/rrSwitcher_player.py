import xbmc
import rrSwitcher_config as rrsconfig
import os

class rrsPlayer(xbmc.Player):

    def __init__(self):
        super(xbmc.Player, self).__init__()

    def onAVStartedAV(self):
        xbmc.log("[RRSwitcher]: Playback started" , level=xbmc.LOGINFO)
        self.changeRefreshRate(xbmc.getInfoLabel('Player.Process(VideoFps)'))
    
    def onAVChange(self):
        xbmc.log("[RRSwitcher]: Playback changed" , level=xbmc.LOGINFO)
        self.changeRefreshRate(xbmc.getInfoLabel('Player.Process(VideoFps)'))

    def onPlayBackEnded(self):
        self.onPlayBackEndedOrStopped()

    def onPlayBackStopped(self):
        self.onPlayBackEndedOrStopped()
        
    def onPlayBackEndedOrStopped(self):
        xbmc.log("[RRSwitcher]: Playback stopped" , level=xbmc.LOGINFO)
        self.changeRefreshRate(rrsconfig.defaultRefreshRate)

    def changeRefreshRate(self, refreshRate):
        if(float(refreshRate) != rrsconfig.currentRefreshRate):
            rrsconfig.currentRefreshRate = float(refreshRate)
            primary = ""
            additionalStr = ""

            if(rrsconfig.isPrimaryMonitor):
                primary = "--primary"
            if(rrsconfig.additionalConfig.strip()):
                additionalStr = rrsconfig.additionalConfig
            
            xbmc.log("[RRSwitcher]: Changing refresh rate to: %s" % rrsconfig.getCurrentRefreshRate() , level=xbmc.LOGINFO)
            gdctlStr = 'gdctl set --logical-monitor %s --monitor=%s --mode=%s@%s %s' % (primary, rrsconfig.defautlMonitorName, rrsconfig.defaultResolution, rrsconfig.getCurrentRefreshRate(), additionalStr)
            xbmc.log("[RRSwitcher]: Gdctl String: %s" % gdctlStr, level=xbmc.LOGINFO)
            os.system(gdctlStr)