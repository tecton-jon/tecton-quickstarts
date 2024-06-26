from tecton import batch_feature_view
from tecton.types import Field, String, Timestamp
from entities import user
from data_sources.users import users
from datetime import datetime, timedelta


@batch_feature_view(
    sources=[users],
    entities=[user],
    mode="pandas",
    online=True,
    offline=True,
    feature_start_time=datetime(2017, 1, 1),
    batch_schedule=timedelta(days=1),
    description="User credit card issuer derived from the user credit card number.",
    schema=[Field("user_id", String), Field("signup_timestamp", Timestamp), Field("credit_card_issuer", String)],
)
def user_credit_card_issuer(users):
    users["credit_card_issuer"] = users["cc_num"].apply(
        lambda x: "Visa"
        if str(x)[0] == "4"
        else "MasterCard"
        if str(x)[0] == "5"
        else "Discover"
        if str(x)[0] == "6"
        else "other"
    )
    return users[["user_id", "signup_timestamp", "credit_card_issuer"]]