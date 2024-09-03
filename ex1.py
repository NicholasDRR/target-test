# 1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
# Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
# Imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?

INDEX = 13
SUM = 0
K = 0

while K < INDEX:
    K += 1
    SUM += K

print("The final value of SUM is:", SUM)
# The final value of SUM is: 91