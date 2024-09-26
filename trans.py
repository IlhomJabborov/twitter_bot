from googletrans import Translator

tr = Translator()


def translate(text: str) -> str:
    lang = tr.detect(text).lang
    
    if lang == "en":
        result = tr.translate(text,dest='uz')
        return result.text
    else:
        return "Barselona FC'ning shiori 'Mes que un club' (klubdan ko'ra ko'proq)"
    