from PIL import Image, ImageDraw

# Criar uma nova imagem (500x500 pixels, cor de fundo branca)
imagem = Image.new("RGB", (500, 500), "white")

# Criar um objeto de desenho
desenho = ImageDraw.Draw(imagem)

# Desenhar um círculo vermelho
desenho.ellipse((150, 150, 350, 350), fill="red", outline="black")

# Adicionar um texto à imagem
desenho.text((200, 400), "Minha Imagem!", fill="black")

# Salvar a imagem
imagem.save("minha_imagem.png")

# Mostrar a imagem
imagem.show()

