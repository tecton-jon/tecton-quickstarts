from tecton import FeatureService
from features.user_transaction_amount_totals import user_transaction_amount_totals
from features.user_transaction_metrics import user_transaction_metrics
from features.transaction_amount_is_higher_than_average import transaction_amount_is_higher_than_average
from features.user_credit_card_issuer import user_credit_card_issuer

fraud_detection_feature_service = FeatureService(
    name="fraud_detection_feature_service",
    features=[user_transaction_metrics]
)

fraud_detection_feature_service_v2 = FeatureService(
    name="fraud_detection_feature_service:v2",
    features=[user_transaction_amount_totals, user_transaction_metrics, transaction_amount_is_higher_than_average, user_credit_card_issuer]
)

fraud_detection_feature_service_streaming = FeatureService(
    name="fraud_detection_feature_service_streaming", features=[user_transaction_amount_totals]
)