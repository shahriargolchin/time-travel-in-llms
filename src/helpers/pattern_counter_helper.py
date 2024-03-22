import re


class PatternCounter:
    def __init__(self, evaluations, pattern_severity):
        self.evaluations = evaluations
        self.pattern_severity = pattern_severity

    def count_patterns(self):
        counts = {pattern: 0 for pattern in self.pattern_severity.keys()}
        for evaluation in self.evaluations:
            for pattern in self.pattern_severity.keys():
                if re.search(pattern, evaluation):
                    counts[pattern] += 1
        return counts

    def save_results(self, result_filename, counts):
        with open(result_filename, "w") as f:
            f.write(
                f"{'Metric':<15} {'Match Type':<30}{'Count':<10} {'Contaminated'}\n"
            )
            f.write(f"{'-' * 75}\n")
            for pattern, count in counts.items():
                f.write(
                    f"{'GPT-4 ICL:':<15} {pattern:<30}{count:<10} {'Yes' if count >= self.pattern_severity[pattern] else 'No'}\n"
                )

    def evaluate_and_save_results(self, result_filename):
        counts = self.count_patterns()
        self.save_results(result_filename, counts)
