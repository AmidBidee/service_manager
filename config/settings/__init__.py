"""
SERVICEMANAGER CONFIGURATION LOADER
"""
# tries to get environmental vairaible package
try:
    from decouple import config as getenv
except ModuleNotFoundError:
    from os import getenv

LIVE = False
ON_PREM = False
DEV = True

if LIVE:
    try:
        from config.settings.live import *
    except ImportError:
        from config.settings.onprem import *
if DEV:
    try:
        from config.settings.dev import *
    except Exception as e:
        raise(e)