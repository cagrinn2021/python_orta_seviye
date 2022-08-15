writing yazma w , reading r, append ekleme a
dosya=open("Merhaba.txt","w")#eski dosya içeriği silinir ve sıfırlanırr
dosya.write("Merhaba ben programi öğreniyorum")
dosya.close()
dosya=open("Merhaba.txt","a")#eski dosya içeriği silinir ve sıfırlanırr
dosya.write("\nMerhaba ben programi öğreniyorum")
dosya.close()
dosya=open("Merhaba2.txt","x")#eski dosya içeriği silinir ve sıfırlanırr
dosya.write("Merhaba ben programi öğreniyorum")
dosya.close()
#x modu dosya aynı isimle dosya varsa hata veriyor bu w den farki