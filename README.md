# CVProject
Paper da google sobre o Tesseract:
http://static.googleusercontent.com/media/research.google.com/pt-BR//pubs/archive/33418.pdf

## O que o projeto faz
1. O programa é alimentado com várias imagens que contém texto.
2. Utilizando o software Tesseract o texto contido nas imagens é extraido e armazenado em txts. 
3. O usuário pode então pesquisar uma palavra e o resultado é o conjunto de todas as imagens que contém tal palavra. 

## Sobre o Tesseract
* Software open source da Google, considerado um dos melhores softwares open source para OCR (Optical Character Recognition).
* É incapaz de reconhecer caligrafias manuais.
* É treinado com cerca de 64 fontes no total (cada uma com seus modos negrito, italico, etc).
* Ele não realiza o pré-processamento da imagem, ou seja, as imagens necessitam ter um contraste apropriado, tamanho apropriado, etc.

## Sobre o desenvolvimento
* Feito em python
* Foram também realizados vários experimentos utilizando OpenCV para entender melhor a complexidade do funcionamento interno do Tesseract (problemas como achar a linha e extrair o texto)
