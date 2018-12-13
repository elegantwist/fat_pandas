from typing import List


class FatPandas:
    """
    Wrapper above pandas table, that substitute an iterrows() method for the table

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

    """

    pandas_table = None
    quick_columns = []
    numpy_columns = None
    i = 0
    pd_iter = None
    length = 0

    def __init__(self, dtable=None):

        self.pandas_table = dtable
        self.length = len(dtable)

    def init_quick_columns(self, quick_columns: List = None):

        self.quick_columns = quick_columns
        self.numpy_columns = self.pandas_table[quick_columns].values

    def __iter__(self):

        self.i = 0
        return self

    def __next__(self):

        if self.i == self.length:
            raise StopIteration()

        z_obj = zip(self.quick_columns, self.numpy_columns[self.i])

        row_dict = dict([ll for ll in z_obj])

        self.i = self.i + 1

        return self.i - 1, row_dict


