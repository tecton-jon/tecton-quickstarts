from tecton import stream_feature_view, Aggregation
from tecton.types import Field, String, Timestamp, Float64
from datetime import datetime, timedelta
from data_sources.transactions_stream import transactions_stream
from entities import user 


@stream_feature_view(
    source=transactions_stream,
    entities=[user],
    mode="pandas",
    schema=[Field("user_id", String), Field("timestamp", Timestamp), Field("amount", Float64)],
    aggregations=[
        Aggregation(function="sum", column="amount", time_window=timedelta(minutes=1)),
        Aggregation(function="sum", column="amount", time_window=timedelta(hours=1)),
        Aggregation(function="sum", column="amount", time_window=timedelta(days=30)),
    ],
    online=True,
    offline=True,
    feature_start_time=datetime(2020,1,1),
    batch_schedule=timedelta(days=1)
)
def user_transaction_amount_totals(transactions):
    return transactions[["user_id", "timestamp", "amount"]]