import os, sys

ROOT_DIR = os.path.abspath('../../')
sys.path.append(ROOT_DIR)

from src.backend.backend_test import run_test

run_test()

