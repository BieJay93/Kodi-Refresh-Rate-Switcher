import xbmc
import xbmcgui

import rrSwitcher_config as rrsconfig
import rrSwitcher_player as rrsplayer
import rrSwitcher_monitor as rrsmonitor

xbmc.sleep(2000)

class rrsService:
 
    @staticmethod
    def run():
        xbmc.log("[RRSwitcher]: Addon started", level=xbmc.LOGINFO)
        rrsconfig.initSettings()
        
        monitor = rrsmonitor.rrsMonitor()
        player = rrsplayer.rrsPlayer()
            
        while not monitor.abortRequested():
            if monitor.waitForAbort(10):
                break

        xbmc.log("[RRSwitcher]: closing" , level=xbmc.LOGINFO)
        player.changeRefreshRate(rrsconfig.getDefaultRefreshRate())


if __name__ == '__main__':
    rrsService.run()