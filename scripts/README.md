## Detailed Explanation of Experiments:

As pointed out in the chief README file of the project, for each setting mentioned in the paper there is a corresponding bash file that can be run to replicate the results. 

We also provide a `general_script.sh`, with which you can implement each of our methodologies for detecting data contamination within your data. The necessary standard arguments are supplied already in this file so that you can derive the optimal results from our top-performing technique. Considering that our best strategy is GPT-4 in-context learning evaluation (GPT-4 ICL), this is the default detection method in this script. Nonetheless, experimenting with any methods discussed in the paper is feasible by enabling them through the arguments outlined in the following section.

Since our technique is inexpensive and capable of detecting contamination using a small subset of data (you can use a minimum of ten to a few hundred examples, based on your need), a CSV file is used as input to this project. This is useful when conducting a comparative analysis on the intermediate results obtained from multiple experiments.

## Detailed Explanation of Input Arguments:

- `filepath` (required): The filepath to the input CSV file that is used for data contamination detection. As mentioned, this can be a small part of your entire dataset.

- `task` (required): The task that corresponds to your dataset. Tasks available include classification (`cls`), natural language inference (`nli`), summarization (`sum`), and extreme summarization (`xsum`).

- `dataset` (required): The actual name of the dataset that your data belongs to.

- `split` (required): The split of the dataset that your data belongs to. The split should be one of `train`, `validation`, or `test`.

- `model` (required): The snapshot of the OpenAI model that serves as the underlying model.

- `text_column` (required): The name of the column that contains dataset instances in the input CSV file.

- `experiment` (required): The directory that all the output files will be saved in.

- `process_guided_replication` (required): If the replication should be implemented via guided instructions. This replication is necessary for all evaluations mentioned in the paper.

- `process_general_replication` (conditional): If the replication should be performed via general instructions. This replication is required only when `bleurt_eval` and `rouge_eval` are employed as evaluation methods.

- `label_column` (conditional): The name of the column that contains the labels corresponding to the dataset instances in the input CSV file. This is required if the task comes with labels such as `cls` and `nli`.

- `should_split_text` (conditional): If the dataset instances need to be randomly split. This is required for datasets other than NLI. Splitting is performed differently based on the structure of each data point. Refer to the paper for more details. For the data that has already been pre-split, you can skip the splitting process. Ensure that the pre-split data is divided into `first_piece` and `second_piece` columns.

- `icl_eval` (optional): Specifies if evaluations should be conducted based on GPT-4 ICL. This is our top-performing evaluation method.

- `bleurt_eval` (optional): Specifies if evaluations should be conducted based on BLEURT scores. Make sure all the dependencies are installed.

- `rouge_eval` (optional): Specifies if evaluations should be conducted based on ROUGE-L scores.

- `min_p` (optional): Minimum percentage for the range of [min_p, max_p] when dataset instances are randomly split according to their length to generate initial segments of random lengths.

- `max_p` (optional): Maximum percentage for the range of [min_p, max_p] when dataset instances are randomly split according to their length to generate initial segments of random lengths.

- `seed` (optional): Seed for the random text split mechanism.
