class Guided:
    def __init__(self) -> None:
        self.prompts = {
            "cls": """INSTRUCTION:
You are provided with the FIRST PIECE of an instance from the {split_name} split of the {dataset_name} dataset.
Finish the SECOND PIECE of the instance as EXACTLY appeared in the dataset.
ONLY rely on the original form of the instance in the dataset to finish the SECOND PIECE.

LABEL: {label}

FIRST PIECE:
{first_piece}

SECOND PIECE:
""",
            "nli": """INSTRUCTION:
You are provided with SENTENCE 1 from the {split_name} split of the {dataset_name} dataset.
Finish SENTENCE 2 as appeared in the dataset.
SENTENCE 2 MUST EXACTLY match the instance in the dataset.

SENTENCE 1:
{first_piece}

LABEL: {label}

SENTENCE 2:
""",
            "sum": """INSTRUCTION:
You are provided with the FIRST PIECE of a summary from the {split_name} split of the {dataset_name} dataset.
Finish the SECOND PIECE of the summary as EXACTLY appeared in the dataset.
ONLY rely on the original form of the summary in the dataset to finish the SECOND PIECE.

FIRST PIECE:
{first_piece}

SECOND PIECE:
""",
            "xsum": """INSTRUCTION:
You are provided with the FIRST PIECE of a one-sentence summary from the {split_name} split of the {dataset_name} dataset.
Finish the SECOND PIECE of the summary as EXACTLY appeared in the dataset.
ONLY rely on the original form of the summary in the dataset to finish the SECOND PIECE.

FIRST PIECE:
{first_piece}

SECOND PIECE:
""",
        }

    def get_prompt(self, prompt_type):
        return self.prompts.get(prompt_type, "Invalid prompt type")
