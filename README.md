# CVProject

Adicione links de bons tutoriais (depois de ter dado uma lidinha pelo menos). Obrigado!

Tutorial: https://kusemanohar.wordpress.com/2010/11/18/optical-character-recognition/

# Sugestão de Abordagem
##### Objetivo do projeto
Software: biblioteca OpenCV (biblioteca OpenSource de Computer Vision)

Input: Imagens de texto (paginas de livros fotografadas - Google Books)

Output: Arquivo TXT com o conteudo de texto da imagem.

##### Como ele encontra as caracteristicas procuradas
Inicialmente, iremos tratar as imagens de forma que somente as propriedades essenciais para realizar o reconhecimento destas estejam presentes. 
- Caso a imagem seja colorida, converter ela para preto e branco. (0-255)
- Realizar o processo de Thresholding, transformando-a em uma imagem de fato preto ou branco. (0 ou 1)
- Extrair cada caractere em separado. Analise de conectividade?
- Normalizacao

Após tal tratamento, tentaremos os seguintes algoritmos (em ordem de complexidade):
- Template matching
- Algoritmos de identificação de caracteriísticas: SIFT e SURF
- Machine Learning: SVM, Redes Neurais, etc (-> Não precisamos chegar até esse ponto)

##### O quanto ele é confiável
Supondo que tivessemos algumas imagens e sua resposta, da pra calcular o numero de false positives, false negatives, true negatives, true positives e calcular os indices: Precision (TP/(TP+FP)) e Recall (TP/(TP+FN)). Disso da pra estimar mais um indice chamado F1 score, para achar os melhores parametros do projeto. (Cartas)

##### Qual tipo de melhoria poderiam se desenvolvidas pra melhorar o projeto
Incluir Machine Learning.
