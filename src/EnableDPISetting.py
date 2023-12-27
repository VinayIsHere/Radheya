import ctypes

PROCESS_PER_MONITOR_DPI_AWARE = 2

def EnableWindowsDPIAware():
    ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DPI_AWARE)