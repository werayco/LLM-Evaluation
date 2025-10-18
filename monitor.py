from evidently import Dataset, DataDefinition
from evidently.descriptors import (LLMEval, DeclineLLMEval, FaithfulnessLLMEval, BERTScore, SentenceCount)
from process import run_agent
import pandas as pd
import time
dataframe = pd.read_csv(r"./evals.csv")
quest = list(dataframe["questions"].to_list())
print(quest)
mdresponse = [run_agent(str(question), int(time.time())) for question in quest]
dataframe["model_output"] = mdresponse
datadef = DataDefinition(text_columns=["questions", "answers", "model_output"])
evidentlyAIDataframe = Dataset.from_pandas(dataframe, datadef) # this wraps our dataset to a evidently dataset
evidentlyAIDataframe.add_descriptors(descriptors=[BERTScore(columns=["model_output", "answers"])])
print(dataframe)
