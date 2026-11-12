import xbmc
import rrSwitcher_config as rrsconfig
import os

class rrsPlayer(xbmc.Player):

    def __init__(self):
        super(xbmc.Player, self).__init__()

    def onAVStartedAV(self):
        xbmc.log("[RRSwitcher]: Playback started" , level=xbmc.LOGINFO)
        self.onAVStartedOrChanged()
    
    def onAVChange(self):
        xbmc.log("[RRSwitcher]: Playback changed" , level=xbmc.LOGINFO)
        self.onAVStartedOrChanged()

    def onPlayBackEnded(self):
        self.onPlayBackEndedOrStopped()

    def onPlayBackStopped(self):
        self.onPlayBackEndedOrStopped()
        
    def onPlayBackEndedOrStopped(self):
        xbmc.log("[RRSwitcher]: Playback stopped" , level=xbmc.LOGINFO)
        self.changeRefreshRate(rrsconfig.defaultRefreshRate)

    def onAVStartedOrChanged(self):
        hdrType = xbmc.getInfoLabel('VideoPlayer.HdrType')
        if hdrType:
            xbmc.log("[RRSwitcher]: HDR type: %s" %(hdrType), level=xbmc.LOGINFO)
        if not rrsconfig.enableDurationCheck:
            # We do not care about video length, just change the refresh
            self.changeRefreshRate(xbmc.getInfoLabel('Player.Process(VideoFps)'), hdrType)
        else:
            mediaDuration = xbmc.getInfoLabel('Player.Duration(hh:mm:ss)')
            xbmc.log("[RRSwitcher]: raw mediaDuration=%s" %(mediaDuration) , level=xbmc.LOGINFO)
            try:
                # the Player.Duration returns hours:minutes:seconds, we convert this to seconds
                durationlist = mediaDuration.split(":")
                mediaDuration = int(durationlist[0])*60*60 + int(durationlist[1])*60 + int(durationlist[2])
            except:
                mediaDuration = 9999
            xbmc.log("[RRSwitcher]: media duration in seconds: %s , minimalDuration in config: %s" %(mediaDuration, rrsconfig.minimalDuration) , level=xbmc.LOGINFO)
            if (mediaDuration > rrsconfig.minimalDuration):
                self.changeRefreshRate(xbmc.getInfoLabel('Player.Process(VideoFps)'), hdrType)



    def changeRefreshRate(self, refreshRate, HDR=None):
        if(float(refreshRate) != rrsconfig.currentRefreshRate):
            rrsconfig.currentRefreshRate = float(refreshRate)
            primary = ""
            additionalStr = ""
            hdrStr = ""

            if(rrsconfig.isPrimaryMonitor):
                primary = "--primary"
            if(rrsconfig.additionalConfig.strip()):
                additionalStr = rrsconfig.additionalConfig
            if(rrsconfig.enableHDR and HDR):
                hdrStr = "--color-mode bt2100"
            
            xbmc.log("[RRSwitcher]: Changing refresh rate to: %s" % rrsconfig.getCurrentRefreshRate() , level=xbmc.LOGINFO)
            gdctlStr = '%s set --logical-monitor %s --monitor=%s --mode=%s@%s %s %s' % (rrsconfig.gdctlPath, primary, rrsconfig.defautlMonitorName, rrsconfig.defaultResolution, rrsconfig.getCurrentRefreshRate(), additionalStr, hdrStr)
            xbmc.log("[RRSwitcher]: Gdctl String: %s" % gdctlStr, level=xbmc.LOGINFO)
            os.system(gdctlStr)
