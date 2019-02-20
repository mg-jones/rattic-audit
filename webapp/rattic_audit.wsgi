import os
import sys


app_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, app_dir)

from rattic_audit import app as application
