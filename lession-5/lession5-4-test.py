from translate import Translator

# translator = Translator(to_lang="Russian")
# translation = translator.translate("One")
# print(translation)

with open("textfile-4.txt") as numb:
    new_content = []
    for line in numb:
        key, digit = line.split('-')
        translator = Translator(to_lang="Russian")
        key_new = translator.translate(key)
        line_new = (f"{key_new} -{digit}")
        new_content.append(line_new)

with open("textfile-4-new-test.txt", "w", encoding="utf-8") as numb_new:
    numb_new.writelines(new_content)

