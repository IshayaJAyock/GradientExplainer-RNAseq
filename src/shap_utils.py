"""
This file is part of the Verifying explainability of a deep learning tissue classifier trained on RNA-seq data project.

Verifying explainability of a deep learning tissue classifier trained on RNA-seq data project is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.


Verifying explainability of a deep learning tissue classifier trained on RNA-seq data project is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with the Verifying explainability of a deep learning tissue classifier trained on RNA-seq data project.  If not, see <http://www.gnu.org/licenses/>.
"""
from tqdm import tqdm
from constant import inv_map, map_dict
import numpy as np
import pandas as pd

def filter_shap(test_data, shap_arr, y_pred):
    df_data = []
    ids_list = test_data.index.to_list()
    genes_list = test_data.columns.tolist()[:-1]
    for i in tqdm(range(shap_arr.shape[0])):
        sample = shap_arr[i]
        sample_id = ids_list[i]
        label = inv_map[y_pred[i]]
        _, w, h = sample.shape
        shap_scores_flat = np.reshape(sample[label], (w * h,))[: len(genes_list)]

        df_data.append([sample_id, *list(shap_scores_flat), label])

    shap_df = pd.DataFrame(
        data=np.array(df_data), columns=["id", *genes_list, "predicted_label"]
    )

    shap_df.set_index("id", inplace=True)
    shap_df["true_label"] = test_data["type"]
    shap_df["predicted_label"] = shap_df["predicted_label"].astype("int").map(map_dict)

    return shap_df

def drop_false_pred(df):
    df = df[df.predicted_label == df.true_label].copy()
    df.drop("predicted_label", axis=1, inplace=True),
    return df

def get_rank_df(df):
    df = drop_false_pred(df)
    shap_df = df.loc[:, df.columns != "true_label"].astype("float64")
    shap_df["true_label"] = df["true_label"]

    median_shap = shap_df.groupby("true_label").median()
    median_shap = median_shap.T

    rank_dict = {}
    for col in median_shap:
        sorted_df = median_shap.sort_values(by=col, ascending=False)
        rank_dict[col] = sorted_df.index
    rank_df = pd.DataFrame.from_dict(rank_dict)
    return rank_df