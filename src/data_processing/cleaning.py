def remove_outliers(data, column, threshold=3):
    """
    Remove outliers from a DataFrame column using z-score method.
    
    Parameters:
    -----------
    data : pandas.DataFrame
        The DataFrame containing the data
    column : str
        The column name to check for outliers
    threshold : float, default=3
        Z-score threshold to identify outliers
        
    Returns:
    --------
    pandas.DataFrame
        DataFrame with outliers removed
    """
    z_scores = (data[column] - data[column].mean()) / data[column].std()
    return data[abs(z_scores) <= threshold]


def handle_missing_values(data, method='interpolate'):
    """
    Handle missing values in the DataFrame.
    
    Parameters:
    -----------
    data : pandas.DataFrame
        The DataFrame to process
    method : str, default='interpolate'
        Method to handle missing values: 'interpolate', 'mean', 'median', or 'drop'
        
    Returns:
    --------
    pandas.DataFrame
        DataFrame with missing values handled
    """
    if method == 'interpolate':
        return data.interpolate()
    elif method == 'mean':
        return data.fillna(data.mean())
    elif method == 'median':
        return data.fillna(data.median())
    elif method == 'drop':
        return data.dropna()
    else:
        raise ValueError(f"Unknown method: {method}. Use 'interpolate', 'mean', 'median', or 'drop'")