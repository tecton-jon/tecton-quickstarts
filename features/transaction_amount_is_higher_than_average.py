from tecton import on_demand_feature_view, RequestSource
from tecton.types import Float64, Bool, Field
from features.user_transaction_metrics import user_transaction_metrics


transaction_request = RequestSource(schema=[Field("amount", Float64)])


@on_demand_feature_view(
    sources=[transaction_request, user_transaction_metrics],
    mode="python",
    schema=[Field("transaction_amount_is_higher_than_average", Bool)],
)
def transaction_amount_is_higher_than_average(transaction_request, user_transaction_metrics):
    amount_mean = user_transaction_metrics["amount_mean_1d_1d"] or 0
    return {"transaction_amount_is_higher_than_average": transaction_request["amount"] > amount_mean}