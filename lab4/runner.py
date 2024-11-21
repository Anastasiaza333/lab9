from lab4.MyAsciiArtGenerator import MyAsciiArtGenerator
from source.ABC123asterism import draw_char_asterism
from source.ABC123dog import draw_char_dog
from source.ABC123hash import draw_char_hash

def figlet_format(art_text, font):
            result = [""] * 7  

            for letter in art_text:
                if font == "#":
                    letter_art = draw_char_hash(letter)
                elif font == "@":
                    letter_art = draw_char_dog(letter)
                elif font == "*":
                    letter_art = draw_char_asterism(letter)
                
                for i in range(7):
                    result[i] += letter_art[i]  

            return "\n".join(result)




def run():

    art = MyAsciiArtGenerator()
    art.run()



