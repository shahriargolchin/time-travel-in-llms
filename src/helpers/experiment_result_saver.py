from pathlib import Path
from helpers.logging_config import configure_logger

logger = configure_logger(__name__)


class ExperimentResultSaver:
    def __init__(self, df, filepath, experiment, save_intermediate_results):
        self.df = df
        self.filepath = Path(filepath)
        self.experiment = experiment
        self.save_intermediate_results = save_intermediate_results
        # Determine Absolute path dynamically
        self.base_dir = Path(__file__).resolve().parent.parent.parent
        self.results_dir = self.base_dir / "results" / self.experiment

    def check_or_create_experiment_result_folder(self):
        if not self.results_dir.exists():
            self.results_dir.mkdir(parents=True, exist_ok=True)

    def save_to_csv(self):
        if self.save_intermediate_results:
            self.check_or_create_experiment_result_folder()
            csv_filepath = self.results_dir / self.filepath.name
            self.df.to_csv(
                csv_filepath,
                encoding="utf-8",
                index=False,
            )
            logger.info(f"File saved to: {csv_filepath}")
