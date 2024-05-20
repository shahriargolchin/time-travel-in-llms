from prompts.general_instructions import General
from prompts.guided_instructions import Guided
from helpers.metric_helper import Rouge, Bleurt, ICL
from services.argparse_handler import ArgumentParser
import pandas as pd
from core.evaluation_phase import Alg1EvalPhase, Alg2EvalPhase
from core.replication_phase import ReplicationPhase
from helpers.logging_config import configure_logger


logger = configure_logger(__name__)


if __name__ == "__main__":
    args = ArgumentParser().parse_args()
    df = pd.read_csv(args.filename, encoding="utf-8")

    if args.process_guided_replication:
        df = ReplicationPhase(
            df=df,
            args=args,
            instruction=Guided(),
            save_intermediate_results=True,
        ).process()

    if args.process_general_replication:
        df = ReplicationPhase(
            df=df,
            args=args,
            instruction=General(),
            save_intermediate_results=True,
        ).process()

    if args.rouge_eval:
        df = Alg1EvalPhase(
            df=df,
            args=args,
            scoring_tool=Rouge("rougeL"),
            save_intermediate_results=True,
        ).evaluate()

    if args.bleurt_eval:
        df = Alg1EvalPhase(
            df=df,
            args=args,
            scoring_tool=Bleurt(),
            save_intermediate_results=True,
        ).evaluate()

    if args.icl_eval:
        df = Alg2EvalPhase(
            df=df,
            args=args,
            scorer=ICL(args),
            pattern_severity={
                "Yes \\(exact match\\)": 1,
                "Yes \\(near\\-exact match\\)": 2,
            },
            save_intermediate_results=True,
        ).evaluate()

    logger.info("*** All process done! ***")
