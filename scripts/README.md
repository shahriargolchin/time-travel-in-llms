## Detailed Explanation of Experiments:

As pointed out in the chief README documentation of the project, corresponding bash files are available for each setting mentioned in the paper and these can be run to replicate the research findings. 

We also offer a `general_script.sh`, with which you can implement our methodology for identifying data contamination tailored to your own data. The necessary standard arguments are supplied already in this file so that you can derive the optimal results from our identification technique. Considering that our superior performing evaluation strategy is GPT-4 in-context learning evaluation (GPT-4 ICL), this is the default identification method in the mentioned script. Nonetheless, the inclusion of any methods detailed in the paper is feasible by enabling them through the arguments outlined in the next section.

Since our technique is inexpensive and is capable of identifying contamination using a small subset of data (you can use a minimum of ten to a few hundred examples, based on your need), a CSV file is used for input into this project. This is greatly useful when conducting a comparative analysis on the interim results obtained during the various experiments.


## Detailed Explanation of Input Arguments:

- `filename` (required): The CSV filename that is used for the detection of data contamination. As mentioned, this can be a small part of your entire dataset.

- `task` (required): The task that corresponds to your dataset. Tasks available include classification (`cls`), natural language inference (`nli`), summarization (`sum`), and extreme summarization (`xsum`).

- `dataset` (required): The actual name of the dataset that aligns with your data.

- `split` (required): The corresponding partition of the dataset to which data belongs.

- `model` (required): The OpenAI model snapshot used for detection of contamination. Options available include GPT-4 and GPT-3.5.

- `text_column` (required): The name of the column that contains your data points in the CSV file.

- `experiment` (required): The name of the directory in which the results should be stored under the `results` directory.

- `process_guided_replication` (required): If the replication should be implemented via guided instructions. This replication is necessary for any evaluations mentioned in the paper.

- `process_general_replication` (conditional): If the replication must be performed via general instructions. This replication is necessary only when `bleurt_eval` and `rouge_eval` are employed for evaluation methods.

- `label_column` (conditional): The name of the column that contains the labels of the data points. This is required if the task comes with labels such as `cls` and `nli`.

- `should_text_split` (conditional): If the data points need to be randomly split. This is required for datasets other than NLI. Splitting is performed different based on the structure of each data point. Refer to the paper for more details. For data that has already been pre-split, you can skip the splitting process. However, ensure that the data is divided into `first_piece` and `second_piece` columns.

- `icl_eval` (optional): Specifies that an evaluation should be conducted based on GPT-4 ICL (our top-performing evaluation).

- `bleurt_eval` (optional): Specifies that an evaluation should be conducted based on BLEURT. Make sure all the dependencies are installed beforehand.

- `rouge_eval` (optional): Specifies that an evaluation should be conducted based on ROUGE-L.

- `min_p` (optional): Minimum percentage for the range of [min_p, max_p] when data points are randomly split according to their length to generate initial segments of random lengths.

- `max_p` (optional): Maximum percentage for the range of [min_p, max_p] when data points are randomly split according to their length to generate initial segments of random lengths.

- `seed` (optional): Seed for the random text split mechanism.
