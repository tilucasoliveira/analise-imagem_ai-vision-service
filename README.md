# 
# Análise de Imagem 4.0 com AI Vision Service

## Descrição
Este projeto utiliza a API de AI Vision Service para realizar o reconhecimento de texto em imagens. O objetivo é analisar imagens e extrair textos ou informações relevantes de forma automatizada.

## Como Rodar
1. Clone o repositório:
   ```bash
   git clone https://github.com/tilucasoliveira/analise-imagem_ai-vision-service.git
   ```

2. Instale as dependências:
   - **Python 3.x**
   - **Google Cloud Vision API**:
   ```bash
     pip install google-cloud-vision
   ```

3. Coloque as imagens que você deseja analisar na pasta `inputs/`.

4. Execute o script `processar_imagens.py` para iniciar o reconhecimento.

   ```bash
   python processar_imagens.py
   ```

5. Os resultados serão salvos na pasta `output/`.

## Exemplo de Imagens e Resultados
![Exemplo de Imagem](inputs/imagem1.jpg)
Resultado extraído:
- **Texto detectado**: "Texto exemplo da imagem."

## Possíveis Melhorias
- Implementar o reconhecimento de faces.
- Adicionar o reconhecimento de objetos (via API de objetos).
- Melhorar a formatação dos resultados para incluir mais detalhes.

## Insights
Este projeto demonstrou como as APIs de AI Vision podem ser utilizadas para resolver problemas de reconhecimento de imagem de forma simples, automatizada e eficiente. A combinação de técnicas de OCR (reconhecimento óptico de caracteres) e IA pode ser aplicada em diversas áreas, como automação de documentos, acessibilidade e segurança.

## Tecnologias Utilizadas
- ![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white) - **Vision API**
- ![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white) - **SDK**
- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

