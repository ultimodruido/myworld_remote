"""
Module: settings
This module offers to function to save and read configuration on a local file.
"""
import json
from typing import Optional, Dict, List

# Configuration filename
FILE = 'myworld.conf'
VERSION = '0.1'


def load_settings() -> Optional[Dict]:
    """
    Read stored settings from configuration files if existing
    :return: JSON dictionary with playground port and list of trains
    """
    try:
        with open(FILE, encoding='utf-8') as f:
            config = json.load(f)
            print('[I] Settings: settings loaded')
            return config
    except:
        print('[E] Settings: error while loading settings')
        return None


def save_settings(port: str, rolling_stock: List[Dict[str, str]]) -> bool:
    """Stores the plavground express port and the list of train in a configuration file
    for future references"""
    # TODO; make a backup of the previous version?
    try:
        with open(FILE, mode='w', encoding='utf-8') as f:
            config = {
                'version': VERSION,
                'port': port,
                'rolling_stock': rolling_stock
            }
            json.dump(config, f, ensure_ascii=False)
            print('[I] Settings: settings saved')
            return True
    except:
        print('[E] Settings: error while savings settings')
        return False
