import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load CSV file
df = pd.read_csv('dow.csv')

# Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

def preprocess_data(df):
    # Handle conversion for each column
    for column in ['Open', 'High', 'Low', 'Close', 'Adj Close']:
        # Remove commas
        df[column] = df[column].str.replace(',', '', regex=False)
        # Handle cases where periods are incorrectly placed
        df[column] = df[column].str.replace(r'(?<=\d)\.(?=\d)', '', regex=True)
        # Convert to numeric
        df[column] = pd.to_numeric(df[column], errors='coerce')

    # Remove commas from Volume and convert to integer
    df['Volume'] = df['Volume'].str.replace(',', '', regex=False).astype(int)
    
    return df

try:
    # Preprocess data
    df = preprocess_data(df)
    
    # Check processed data
    print(df.head())
    
    # Define test file specifics
    test_file = {
        'filename': 'dow.csv',
        'target_column': 'Close',
        'features': ['Open', 'High', 'Low', 'Volume']
    }
    
    file = test_file['filename']
    target_column = test_file['target_column']
    features = test_file['features']
    
    # Check if the target column exists
    if target_column not in df.columns:
        raise ValueError(f"Column '{target_column}' is missing from the data")

    # Drop rows with missing values
    df = df.dropna(subset=[target_column] + features)
    
    # Verify data after dropping rows
    print("Data after dropping rows with missing values:")
    print(df.head())
    
    # Select features and target
    X = df[features]
    y = df[target_column]

    # Ensure there are enough rows to split into train and test sets
    if len(df) < 10:
        raise ValueError("Not enough data to split into training and testing sets")

    # Split data into training and testing sets
    test_size = min(0.2, len(df) / 10)  # Ensure at least one sample in the test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    # Create and train model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Evaluate model
    mse = mean_squared_error(y_test, y_pred)
    print(f'MSE for {file}: {mse:.2f}')
    
    # Inspect predictions vs actual values
    comparison_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    print(comparison_df.head())

except FileNotFoundError:
    print(f"File '{file}' not found.")
except ValueError as e:
    print(f"Error with file '{file}': {e}")
except Exception as e:
    print(f"An error occurred with file '{file}': {e}")
