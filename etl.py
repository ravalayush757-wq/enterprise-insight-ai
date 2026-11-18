from database import DatabaseManager
import pandas as pd


class ETLPipeline:

    def __init__(self, file_path):
        self.file_path = file_path

    def extract(self):
        return pd.read_csv(self.file_path)

    def transform(self, df):

        print("\nCleaning Dataset...")

        # Remove unnecessary columns
        columns_to_drop = ["记录数", "Row.ID"]

        df = df.drop(columns=columns_to_drop)

        # Convert dates
        df["Order.Date"] = pd.to_datetime(df["Order.Date"])
        df["Ship.Date"] = pd.to_datetime(df["Ship.Date"])

        # Rename columns
        df.columns = (
            df.columns
            .str.lower()
            .str.replace(".", "_", regex=False)
            .str.replace(" ", "_")
        )

        print("Cleaning Completed")

        return df


if __name__ == "__main__":

    pipeline = ETLPipeline("data/superstore.csv")

    df = pipeline.extract()

    df = pipeline.transform(df)

    db = DatabaseManager()

    db.load_dataframe(df)