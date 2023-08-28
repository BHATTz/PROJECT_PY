from googletrans import Translator, LANGUAGES

def translate_text(text, target_language):
    translator = Translator()
    translated = translator.translate(text, src="auto", dest=target_language)
    return translated.text

def get_supported_languages():
    return LANGUAGES

# Get user input
input_text = input("Enter the text you want to translate: ")
target_language = input("Enter the target language code (e.g., 'es' for Spanish): ")

supported_languages = get_supported_languages()

print("Supported languages:")
for code, language in supported_languages.items():
    print(f"{code}: {language}")

if target_language in supported_languages:
    translated_text = translate_text(input_text, target_language)
    print(f"Translated text: {translated_text}")
else:
    print("Invalid target language code. Please choose a valid language code.")
