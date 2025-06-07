
# 🖼 Criando uma Imagem de um Círculo Vermelho com Python

Este projeto demonstra como criar uma imagem simples contendo um **círculo vermelho** utilizando **Python** e a biblioteca **Pillow**.

## 🚀 Tecnologias Utilizadas
- **Python 3.12** ou superior
- **Pillow (PIL)** - Biblioteca para manipulação de imagens

## 🛠 Instalação
Antes de executar o código, certifique-se de ter o **Python** e o **Pillow** instalados. Se ainda não tiver Pillow, instale com:

```bash
pip install pillow
```

## 📜 Código Fonte

from PIL import Image, ImageDraw

# Criar uma nova imagem branca
imagem = Image.new("RGB", (500, 500), "white")

# Criar um objeto de desenho
desenho = ImageDraw.Draw(imagem)

# Desenhar um círculo vermelho
desenho.ellipse((150, 150, 350, 350), fill="red", outline="black")

# Salvar e exibir a imagem
imagem.save("circulo_vermelho.png")
imagem.show()


## 📷 Resultado
Este código gerará uma imagem de **500x500 pixels**, contendo um **círculo vermelho** centralizado.

## 🎯 Objetivo do Projeto
Este repositório serve como um exemplo educativo para quem deseja aprender **manipulação de imagens** em Python de forma simples.


![minha_imagem](https://github.com/user-attachments/assets/9fa2b056-6c45-4602-af08-321115a8dda3)
![Captura de tela 2025-06-07 030758](https://github.com/user-attachments/assets/586a1f21-46c0-4212-bb1b-9b46ece13655)


