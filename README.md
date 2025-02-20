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
![Exemplo de Imagem](https://static.wixstatic.com/media/5e7c2b_117b371013e3480f8d841dc9d8254ba9~mv2.jpeg/v1/fit/w_777,h_582,q_90,enc_avif,quality_auto/5e7c2b_117b371013e3480f8d841dc9d8254ba9~mv2.jpeg) 

Resultado extraído:
- **Texto detectado**: "Senhor Deputado,

Em atenção ao ofício PS/81 nº 2092/93, de 18.11.93, que encaminhou a Requerimento de Informação nº 276/93, de autoria do Visconde Milândio Minagé, informo que:
Sobre depoimentos colhidos e falta de acertos tais documentos foram digitalizados e arquivados no sistema do Ministério da Justiça. O acesso a tais documentos está disponível mediante solicitação formal e apresentação de documentação pertinente.

Atenciosamente,
Maurício Corrêa
Ministro da Justiça

Senhor
Roberto Cardoso Alves
1º Secretário da Primeira Secretaria
Câmara dos Deputados"

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

### 5. **Subir os arquivos para o GitHub**
Depois de configurar e testar tudo, faça o commit e o push dos seus arquivos para o GitHub:
```bash
git add .
git commit -m "Adicionando projeto de análise de imagem com AI Vision"
git push origin main
```

### Conclusão
Com essas etapas, você conseguirá entregar o projeto conforme solicitado. Certifique-se de documentar bem o processo e os resultados, além de explicar o aprendizado e as possibilidades de melhorias futuras. Boa sorte no seu projeto!
