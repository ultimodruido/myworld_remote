"""
Module: settings
This module offers to fuction to save and read configuration on a local file.
"""
import json
from typing import Optional, Dict, List

# Configuration filename
FILE = 'myworld.conf'


def load_settings() -> Optional[Dict]:
    """
    Read stored settings from configuration files if existing
    :return: JSON dictionary with playground port and list of trains
    """
    try:
        with open(FILE, encoding='utf-8') as f:
            config = json.load(f)
            return config
    except:
        return None


def save_settings(port: str, rolling_stock: List[Dict[str, str]]) -> bool:
    """Stores the plavground express port and the list of train in a configuration file
    for future references"""
    # TODO; make a backup of the previous version?
    try:
        with open(FILE, mode='w', encoding='utf-8') as f:
            config = {
                'port': port,
                'rolling_stock': rolling_stock
            }
            json.dump(config, f, ensure_ascii=False)
            return True
    except:
        print('Error while savings settings')
        return False
