class ICLEvaluation:
    def __init__(self):
        self.prompts = {
            "gpt4_icl_prompt": """INSTRUCTION:
You are provided with a reference text and a candidate text.
The candidate text is a generated replica of the reference text.
Your task is to determine if the candidate text is an exact or near-exact match of the reference text.
Near-exact match candidates must PRECISELY match the reference candidates in terms of sentence structure, overlap, and contextual similarity.
Respond only with 'Yes' or 'No'.
---
Example 1:

REFERENCE TEXT:
The cat waited at the top.

CANDIDATE TEXT:
The cat waited at the top.

ANSWER: Yes (exact match)
---
Example 2:

REFERENCE TEXT:
icy surface of Jupiter's largest moon, Ganymede. These irregular masses may be rock formations, supported by Ganymede's icy shell for billions of years.

CANDIDATE TEXT:
icy surface of Jupiter's largest moon, Ganymede. These irregular masses may be rock formations, supported by Ganymede's icy shell for billions of years. This discovery supports the theory that Ganymede has a subsurface ocean. Scientists used gravity data from NASA's Galileo spacecraft to create a geophysical model of the interior of Ganymede.

ANSWER: Yes (near-exact match)
---
Example 3:

REFERENCE TEXT:
50th Anniversary of Normandy Landings lasts a year.

CANDIDATE TEXT:
The 50th anniversary celebration of the first Normandy landing will last a year.

ANSWER: Yes (near-exact match)
---
Example 4:

REFERENCE TEXT:
Microsoft's Hotmail has raised its storage capacity to 250MB.

CANDIDATE TEXT:
Microsoft has increased the storage capacity of its Hotmail e-mail service to 250MB.

ANSWER: Yes (near-exact match)
---
Example 5:

REFERENCE TEXT:
{reference_text}

CANDIDATE TEXT:
{candidate_text}

ANSWER:
"""
        }

    def get_prompt(self, prompt_type):
        return self.prompts.get(prompt_type, "Invalid prompt type")
