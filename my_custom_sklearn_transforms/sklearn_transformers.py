from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')


# All sklearn Transforms must have the `transform` and `fit` methods
class CustomColumnsImputer(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        
        # Segundo preenchemos as informações de ingles com zero
        data['INGLES'].fillna(0, inplace=True)
                
        for row in data.loc[data['NOTA_GO'].isnull()].itertuples():
                if row.REPROVACOES_GO == 0:
                    data.at[row.Index, 'NOTA_GO'] = data['NOTA_GO'].mean()
                else:
                    data.at[row.Index, 'NOTA_GO'] = 0
                
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data   
