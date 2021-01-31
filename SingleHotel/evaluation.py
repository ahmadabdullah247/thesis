from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import numpy as np

def forecast_accuracy(y_pred, y_true):
    ME   = np.mean((y_true - y_pred) / y_true)
    SDE  = np.std(y_true - y_pred)
    MAE  = mean_absolute_error(y_true, y_pred)
    MAPE = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    MSE  = mean_squared_error(y_true, y_pred, squared=False)
    RMSE = mean_squared_error(y_true, y_pred, squared=True)
    R2   = r2_score(y_true, y_pred)
    print(str(round(SDE,4))+'\t&\t'+str(round(ME,4))+'\t&\t'+str(round(MAE,4))+'\t&\t'+str(round(MAPE,4))+'\t&\t'+str(round(MSE,4))+'\t&\t'+str(round(RMSE,4))+'\t&\t'+str(round(R2,4)))