import pytube

url = input("Video url girin:")

#path="C:\\Users\\user\\OneDrive\\Masaüstü"
#Masaüstünüze indirmek için kendi masaüstü yolunuzu path içine yazabilirsiniz.
#Bu şekilde açtığınız dosyaya inecektir.(Her bilgisayarın yolu aynı olmayabilir.
path=""
pytube.YouTube(url).streams.get_highest_resolution().download(path)