import random
import numpy as np


class ResamplingProcessor:
    def __init__(self, num_resample):
        self.num_resample = num_resample

    def _resample(self, scores):
        means = []
        for _ in range(self.num_resample):
            resamples = random.choices(scores, k=len(scores))
            means.append(np.mean(resamples))

        return means

    def compute_p_value(self, scores_general, scores_guided):
        resampled_scores_general = self._resample(scores_general)
        resampled_scores_guided = self._resample(scores_guided)

        count = sum(
            avg_guided > avg_general
            for avg_guided, avg_general in zip(
                resampled_scores_guided, resampled_scores_general
            )
        )
        return 1 - (count / self.num_resample)

    def save_results(self, general, guided, metric, result_filename):
        p_value = self.compute_p_value(scores_general=general, scores_guided=guided)
        metric_score = f"{metric.upper()} score:"

        with open(result_filename, "w") as f:
            f.write(f"{'Metric':<20} {'p-value':<10} {'Significance'}\n")
            f.write(f"{'-' * 50}\n")
            p_value_str = f"{p_value:.3f}"
            f.write(
                f"{metric_score:<20} {p_value_str:<10} {'Significant' if p_value <= 0.05 else 'Not Significant'}\n"
            )
