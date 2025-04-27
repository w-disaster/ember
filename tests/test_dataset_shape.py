import pandas as pd
import os


def test_dataset_shape():
    # Open dataset with the hello_world PE file
    print("Loading dataset with hello_world PE file...")
    dataset_filename = os.path.join("tests", "dataset", "malware_ember_features.csv")
    df_ember_features = pd.read_csv(dataset_filename)

    df_ember_features.set_index("sha256", inplace=True)

    X = df_ember_features.drop(columns=["family"])
    y = df_ember_features["family"]

    df_ember_features.shape, X.shape, y.shape

    num_ember_features = 2381
    print(
        f"Testing dataset shape: should contain one sample with {num_ember_features} EMBER features"
    )
    assert df_ember_features.shape == (1, num_ember_features + 1)  # +1 for family
    assert X.shape == (1, num_ember_features)
    assert y.shape == (1,)
