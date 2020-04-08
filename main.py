import pandas as pd

def count_rub(k, T):
    return (k/1024) * T



ADDR = "87.245.198.147"
K = 2


df = pd.read_csv('nfcapd.csv')

BYTES1 = df.loc[df['da'] == ADDR, 'ibyt'].sum()
BYTES2 = df.loc[df['sa'] == ADDR, 'obyt'].sum()

summa = count_rub(K, BYTES1) + count_rub(K, BYTES2)

print ("Суммарная стоимость : ", summa)
