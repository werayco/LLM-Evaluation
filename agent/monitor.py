from evidently import Dataset, DataDefinition
from evidently.descriptors import (
    LLMEval,
    DeclineLLMEval,
    FaithfulnessLLMEval,
    BERTScore,
    SentenceCount, CorrectnessLLMEval , IncludesWords
)
# CorrectnessLLMEval is basically using an AI Judge to compare the answers and the model's answer using OPENAI's API
from agent.process import run_agent
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import time
import logging

dataframe = pd.read_csv(r"./evals.csv")
quest = list(dataframe["questions"].to_list())
ModelResponse = [run_agent(str(question), int(time.time())) for question in quest]
dataframe["model_output"] = ModelResponse

datadef = DataDefinition(text_columns=["questions", "answers", "model_output"])
evidentlyAIDataframe = Dataset.from_pandas(dataframe, datadef) # this wraps our dataset to a evidently dataset
evidentlyAIDataframe.add_descriptors(descriptors=[IncludesWords(column_name="model_output", words_list=["Hello", "good day"], alias="include words"),BERTScore(columns=["model_output", "answers"], alias="BertScore")])
newdf = evidentlyAIDataframe.as_dataframe().to_csv("./report.csv")
print(newdf)
