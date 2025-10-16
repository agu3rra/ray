# Contribuindo para o projeto
Aqui vamos colocar dicas de como você pode contribuir com o projeto.

## Gerando `SpriteSheets` via linha de comando
O programa que usamos para gerar nossas sprites (Aseprite) pode ser usado via linha de comando (CLI - Command Line Interface) para gerar spritesheets a partir dos arquivos que gera com extensão `.aseprite`.
Para isso rodamos o comando:

```bash
aseprite.exe -b {source_file} --sheet {output_file}.png --data {output_file}.json
```

Se você está se perguntando porque geramos um arquivo `.json` além da imagem, é porque iremos usar as informações de posições de frame, suas durações, e outros metadados na nossa game engine (`pygame`).
Mas isso vem depois.