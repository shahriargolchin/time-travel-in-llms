from pathlib import Path
from helpers.logging_config import configure_logger

logger = configure_logger(__name__)


class ExperimentResultSaver:
    def __init__(self, df, filepath, experiment, save_intermediate_results):
        self.df = df
        self.filepath = Path(filepath)
        self.experiment = Path(experiment)
        self.save_intermediate_results = save_intermediate_results

    def check_or_create_experiment_result_folder(self):
        if not self.experiment.exists():
            self.experiment.mkdir(parents=True, exist_ok=True)

    def save_to_csv(self):
        if self.save_intermediate_results:
            self.check_or_create_experiment_result_folder()
            csv_filepath = self.experiment / self.filepath.name
            self.df.to_csv(
                csv_filepath,
                encoding="utf-8",
                index=False,
            )
            logger.info(f"File saved to: {csv_filepath}")
