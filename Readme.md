Servidor Flask Simples Para Assistir Serie na TV

Usei o comando 
python´´´
ffmpeg -i "nome_do_arquivo.mkv" -map 0:v -map 0:a -vf "subtitles='nome_do_arquivo.mkv':si=4" -c:v libx264 -c:a copy "nome_do_arquivo.mp4"
´´´ 
para poder recriar o arquivo do ep .mkv, em .mp4 e sobrepor as legendas que estava ocultas para serem sobrepostas junto com o video (burn-in)
