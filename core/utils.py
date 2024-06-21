def cat_human_translator(text, mode):
    def create_translation_dict():
        translation_dict = {
            "mi": "a",
            "mmii": "ı",
            "miii": "u",
            "mmi": "e",
            "mii": "i",
            "mmiii": "ü",
            "yav": "b",
            "yavv": "c",
            "yavvv": "d",
            "yavvvv": "f",
            "yavvvvv": "g",
            "yaav": "h",
            "yaaav": "j",
            "yaaaav": "k",
            "yaaaaav": "l",
            "yyav": "m",
            "yyyav": "n",
            "yyyyav": "p",
            "yyyyyav": "q",
            "yyyyyyav": "r",
            "yyaav": "s",
            "yyaavv": "t",
            "yyaavvv": "v",
            "yyaavvvv": "w",
            "yyaaavvvv": "x",
            "yyaaaavvv": "y",
            "yyaaaaavv": "z",
        }
        return translation_dict


    def translate_text(encoded_text):
        translation_dict = create_translation_dict()
        words = encoded_text.split()
        decoded_text = ""

        for word in words:
            decoded_word = ""
            i = 0
            while i < len(word):
                matched = False
                for length in range(9, 1, -1):  # Check for the longest patterns first
                    part = word[i : i + length]
                    if part in translation_dict:
                        decoded_word += translation_dict[part]
                        i += length
                        matched = True
                        break
                if not matched:
                    decoded_word += word[i]
                    i += 1
            decoded_text += decoded_word + " "

        return decoded_text.strip()


    def create_reverse_translation_dict():
        translation_dict = create_translation_dict()
        reverse_translation_dict = {v: k for k, v in translation_dict.items()}
        return reverse_translation_dict


    def encode_text(decoded_text):
        reverse_translation_dict = create_reverse_translation_dict()
        words = decoded_text.split()
        encoded_text = ""

        for word in words:
            encoded_word = ""
            for char in word:
                if char in reverse_translation_dict:
                    encoded_word += reverse_translation_dict[char]
                else:
                    encoded_word += char
            encoded_text += encoded_word + " "

        return encoded_text.strip()

    if mode == "cat_to_human":
        return translate_text(text)
    elif mode == "human_to_cat":
        return encode_text(text)