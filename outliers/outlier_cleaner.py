#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    residual_error_list = []
    residual_error_list_copy = []
    outliers_indices = []
    outliers_error = []
    final_count = len(predictions)*0.1
    for i in range(len(predictions)):
        error = predictions[i]-net_worths[i]
        if error<0: error *= -1
        residual_error_list.append(error)
        residual_error_list_copy = residual_error_list
    for j in range(final_count):
        outliers_error.append(max(residual_error_list))
        max_index = residual_error_list.index(max(residual_error_list))
        outliers_indices.append(max_index)
        residual_error_list.remove(max(residual_error_list))
    for k in range(len(residual_error_list)):
        if k not in outliers_indices:
            cleaned_data.append(predictions[k], ages[k], net_worths[k])
    return cleaned_data

