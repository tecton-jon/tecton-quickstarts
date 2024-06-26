from tecton import batch_feature_view, Aggregation
from tecton.types import Field, String, Timestamp, Float64
from datetime import datetime, timedelta
from data_sources.transactions_batch import transactions_batch
from entities import user

@batch_feature_view(
    description="User transaction metrics over 1, 3 and 7 days",
    sources=[transactions_batch],
    entities=[user],
    mode="pandas",
    aggregation_interval=timedelta(days=1),
    aggregations=[
        Aggregation(function="mean", column="amount", time_window=timedelta(days=1)),
        Aggregation(function="mean", column="amount", time_window=timedelta(days=3)),
        Aggregation(function="mean", column="amount", time_window=timedelta(days=7)),
        Aggregation(function="count", column="amount", time_window=timedelta(days=1)),
        Aggregation(function="count", column="amount", time_window=timedelta(days=3)),
        Aggregation(function="count", column="amount", time_window=timedelta(days=7)),
    ],
    schema=[Field("user_id", String), Field("timestamp", Timestamp), Field("amount", Float64)],
    online=True,
    offline=True,
    feature_start_time=datetime(2020,1,1),
    batch_schedule=timedelta(days=1),
    tags={'team': 'finance', 'status': 'production'}
)
def user_transaction_metrics(transactions):
    return transactions[["user_id", "timestamp", "amount"]]