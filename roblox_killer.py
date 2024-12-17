import ctypes
import os
import sys
import time

import psutil


class RobloxKiller:
    def __init__(self, process_name="roblox", check_interval=2):
        self.process_name = process_name.lower()
        self.check_interval = check_interval

    @staticmethod
    def hide_console():
        """Hides the console window if on Windows"""
        if sys.platform == "win32":
            ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

    def kill_process(self):
        """Continuously checks and kills any processes matching the process name"""
        while True:
            try:
                for process in psutil.process_iter(["pid", "name"]):
                    # Match process name containing 'roblox'
                    if self.process_name in process.info["name"].lower():
                        try:
                            os.kill(process.info["pid"], 9)  # Kill process
                        except (psutil.NoSuchProcess, PermissionError):
                            pass
            except Exception as e:
                # Log exceptions to a file or handle gracefully
                print(f"Error: {e}")
            time.sleep(self.check_interval)

    def run(self):
        """Hides the console and starts killing processes"""
        self.hide_console()
        self.kill_process()


if __name__ == "__main__":
    killer = RobloxKiller()
    killer.run()
