import pandas as pd

# Funcion para convertir el resultado de la API en un DataFrame
def ga4_result_to_df(response):
    """Original: print_run_report_response: Prints results of a runReport call. v2.1 changed by Bram to create DataFrame"""
    result_dict = {}
    for dimensionHeader in response.dimension_headers:
        result_dict[dimensionHeader.name] = []
    for metricHeader in response.metric_headers:
        result_dict[metricHeader.name] = []
    for rowIdx, row in enumerate(response.rows):
        for i, dimension_value in enumerate(row.dimension_values):
            dimension_name = response.dimension_headers[i].name
            result_dict[dimension_name].append(dimension_value.value)
        for i, metric_value in enumerate(row.metric_values):
            metric_name = response.metric_headers[i].name
            result_dict[metric_name].append(metric_value.value)
    
    df = pd.DataFrame(result_dict)
    
    # Convertir la columna de fecha al formato DD-MM-YYYY
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], format='%Y%m%d').dt.strftime('%d-%m-%Y')
    
    return df
