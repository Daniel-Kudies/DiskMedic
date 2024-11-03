import logging
import platform
from disk_checker import DiskChecker
from disk_health import DiskHealth

def set_up_logging():
    logging.basicConfig(level=logging.DEBUG, encoding='utf-8', format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.FileHandler("disk_medic.log"), logging.StreamHandler()])

def main():
    try:
        set_up_logging()

        logging.info("Starting the DiskMedic...")
        operation_os = platform.system()

        # dc = DiskChecker(operating_system=operation_os)
        dh = DiskHealth(operating_system=operation_os)

        dh.check_health()
        # dc.check_disks()
        logging.info("Ending the Disk Medic.")

    except Exception as e:
        logging.error(e)

if __name__ == "__main__":
    main()