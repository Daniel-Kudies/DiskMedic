# DiskMedic-
DiskMedic is a comprehensive disk maintenance tool that automates essential tasks like Disk Cleanup, Defragmentation (for HDDs), Error Checking, and Disk Health Monitoring. Keep your drives clean, organized, and healthy effortlessly, ensuring optimal performance and reliability for your system.

DiskMedic/
├── .github
│   ├── configs
│   │   └── .pylintrc              # Contains the settings for the linting
│   ├── workflows
│   │   ├── pylint.yml             # Contains the workflow logic for the linting
│   │   └── security-audit.yml     # Contains the workflow logic for the Security Audit
├── disk_medic
│   ├── disk_checker.py            # Scans and repairs disk issues
│   ├── disk_cleaner.py            # Removes temporary files, system cache and other unnecessary files
│   ├── disk_defrager.py           # Organizes fragmented files (HDDs only)
│   ├── disk_health.py             # Check for potential hardware issues
│   └── main.py                    # Entry point to run the file organizer
├── tests                           # Directory for test cases
├── requirements.txt                # Dependencies for the project
├── README.md                       # Documentation file for the project


1. Disk Cleanup
Tool: cleanmgr.exe on Windows or third-party tools.
What It Does: Removes temporary files, system cache, internet files, and other unnecessary files.
How Often: Weekly or bi-weekly, depending on disk usage.
2. Disk Defragmentation (HDD only)
Tool: dfrgui.exe or third-party defragmenters.
What It Does: Organizes fragmented files, making HDDs more efficient and slightly faster.
How Often: Monthly, but do not use this for SSDs, as it can reduce their lifespan. SSDs handle data differently and don’t require defragmentation.
3. Error Checking
Tool: chkdsk on Windows.
What It Does: Scans and repairs file system errors, bad sectors, and other disk issues.
How Often: Monthly or after any unexpected shutdowns.
5. Disk Health Monitoring
Tool: Use tools like CrystalDiskInfo (Windows), SMART Utility (macOS), or smartctl (Linux).
What It Does: Checks for potential hardware issues, particularly on SSDs, by monitoring S.M.A.R.T. (Self-Monitoring, Analysis, and Reporting Technology) data.
How Often: Every few months, or set up automatic alerts if the tool supports it.

__GENUS          : 2
__CLASS          : MSStorageDriver_FailurePredictStatus
__SUPERCLASS     : MSStorageDriver
__DYNASTY        : MSStorageDriver
__RELPATH        : MSStorageDriver_FailurePredictStatus.InstanceName="SCSI\\Disk&Ven_Samsung&Prod_SSD\\4&2d010f8d&0&000
                   000_0"
__PROPERTY_COUNT : 4
__DERIVATION     : {MSStorageDriver}
__SERVER         : PC-DANIEL
__NAMESPACE      : root\wmi
__PATH           : \\PC-DANIEL\root\wmi:MSStorageDriver_FailurePredictStatus.InstanceName="SCSI\\Disk&Ven_Samsung&Prod_
                   SSD\\4&2d010f8d&0&000000_0"
Active           : True
InstanceName     : SCSI\Disk&Ven_Samsung&Prod_SSD\4&2d010f8d&0&000000_0
PredictFailure   : False
Reason           : 0
PSComputerName   : PC-DANIEL

__GENUS          : 2
__CLASS          : MSStorageDriver_FailurePredictStatus
__SUPERCLASS     : MSStorageDriver
__DYNASTY        : MSStorageDriver
__RELPATH        : MSStorageDriver_FailurePredictStatus.InstanceName="SCSI\\Disk&Ven_ST316031&Prod_0CS\\4&2d010f8d&0&00
                   0100_0"
__PROPERTY_COUNT : 4
__DERIVATION     : {MSStorageDriver}
__SERVER         : PC-DANIEL
__NAMESPACE      : root\wmi
__PATH           : \\PC-DANIEL\root\wmi:MSStorageDriver_FailurePredictStatus.InstanceName="SCSI\\Disk&Ven_ST316031&Prod
                   _0CS\\4&2d010f8d&0&000100_0"
Active           : True
InstanceName     : SCSI\Disk&Ven_ST316031&Prod_0CS\4&2d010f8d&0&000100_0
PredictFailure   : False
Reason           : 0
PSComputerName   : PC-DANIEL

__GENUS          : 2
__CLASS          : MSStorageDriver_FailurePredictStatus
__SUPERCLASS     : MSStorageDriver
__DYNASTY        : MSStorageDriver
__RELPATH        : MSStorageDriver_FailurePredictStatus.InstanceName="SCSI\\Disk&Ven_ST350041&Prod_8AS\\4&2d010f8d&0&00
                   0300_0"
__PROPERTY_COUNT : 4
__DERIVATION     : {MSStorageDriver}
__SERVER         : PC-DANIEL
__NAMESPACE      : root\wmi
__PATH           : \\PC-DANIEL\root\wmi:MSStorageDriver_FailurePredictStatus.InstanceName="SCSI\\Disk&Ven_ST350041&Prod
                   _8AS\\4&2d010f8d&0&000300_0"
Active           : True
InstanceName     : SCSI\Disk&Ven_ST350041&Prod_8AS\4&2d010f8d&0&000300_0
PredictFailure   : True
Reason           : 0
PSComputerName   : PC-DANIEL

__GENUS          : 2
__CLASS          : MSStorageDriver_FailurePredictStatus
__SUPERCLASS     : MSStorageDriver
__DYNASTY        : MSStorageDriver
__RELPATH        : MSStorageDriver_FailurePredictStatus.InstanceName="SCSI\\Disk&Ven_ST12000D&Prod_M0007-2GR116\\4&2d01
                   0f8d&0&000400_0"
__PROPERTY_COUNT : 4
__DERIVATION     : {MSStorageDriver}
__SERVER         : PC-DANIEL
__NAMESPACE      : root\wmi
__PATH           : \\PC-DANIEL\root\wmi:MSStorageDriver_FailurePredictStatus.InstanceName="SCSI\\Disk&Ven_ST12000D&Prod
                   _M0007-2GR116\\4&2d010f8d&0&000400_0"
Active           : True
InstanceName     : SCSI\Disk&Ven_ST12000D&Prod_M0007-2GR116\4&2d010f8d&0&000400_0
PredictFailure   : False
Reason           : 0
PSComputerName   : PC-DANIEL