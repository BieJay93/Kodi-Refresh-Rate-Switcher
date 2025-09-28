import xbmc
import xbmcgui

import rrSwitcher_config as rrsconfig
import rrSwitcher_player as rrsplayer

xbmc.sleep(2000)

class rrSwitcherService:
 
    @staticmethod
    def run():
        xbmc.log("[RRSwitcher]: Addon started", level=xbmc.LOGINFO)
        rrsconfig.initSettings()
        
        monitor = xbmc.Monitor()
        player = rrsplayer.rrsPlayer()
            
        while not monitor.abortRequested():
            if monitor.waitForAbort(10):
                break

        xbmc.log("[RRSwitcher]: closing" , level=xbmc.LOGINFO)
        player.changeRefreshRate(rrsconfig.getDefaultRefreshRate())


if __name__ == '__main__':
    rrSwitcherService.run()