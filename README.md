# Python_ToolBox
Ce projet a pour objectif de regrouper un ensemble de d'outils python pour les usages suivants :
- Création de backup ;
- Vérification des disques ;
- Analyse de logs de sécurité ;
- Monitoring de performances ;

Voici comment se structure le projet :
├── Admin_sys
│   ├── Alerting_Usage
│   │   ├── CPU_Charge_Alerting.py
│   │   └── Disk_usage_Alerting.py
│   ├── Automate_Log-Rotation.py
│   ├── Backup_file.py
│   ├── Metrics-system_getter
│   │   ├── Metrics_getter.py
│   │   ├── Network_pin.py
│   │   ├── Service_Check_Status.py
│   │   ├── System_uptime.py
│   │   └── User_Account_Management.py
│   └── SRV-Conf
│       ├── conf-ip.py
│       ├── data
│       ├── templates
│       └── test.yaml
├── DevOps
│   └── Secret_HashiCorp_Vault.py
├── Docker
│   └── docker_py_lab.py
├── gui.py
├── icons
│   ├── home.png
│   └── parameters.png
├── README.md
└── SOC
    ├── Check_Batch_History.py
    ├── Check_Open_Ports.py
    ├── Hash_Checker.py
    ├── IP_Check_VirusTotal.py
    ├── Log_Analyze.py
    └── Simple_IDS.py