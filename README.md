# AQMI - Assessment of the quality of mammographic images

O software AQMI foi desenvolvido na linguagem Python versão 3.10.6. O objetivo geral do AQMI é a otimizar e unificar o processo de efetuar o teste de Qualidade da Imagem para Mamografia, por meio de uma interface fácil e intuitiva para o usuário. 

---
## Referência 

Quando utilizar essa ferramenta em estudos acadêmicos, por favor, se refira dessa maneira:

AQMI version 1.0 [1] Mangussi et al. (2022) 

---
## Utilizar o software (Windows)

Certifique-se de ter o Python e o pip instalados em seu sistema. Em seguida, execute o seguinte comando para instalar as dependências necessárias:

```pip install -r requirements.txt```

---
## Limitações do software
Por ser a primeira versão do software AQMI, há algumas limitações quanto ao uso dele. Sendo essas:
1. Por usar a biblioteca do Python Tkinter, não há compatibilidade com sistema operacional MacOS;
2. O ambiente de teste utilizou o objeto simulador do *American College of Radiology* (ACR) com imagens do mesmo tamanho para calcular as métricas e exibir a imagem na aba "Teste de qualidade da imagem";


