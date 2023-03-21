# Preprocessamento de Imagens

Este repositório contém um código em Python para preprocessamento básico de imagens, utilizando algumas técnicas comuns como equalização de histograma, desfoque gaussiano, conversão para escala de cinza, limiarização binária, abertura morfológica e extração de momentos de Hu.

## Como usar

1. Clone o repositório para o seu computador:

```git clone https://github.com/seu-usuario/preprocessamento-imagens.git```


2. Instale as dependências necessárias:

```pip install opencv-python numpy```


3. Crie uma pasta contendo as imagens que deseja preprocessar.

4. Execute o arquivo `preprocessamento.py` informando o caminho para a pasta de entrada e a pasta de saída:

```
python preprocessamento.py --input_dir caminho/para/pasta/de/entrada --output_dir caminho/para/pasta/de/saida
```

O código irá percorrer todas as imagens nas subpastas da pasta de entrada que possuem as extensões `.png`, `.jpg`, `.jpeg` ou `.bmp`, aplicar as técnicas de preprocessamento descritas acima e salvar as imagens resultantes na pasta de saída, mantendo a mesma estrutura de pastas da pasta de entrada.
