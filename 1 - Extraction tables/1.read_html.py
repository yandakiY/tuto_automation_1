import pandas as pd

tables_s1 = pd.read_html('https://fr.wikipedia.org/wiki/Liste_des_%C3%A9pisodes_des_Simpson')

print(len(tables_s1))
print(tables_s1[1])