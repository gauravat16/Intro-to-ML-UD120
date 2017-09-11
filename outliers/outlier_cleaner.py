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

    # print predictions
    # print ages
    # print net_worths

    from sklearn.metrics import mean_squared_error

    error_tuple = []
    for i in range(0, len(predictions)):
        error_tuple.insert(i, (ages[i],net_worths[i],mean_squared_error(net_worths[i], predictions[i])))

    error_tuple.sort(key=lambda x:x[2])
    cleaned_data = error_tuple[0:81]
    print error_tuple

    return cleaned_data
