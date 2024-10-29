import pandas

from pandas import DataFrame

from typing import List

if __name__ == '__main__':
    dataset: DataFrame = pandas.read_csv('dataset.csv')

    for column in dataset.columns:
        ratio: float = dataset[column].isnull().sum() / len(dataset)

        if ratio > 0.05:
            dataset = dataset.drop(columns=[column], axis=1)

    dataset = dataset.drop(columns=['GeoLocation', 'LocationDesc', 'LocationID'], axis=1)
