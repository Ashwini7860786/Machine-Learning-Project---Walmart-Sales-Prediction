# Machine Learning Project - Walmart Sales Prediction

## Objective
This project aims to predict weekly sales for Walmart stores using various machine learning algorithms. The dataset includes 6435 entries with 8 features such as store number, date, weekly sales, holiday flag, temperature, fuel price, CPI, and unemployment rate.

## Dataset Information
The dataset covers sales from 2010-02-05 to 2012-11-01. The fields include:
- **Store**: Store number
- **Date**: Week of sales
- **Weekly_Sales**: Sales for the given store
- **Holiday_Flag**: Whether the week is a special holiday week (1: Holiday, 0: Non-holiday)
- **Temperature**: Temperature on the day of sale
- **Fuel_Price**: Cost of fuel in the region
- **CPI**: Consumer price index
- **Unemployment**: Unemployment rate

### Holiday Events
- **Super Bowl**: 12-Feb-10, 11-Feb-11, 10-Feb-12, 8-Feb-13
- **Labour Day**: 10-Sep-10, 9-Sep-11, 7-Sep-12, 6-Sep-13
- **Thanksgiving**: 26-Nov-10, 25-Nov-11, 23-Nov-12, 29-Nov-13
- **Christmas**: 31-Dec-10, 30-Dec-11, 28-Dec-12, 27-Dec-13

## Approach

### Libraries Used
- **Pandas**: For data manipulation and analysis.
- **Numpy**: For numerical computations.
- **Matplotlib & Seaborn**: For data visualization.
- **Scikit-learn**: For machine learning algorithms and preprocessing.

### Data Preprocessing
- **Handling Null Values**: Ensured there are no missing values in the dataset.
- **Outlier Detection and Removal**: Used the Interquartile Range (IQR) method to identify and remove outliers, ensuring the dataset is clean and reliable.
- **Feature Scaling**: Applied `StandardScaler` to normalize numerical features, ensuring they contribute equally to the model performance.

### Feature Engineering
- **Correlation Matrix and Heatmap**: Identified relationships between features to detect multicollinearity.
- **Variance Inflation Factor (VIF)**: Removed multicollinear features to enhance model performance.
- **P-Value Significance**: Selected features based on their statistical significance.

### Modeling
- **Linear Regression**: Basic model to establish a baseline.
- **Polynomial Regression**: Enhanced model complexity to capture non-linear relationships.
- **Regularization Techniques**: Used Ridge, Lasso, and Elastic Net to address overfitting by penalizing large coefficients.

## Results
Achieved the best performance with Multiple Linear Regression:
- **Testing R² Score**: 0.9277
- **Root Mean Squared Error (RMSE)**: 157283.79