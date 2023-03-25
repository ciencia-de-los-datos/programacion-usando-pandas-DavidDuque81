"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    quant = len(tbl0)
    return quant


def pregunta_02():
    col = tbl0.shape[1]
    return col


def pregunta_03():
    registers = tbl0['_c1'].value_counts().sort_index()
    return registers


def pregunta_04():
    letter_mean = tbl0.groupby('_c1')['_c2'].mean()
    return letter_mean


def pregunta_05():
    letter_max = tbl0.groupby('_c1')['_c2'].max()
    return letter_max


def pregunta_06():
    registers = sorted(tbl1['_c4'].unique())
    registers = [x.upper() for x in registers]
    return registers


def pregunta_07():
    letter_sum = tbl0.groupby('_c1')['_c2'].sum()
    return letter_sum


def pregunta_08():
    tbl0['suma'] = tbl0['_c0'] + tbl0['_c2']
    return tbl0


def pregunta_09():
    tbl0['year'] = tbl0['_c3'].apply(lambda x: x.strip().split('-')[0])
    return tbl0


def pregunta_10():
    """ my_dict = {}
    for i in range(len(tbl0)):
        letter = tbl0['_c1'][i]
        if letter in my_dict:
            my_dict[letter].append(tbl0['_c2'][i])
        else:
            my_dict[letter] = [tbl0['_c2'][i]]
    for key in my_dict:
        my_dict[key] = sorted(my_dict[key])
    df = pd.DataFrame(my_dict.items(), columns = ['_c1','_c2'])
    df['_c2'] = df['_c2'].apply(lambda x: ':'.join(map(str, x)))
    df = df.sort_values(by=['_c1']).reset_index()
    df.drop('index', axis='columns', inplace=True) """
    tbl0['_c2'] = tbl0['_c2'].astype('string')
    tbl = tbl0.sort_values(['_c1', '_c2'], ascending = [True, True])
    df = tbl0.groupby('_c1')['_c2'].apply(lambda x: ':'.join(map(str, sorted(list(x)))))
    new_df = pd.DataFrame(df)
    new_df
    return new_df


def pregunta_11():
    data = tbl1.groupby('_c0')['_c4'].sum().apply(lambda x: ','.join(sorted(map(str, x))))
    df = pd.DataFrame(data, columns = ['_c4']).reset_index()
    return df


def pregunta_12():
    my_dict = {}
    q =len(tbl2)
    for i in range(q):
        line = tbl2['_c0'][i]
        key = str(tbl2['_c5a'][i]) + ':' + str(tbl2['_c5b'][i])
        #print(line)
        if line in my_dict:
            my_dict[line] += ',' + key
        else:
            my_dict[line] = key
    for key, value in my_dict.items():
        my_dict[key] = ','.join(sorted(value.split(',')))
    df = pd.DataFrame.from_dict(my_dict, orient='index', columns = ['_c5']).reset_index()
    df.columns = ['_c0', '_c5']
    return df


def pregunta_13():
    """
    Si la columna _c0 es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`, compute la
    suma de tbl2._c5b por cada valor en tbl0._c1.

    Rta/
    _c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: _c5b, dtype: int64
    """
    merged = pd.merge(tbl0[['_c0', '_c1']], tbl2[['_c0', '_c5b']], on ='_c0')
    result = merged.groupby('_c1')['_c5b'].sum()
    return result

