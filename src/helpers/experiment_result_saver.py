import os
from pathlib import Path


class ExperimentResultSaver:
    def __init__(self, df, filename, experiment, save_intermediate_results):
        self.df = df
        self.experiment = experiment
        self.save_intermediate_results = save_intermediate_results
        self.file_path = Path(filename)

    def check_or_create_experiment_result_folder(self):
        experiment_folder_path = f"../../../results/{self.experiment}/"
        if not os.path.exists(experiment_folder_path):
            os.makedirs(experiment_folder_path)

    def save_to_csv(self):
        if self.save_intermediate_results:
            self.check_or_create_experiment_result_folder()
            self.df.to_csv(
                f"../../../results/{self.experiment}/{self.file_path.name}",
                encoding="utf-8",
                index=False,
            )
