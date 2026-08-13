# Dow Jones Quantitative Market Analysis

## Overview

This project explores historical Dow Jones market data using Python and quantitative analysis techniques. The project was developed as an early exploration of applying statistical and machine learning methods to financial market data.

The analysis focuses on cleaning and standardizing historical OHLCV (Open, High, Low, Close, and Volume) data, examining relationships between market variables, evaluating a linear regression model, and visualizing historical price movements.

## Objectives

The project was designed to:

* Clean and standardize historical financial market data
* Work with OHLCV market variables
* Examine relationships between market variables and closing price
* Apply linear regression to financial market data
* Evaluate model performance using mean squared error (MSE)
* Visualize historical closing-price trends

## Dataset

The dataset contains historical Dow Jones market observations from 2024.

The primary variables include:

* **Date** — Trading date
* **Open** — Opening price
* **High** — Highest price during the trading period
* **Low** — Lowest price during the trading period
* **Close** — Closing price
* **Adjusted Close** — Adjusted closing price
* **Volume** — Trading volume

Because the original dataset contained inconsistencies in numeric formatting, preprocessing was required before analysis.

## Data Cleaning & Preprocessing

Using Python and Pandas, I developed a preprocessing workflow to:

* Convert dates into a standardized datetime format
* Remove comma separators from numeric values
* Correct formatting inconsistencies in price fields
* Convert price variables to numeric data types
* Convert trading volume to numeric values
* Handle invalid or missing observations
* Verify the processed dataset before modeling

This provided a standardized dataset suitable for quantitative analysis.

## Quantitative Analysis

I used the following market variables as predictors:

* Open
* High
* Low
* Volume

The target variable was:

* Close

A multiple linear regression model was then trained to examine the relationship between these market variables and closing price.

### Model Evaluation

The model was evaluated using **Mean Squared Error (MSE)** to quantify the difference between predicted and observed closing prices.

The project also generated a comparison of actual versus predicted closing prices to provide an additional view of model performance.

## Visualization

I created a historical price visualization using Matplotlib to examine closing-price movements over the available period.

The visualization provides a simple view of market price trends and serves as a foundation for more advanced financial time-series analysis.

## Technology

* Python
* Pandas
* NumPy
* scikit-learn
* Matplotlib
* Microsoft Excel/CSV data

## Project Structure

```text
dow-jones-quantitative-analysis/
│
├── dow.py
├── dowgraph.py
├── dow.csv
└── README.md
```

### `dow.py`

Handles data preprocessing, feature selection, linear regression, predictions, and model evaluation.

### `dowgraph.py`

Creates visualizations of historical closing-price movements.

### `dow.csv`

Contains the historical market data used for the analysis.

## Key Takeaways

This project provided practical experience working with financial market data and demonstrated how Python can be used to move from raw financial data through preprocessing, statistical modeling, model evaluation, and visualization.

More broadly, the project helped me develop an understanding of how quantitative methods can be applied to financial datasets and provided a foundation for more advanced work in financial analytics, time-series analysis, and quantitative finance.

## Future Improvements

If this project were extended, I would improve the methodology by:

* Expanding the historical dataset to multiple years
* Using time-series-aware train/test splits rather than random sampling
* Adding technical indicators such as moving averages, RSI, MACD, and volatility measures
* Engineering lagged and return-based features
* Comparing linear regression with additional predictive models
* Evaluating predictions using financial metrics in addition to MSE
* Implementing walk-forward validation
* Accounting for transaction costs and slippage
* Developing a backtesting framework to evaluate trading strategies

## Disclaimer

This project is for educational and analytical purposes only. The regression analysis does not constitute an investment strategy or financial advice.
