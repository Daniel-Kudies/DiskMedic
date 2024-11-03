# Linux lbslk
# Windows Get-PhysicalDisk | Select-Object -Property DeviceID, OperationalStatus, HealthStatus
import re
import logging
import subprocess

class DiskHealth:
    def __init__(self, operating_system):
        self.operating_system = operating_system

    def check_health(self):
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
            windows_command = r'powershell -Command "Get-WmiObject -Namespace root\wmi -Class MSStorageDriver_FailurePredictStatus | Select-Object InstanceName, Active, PredictFailure"'
            logging.debug("Using Command: %s", windows_command)
            process = subprocess.Popen(windows_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
            stdout, stderr = process.communicate()
            if stdout:
                drive_infos = self.return_drives_windows(data=stdout.splitlines())
                for line in drive_infos:
                    logging.info("InstanceName: %s, Active: %s, PredictFailure: %s", line["InstanceName"], line["Active"], line["PredictFailure"])

            if stderr:
                logging.error("Command Error: %s", stderr)
            process.kill()

        except Exception as e:
            print(e)

    def return_drives_windows(self, data):
        drive_infos = []
        for line in data[2:]:
            parts = line.split()
            if len(parts) >= 3:
                instance_name = " ".join(parts[:-2])
                active = parts[-2]
                predict_failure = parts[-1]
                drive_infos.append({"InstanceName": instance_name, "Active": active, "PredictFailure": predict_failure})
        drive_infos.pop(0)
        return drive_infos

    def check_linux(self):
        try:
            print("hi")
        except Exception as e:
            print(e)