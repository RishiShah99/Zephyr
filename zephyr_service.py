import win32serviceutil
import win32service
import win32event
import servicemanager
import logging
import os
from Test import wake_word_callback, WakeWordDetector

class ZephyrService(win32serviceutil.ServiceFramework):
    _svc_name_ = "ZephyrService"
    _svc_display_name_ = "Zephyr Voice Assistant Service"
    _svc_description_ = "A voice assistant service that listens for a wake word and provides assistance."

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.stop_requested = False

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.stop_requested = True

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ""))
        self.main()

    def main(self):
        keyword_path = "path/to/your/keyword/file.ppn"
        detector = WakeWordDetector(keyword_path)
        while not self.stop_requested:
            detector.start(wake_word_callback)

if __name__ == "__main__":
    win32serviceutil.HandleCommandLine(ZephyrService)