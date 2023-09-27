from googletrans import Translator, LANGUAGES

def translate_text():
    # Create a Translator object
    translator = Translator()

    # Get user input
    sentence = input("Enter your sentence: ")

    # Detect the source language
    detected_lang = translator.detect(sentence)
    print(f"This sentence is in: {LANGUAGES[detected_lang.lang]}")

    # Ask the user for the destination language
    dest_lang_code = input("Enter the language code of the preferred language (e.g., en for English): ")

    # Translate the sentence to the specified language
    translated_sentence = translator.translate(sentence, dest=dest_lang_code)
    print(f"This sentence in {LANGUAGES[dest_lang_code]} is: {translated_sentence.text}")

if __name__ == "__main__":
    translate_text()
