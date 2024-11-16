import pandas

from pandas import DataFrame

from typing import Dict, List

def read_from(filename: str) -> DataFrame:
    return pandas.read_csv(
        "dataset.csv",
        dtype={
            "YearStart": "int64",
            "YearEnd": "int64",
            "LocationAbbr": "object",
            "LocationDesc": "object",
            "DataSource": "object",
            "Topic": "object",
            "Question": "object",
            "Response": "float64",
            "DataValueUnit": "object",
            "DataValueType": "object",
            "DataValue": "object",
            "DataValueAlt": "float64",
            "DataValueFootnoteSymbol": "object",
            "DatavalueFootnote": "object",
            "LowConfidenceLimit": "float64",
            "HighConfidenceLimit": "float64",
            "StratificationCategory1": "object",
            "Stratification1": "object",
            "StratificationCategory2": "float64",
            "Stratification2": "float64",
            "StratificationCategory3": "float64",
            "Stratification3": "float64",
            "GeoLocation": "object",
            "ResponseID": "float64",
            "LocationID": "int64",
            "TopicID": "object",
            "QuestionID": "object",
            "DataValueTypeID": "object",
            "StratificationCategoryID1": "object",
            "StratificationID1": "object",
            "StratificationCategoryID2": "float64",
            "StratificationID2": "float64",
            "StratificationCategoryID3": "float64",
            "StratificationID3": "float64",
        },
    ).drop(
        columns=[
            "LocationDesc",
            "Response",
            "DataValueAlt",
            "DataSource",
            "DataValueUnit",
            "DataValueFootnoteSymbol",
            "DatavalueFootnote",
            "StratificationCategory1",
            "StratificationCategory2",
            "Stratification2",
            "StratificationCategory3",
            "Stratification3",
            "GeoLocation",
            "ResponseID",
            "LocationID",
            "LocationDesc",
            "LocationID",
            "DataValueTypeID",
            "StratificationID1",
            "StratificationCategoryID2",
            "StratificationID2",
            "StratificationCategoryID3",
            "StratificationID3",
            "TopicID",
            "QuestionID",
        ],
        axis=1,
    )


def split(dataframe: DataFrame, column: str) -> Dict[str, DataFrame]:
    dictionary: Dict[str, DataFrame] = {}

    for key in dataframe[column].unique():
        dictionary[key] = dataframe[dataframe[column] == key].drop(
            columns=[column], axis=1
        )

    return dictionary


if __name__ == "__main__":
    dataset: DataFrame = read_from("dataset.csv")

    remap: Dict[str, str] = {
        "Stratification1": "Stratification",
        "StratificationCategoryID1": "StratificationCategory",
        "LocationAbbr": "Location"
    }

    dataset["ObservationYears"] = dataset["YearEnd"] - dataset["YearStart"]

    for key, value in remap.items():
        dataset[value] = dataset[key]

    dataset = dataset.drop(columns=remap.keys(), axis=1)

    dataset = dataset.drop(columns=["YearEnd", "YearStart"], axis=1)

    topic_filtered: Dict[str, DataFrame] = split(dataset, "Topic")
