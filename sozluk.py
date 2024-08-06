meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "bir şakaya karşılık cevap"
            }
for i in range(5):
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

    if word in meme_dict.keys():  # meme_dict sözlüğündeki tüm anahtarlar liste olarak gelir
        print("Aradığınız kelimenin anlamı: ", meme_dict[word])
    else:
        print("Aradığınız kelime sözlükte bulunmamaktadır.")
