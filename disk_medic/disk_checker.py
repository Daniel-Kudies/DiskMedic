import os
import time
import logging
import subprocess

class DiskChecker:
    def __init__ (self, operating_system):
        self.operating_system = operating_system

    def check_disks(self):
        try:
            match self.operating_system:
                case "Windows":
                    self.check_windows()
                case "Linux":
                    self.check_linux()
                case _:
                    logging.error("Unsupported Opperatingsystem: %s", self.operating_system)

        except Exception as e:
            print(e)

    def check_windows(self):
        try:
            possible_drives = [drive.replace("\\", "") for drive in os.listdrives()]
            logging.debug("List of the Drives: %s", possible_drives)
            for drives in possible_drives:
                windows_command = ["chkdsk", drives, "/R", "/X"]
                command_str = ' '.join(windows_command)
                logging.debug("Command for the run: %s", command_str)
                process = subprocess.Popen(windows_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if drives =="C:":
                    stdout, stderr = process.communicate(input="J\n")
                if stdout:
                    logging.info("Disk Check Output for Disk: %s \n %s", drives, stdout)
                if stderr:
                    logging.error("Disk Check Error for Disk: %s \n %s", drives, stderr)
            time.sleep(1)

        except subprocess.CalledProcessError as e:
            logging.error(e)
        except subprocess.TimeoutExpired as e:
            logging.error(e)
        except Exception as e:
            logging.error(e)

    def check_linux(self):
        # Using fsck for linux
        print("checking on linux")