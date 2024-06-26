from tecton import BatchSource, FileConfig


transactions_batch = BatchSource(
    name="transactions_batch",
    batch_config=FileConfig(
        uri="s3://mft-porter-data/tutorials/transactions.pq",
        file_format="parquet",
        timestamp_field="timestamp",
    ),
)