# Documentación oficial: https://developers.google.com/analytics/devguides/reporting/data/v1/quickstart-client-libraries#python
# Info sobre dimensiones y métricas: https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)
from google.oauth2 import service_account

def fetch_ga4_data(property_id, credentials_dict, dimensionsList, metricsList):
    
    credentials = service_account.Credentials.from_service_account_info(credentials_dict)
    client = BetaAnalyticsDataClient(credentials=credentials)
    
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name=dim) for dim in dimensionsList],
        metrics=[Metric(name=met) for met in metricsList],
        date_ranges=[DateRange(start_date="2024-06-12", end_date="today")],
    )
    
    response = client.run_report(request)
    return response