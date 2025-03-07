from data_processing import load_data, preprocess_data
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

def train_model():
    df_sales, df_features, df_stores = load_data()
    df = preprocess_data(df_sales, df_features, df_stores)
    
    df = df[['Date', 'Store', 'Weekly_Sales']]
    df['Date'] = df['Date'].view(int) / 10**9
    
    X = df[['Date', 'Store']].values
    y = df['Weekly_Sales'].values.reshape(-1, 1)
    
    scaler = MinMaxScaler()
    X = scaler.fit_transform(X)
    y = scaler.fit_transform(y)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = keras.Sequential([
        keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dense(1)
    ])
    
    model.compile(optimizer='adam', loss='mse')
    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))
    
    model.save("model.h5")
    print("Modelo salvo com sucesso!")

if __name__ == "__main__":
    train_model()