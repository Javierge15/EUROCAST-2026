import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

files = {
    'UDP Stopped': 'UDP_STOPPED_.csv',
    'TCP Stopped': 'TCP_STOPPED_.csv',
    'UDP Moving': 'UDP_MOVING.csv',
    'TCP Moving': 'TCP_MOVING.csv'
}

dataframes = []
for label, path in files.items():
    df = pd.read_csv(path)
    df['Scenario'] = label
    df['Protocolo'] = 'UDP' if 'UDP' in label else 'TCP'
    df['Estado'] = 'Parado' if 'Stopped' in label else 'Movimiento'
    dataframes.append(df)

all_data = pd.concat(dataframes, ignore_index=True)

sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.size': 12})

# --- GRÁFICA 1: BOXPLOT COMPARATIVO (RTT) ---
plt.figure(figsize=(10, 6))
sns.boxplot(x='Scenario', y='rtt_ms', data=all_data, palette='Set2')
plt.title('RTT Latency Comparison')
plt.ylabel('RTT (ms)')
plt.xlabel('')
plt.savefig('1_BOXPLOT.png', dpi=300)
plt.show()

# --- GRÁFICA 2: ANÁLISIS DE JITTER ---
all_data['jitter'] = all_data.groupby('Scenario')['rtt_ms'].diff().abs()

plt.figure(figsize=(10, 6))
sns.kdeplot(data=all_data, x='jitter', hue='Scenario', fill=True, common_norm=False)
plt.title('Jitter Distribution')
plt.xlabel('Jitter (ms)')
plt.ylabel('Density')
plt.xlim(0, 20)
plt.savefig('2_JITTER-DISTRIBUTION.png', dpi=300)
plt.show()

# --- 3. CÁLCULO DE MÉTRICAS PARA LA TABLA DEL PAPER ---
metrics = all_data.groupby('Scenario')['rtt_ms'].agg([
    ('Media', 'mean'),
    ('Desv. Est.', 'std'),
    ('Mín', 'min'),
    ('Máx', 'max'),
    ('P99 (Percentil 99)', lambda x: x.quantile(0.99))
]).round(3)

print("\n--- MÉTRICAS PARA LA TABLA DEL PAPER ---")
print(metrics)

metrics.to_csv('3_RESULT-METRICS.csv')