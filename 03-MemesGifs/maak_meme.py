from PIL import Image, ImageFont, ImageDraw

achtergrond = Image.open("meme_background.png")

breedte = achtergrond.width
hoogte = achtergrond.height

print("De afbeelding is " + str(breedte) + " pixels breed en " + str(hoogte) + " pixels hoog")

lettertype = ImageFont.truetype("impact.ttf", 40)

tekengebied = ImageDraw.Draw(achtergrond)

# Tekst schrijven
tekst = "Meow Meow!"

tekst_breedte, tekst_hoogte = tekengebied.textsize(tekst, font=lettertype) 
print("tekstbreedte=" + str(tekst_breedte) + ", tekst_hoogte=" + str(tekst_hoogte))


# Tekst positie berekenen
tekst_x = 38.5#(breedte - tekst_breedte) / 2
tekst_y = 10#(hoogte - tekst_hoogte) / 2


tekengebied.multiline_text((tekst_x, tekst_y), tekst, font=lettertype, fill=(255,255,255))
tekengebied.multiline_text((tekst_x-2, tekst_y-2), tekst, font=lettertype, fill=(0,0,0))

# Het resultaat tonen
achtergrond.show()

# En opslaan onder een andere naam
# achtergrond.save("meme_met_tekst.png")