import os
import io
from google.cloud import vision

# Diretórios de entrada e saída
INPUT_DIR = 'inputs'
OUTPUT_DIR = 'output'

# Criação das pastas se não existirem
os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Inicialização do cliente da API Vision
client = vision.ImageAnnotatorClient()

def detect_text(image_path):
    """Detecta texto em uma imagem usando a API Google Cloud Vision."""
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)

    if response.error.message:
        raise Exception(f'Erro da API: {response.error.message}')

    return response.text_annotations

def process_images():
    """Processa todas as imagens da pasta de entrada e salva os resultados na pasta de saída."""
    images = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(('jpg', 'jpeg', 'png'))]

    if not images:
        print(f'Nenhuma imagem encontrada em {INPUT_DIR}.')
        return

    for image_name in images:
        image_path = os.path.join(INPUT_DIR, image_name)
        print(f'Processando {image_name}...')

        texts = detect_text(image_path)
        output_file = os.path.join(OUTPUT_DIR, f'resultado_{os.path.splitext(image_name)[0]}.txt')

        with open(output_file, 'w', encoding='utf-8') as file:
            for text in texts:
                file.write(f'{text.description}\n')

        print(f'Resultado salvo em: {output_file}')

if __name__ == '__main__':
    process_images()
