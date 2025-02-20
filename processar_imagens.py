from google.cloud import vision
import os
import io

# Configuração do cliente da API Vision
client = vision.ImageAnnotatorClient()

# Caminho da imagem
image_path = 'inputs/imagem1.jpg'

# Função para detectar texto
def detect_text(image_path):
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    if response.error.message:
        raise Exception(f'API Error: {response.error.message}')
    
    return texts

# Detecta texto na imagem
texts = detect_text(image_path)

# Salva o resultado
output_path = 'output/resultado_imagem1.txt'
with open(output_path, 'w') as file:
    for text in texts:
        file.write(f'{text.description}\n')

print(f'Resultado salvo em: {output_path}')
