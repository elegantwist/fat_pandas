A wrapper around pandas table, that substitute an iterrows() method for the table
    
you can use this wrapper with 2 steps:

1. init the wrapper, passing the pandas table into fatpandas' constructor
2. init the column you need, via calling fatpandas' init_quick_columns() method
3. substitute the call of pd_table.iterrows() with fatpandas' object in for-cycle
4. leave the iteration as it would be run with pandas table

if you've got something like:

------
pd_table = pd.DataFrame(['Column1', 'Column2', 'Column3'])
for i, row in pd_table.iterrows():
    value = row['val_name']
------
this should be converted do something like this:

------
pd_table = pd.DataFrame(['Column1', 'Column2', 'Column3'])
fp = FatPandas(pd_table).init_quick_columns(['Column1', 'Column2', 'Column3']) # <- init
for i, row in fp: # <- change pd_table.iterrows() to fp
    value = row['val_name']
------
