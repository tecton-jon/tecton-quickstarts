from tecton import BatchSource, FileConfig


users = BatchSource(
    name="users",
    batch_config=FileConfig(
        uri="s3://mft-porter-data/tutorials/users.pq",
        file_format="parquet",
        timestamp_field="timestamp",
    ),
)