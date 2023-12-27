# import camelot

# tables = camelot.read_pdf('tablesu.pdf' , pages='1')

# tables.export('foo.csv' , f='csv' , compress=True)

# tables[0].to_csv('foo.csv')

import camelot

tables = camelot.read_pdf('./files/camelot_test.pdf', pages='1', flavor='lattice')
# print(tables)

tables.export('table_camelot.csv', f='csv', compress=True)
tables[0].to_csv('table_camelot.csv') # to a csv file
print(tables[0].df) # to a df