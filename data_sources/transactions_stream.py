from tecton import StreamSource, PushConfig, FileConfig
from tecton.types import Field, String, Timestamp, Float64


transactions_stream = StreamSource(
    name="transactions_stream",
    stream_config=PushConfig(),
    batch_config=FileConfig(
        uri="s3://mft-porter-data/tutorials/transactions.pq",
        file_format="parquet",
        timestamp_field="timestamp",
    ),
    schema=[Field("user_id", String), Field("timestamp", Timestamp), Field("amount", Float64)],
)