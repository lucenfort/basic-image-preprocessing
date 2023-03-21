import cv2
import os
import shutil

# Define os diretórios de entrada e saída
input_dir = "input"
output_dir = "output"

# Cria o diretório de saída se não existir
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Percorre todas as imagens no diretório de entrada
for root, dirs, files in os.walk(input_dir):
    for filename in files:
        # Verifica se o arquivo é uma imagem
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            # Monta o caminho completo da imagem de entrada
            input_path = os.path.join(root, filename)
            # Carrega a imagem
            img = cv2.imread(input_path)

            # Aplica a estratégia de preprocessamento
            img = cv2.equalizeHist(img)
            img = cv2.GaussianBlur(img, (5, 5), 0)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
            opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
            resized = cv2.resize(opening, (50, 50))
            features = cv2.HuMoments(cv2.moments(resized)).flatten()

            # Monta o caminho completo da imagem de saída
            output_path = os.path.join(output_dir, os.path.relpath(input_path, input_dir))
            # Cria os diretórios de saída se não existirem
            output_dirname = os.path.dirname(output_path)
            if not os.path.exists(output_dirname):
                os.makedirs(output_dirname)

            # Salva a imagem preprocessada
            cv2.imwrite(output_path, resized)

            print(f"Imagem {input_path} preprocessada e salva em {output_path}")
