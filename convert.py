import string

LCASE = string.ascii_lowercase
UCASE = string.ascii_uppercase
# hiragana to Latin Character mapping
hirToLatin = {"あ": "a", "い": "i", "う": "u", "え": "e", "お": "o",
            "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",
            "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so",
            "た": "ta", "ち": "chi", "つ": "tsu", "て": "te", "と": "to",
            "な": "na", "に": "ni", "ぬ": "nu", "ね": "ne", "の": "no",
            "は": "ha", "ひ": "hi", "ふ": "fu", "へ": "he", "ほ": "ho",
            "ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo",
            "や": "ya", "ゆ": "yu", "よ": "yo",
            "ら": "ra", "り": "ri", "る": "ru", "れ": "re", "ろ": "ro",
            "わ": "wa", "を": "wo",
            "が": "ga", "ぎ": "gi", "ぐ": "gu", "げ": "ge", "ご": "go", "ん": "n",
            "ざ": "za", "じ": "ji", "ず": "zu", "ぜ": "ze", "ぞ": "zo",
            "だ": "da", "ぢ": "dzi", "づ": "zu", "で": "de", "ど": "do",
            "ば": "ba", "び": "bi", "ぶ": "bu", "べ": "be", "ぼ": "bo",
            "ぱ": "pa", "ぴ": "pi", "ぷ": "pu", "ぺ": "pe", "ぽ": "po","ゃ":"ja","っ":"s",
            }

clusters = {
    "きゅ": 'kyu',
    "きょ": 'kyo',
    "みゃ": 'mja',
    "しゃ": 'sha',
    "しゅ": 'shu',
    "しょ": 'sho',
    "じゃ": 'ja',
    "じゅ": 'ju',
    "じょ": 'jo',
    "ちゃ": 'cha',
    "ちゅ": 'chu',
    "ちょ": 'cho',
    "ぢゃ":'ja',
    "ぢゅ":'ju',
    "ぢょ": 'jo'
}
longVowels = {
    "a": "ā",
    "e": "ē",
    "i": "ī",
    "u": "ū",
    "o": "ō"
}

def hepburn(*hir,long_vowel="h"):
    for i in range(len(hir)):
        for j in hir[i]:
            if j not in hirToLatin:
                raise ValueError("Unexpected Latin Character in %s" % hir[i])
    translations = []
    for word in hir:
        for c in clusters:
            if c in word :
                word = word.replace(c, clusters[c])
        for char in word:
            if char in hirToLatin:
                word = word.replace(char, hirToLatin[char])
        if "nn" in word:
            word = word.replace("nn", "n’n")
        for long in longVowels:
            if long*2 in word:
                if long.lower() in "uo":
                    if long_vowel == "h":
                        word = word.replace(long*2, long + "h")
                    elif long_vowel == "u":
                        word = word.replace(long*2, long + "u")
                else:
                    word = word.replace(long*2, longVowels[long])
        translations.append(word)
    return translations

print(hepburn("こんにちわ"))

if __name__ == "__main__":
    print(hepburn("こんにち", "は", "とても", "あつい"))
