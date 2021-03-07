
import numpy as np
import pandas as pd
coluna = 'A B C D E F G'.split()
linha = ' nome sexo idade estado-civíl data_de_nascimento forma_de_pagamento'.split()
dados = np.random.randint(len(coluna * len(linha)))
print(dados)
