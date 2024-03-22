class General:
    def __init__(self) -> None:
        self.prompts = {
            "cls": """INSTRUCTION:
Finish the SECOND PIECE based on the FIRST PIECE, such that these two pieces become a single instance with the following LABEL.

LABEL: {label}

FIRST PIECE:
{first_piece}

SECOND PIECE:
""",
            "nli": """INSTRUCTION:
Finish SENTENCE 2 based on SENTENCE 1, such that the following LABEL shows the logical relationship between SENTENCE 1 and SENTENCE 2.

SENTENCE 1:
{first_piece}

LABEL: {label}

SENTENCE 2:
""",
            "sum": """INSTRUCTION:
Finish the SECOND PIECE based on the FIRST PIECE, such that these two pieces become a single summary.

FIRST PIECE:
{first_piece}

SECOND PIECE:
""",
            "xsum": """INSTRUCTION:
Finish the SECOND PIECE based on the FIRST PIECE, such that these two pieces become a single one-sentence summary.

FIRST PIECE:
{first_piece}

SECOND PIECE:
""",
        }

    def get_prompt(self, prompt_type):
        return self.prompts.get(prompt_type, "Invalid prompt type")
