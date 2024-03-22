import os
import sys


class BleurtLoader:
    def __init__(self, checkpoint="BLEURT-20", bleurt_folder="bleurt_scorer"):
        self.base_dir = os.path.dirname(__file__)
        self.dependencies_path = self.get_dependencies_path()
        self.bleurt_path = self.get_bleurt_path(bleurt_folder)
        self.checkpoint = checkpoint
        self.model_path = os.path.join(self.bleurt_path, self.checkpoint)

    def get_dependencies_path(self):
        return os.path.join(self.base_dir, "../../dependencies")

    def get_bleurt_path(self, bleurt_folder):
        return os.path.join(self.dependencies_path, bleurt_folder)

    @staticmethod
    def add_path_to_sys(path):
        if path not in sys.path:
            sys.path.insert(0, path)

    def prepare_module(self):
        self.add_path_to_sys(self.dependencies_path)
        self.add_path_to_sys(self.bleurt_path)
