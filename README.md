# 📦 Otimização de Supply Chain com Machine Learning

## 📌 Descrição
Este projeto tem como objetivo otimizar a cadeia de suprimentos utilizando modelos de **Machine Learning** para previsão de demanda e redução de custos logísticos. O foco está na previsão de vendas, otimização de estoques e melhoria nas rotas de transporte.

## 🔧 Tecnologias Utilizadas
- **Python** (Pandas, NumPy, Scikit-Learn, TensorFlow, Matplotlib, Seaborn)
- **Modelos Preditivos**: ARIMA, LSTM
- **Clusterização**: K-Means
- **Otimização**: Programação Linear
- **Gerenciamento de Variáveis de Ambiente**: `python-dotenv`

## 📂 Estrutura do Projeto
```
repo/
│-- dataset/
│   │-- train.csv
│   │-- features.csv
│   │-- stores.csv
│-- notebooks/
│   │-- exploratory_analysis.ipynb
│   │-- model_training.ipynb
│-- src/
│   │-- data_processing.py
│   │-- train_model.py
│-- .env
│-- requirements.txt
│-- README.md
```

## 📥 Importação do Dataset
Os dados estão armazenados na pasta `dataset/`. O caminho do dataset é gerenciado por um arquivo `.env`.

### Carregando os dados no Python
```python
import pandas as pd
import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

# Obter caminho do dataset do .env
dataset_path = os.getenv("DATASET_PATH")

# Carregar os arquivos CSV
df_sales = pd.read_csv(f'{dataset_path}/train.csv')
df_features = pd.read_csv(f'{dataset_path}/features.csv')
df_stores = pd.read_csv(f'{dataset_path}/stores.csv')

# Exibir as primeiras linhas
df_sales.head()
```

## 🚀 Implementação dos Modelos

### 1️⃣ **Previsão de Demanda**
- Utilização de **modelos de séries temporais** como **ARIMA** e **LSTM**.

### 2️⃣ **Otimização de Estoques**
- Clusterização de **centros de distribuição** usando **K-Means** para melhor alocação de estoque.

### 3️⃣ **Redução de Custos de Transporte**
- Implementação de **algoritmos de otimização (Programação Linear)** para minimizar os custos logísticos.

## 📈 Resultados Esperados
✅ Redução de **15% nos custos logísticos**
✅ **Melhoria de 30%** na precisão das previsões, reduzindo desperdício de estoque
✅ **Otimização das rotas** e alocação eficiente dos recursos

## 🔨 Como Executar o Projeto

1️⃣ **Instalar dependências**:
```bash
pip install -r requirements.txt
```

2️⃣ **Executar a análise exploratória**:
```bash
jupyter notebook notebooks/exploratory_analysis.ipynb
```

3️⃣ **Treinar o modelo**:
```bash
python src/train_model.py
```

4️⃣ **Avaliar os resultados**:
Verifique as métricas de desempenho e os insights gerados pelo modelo.

## 📌 Contribuição
Sinta-se à vontade para contribuir! Sugestões e melhorias são bem-vindas. 🚀

---

📩 **Contato:** [Seu Email / LinkedIn / GitHub]

