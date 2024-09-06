LANGUAGES = {
    "en": "english",
    "zh": "chinese",
    "de": "german",
    "es": "spanish",
    "ru": "russian",
    "ko": "korean",
    "fr": "french",
    "ja": "japanese",
    "pt": "portuguese",
    "tr": "turkish",
    "pl": "polish",
    "ca": "catalan",
    "nl": "dutch",
    "ar": "arabic",
    "sv": "swedish",
    "it": "italian",
    "id": "indonesian",
    "hi": "hindi",
    "fi": "finnish",
    "vi": "vietnamese",
    "he": "hebrew",
    "uk": "ukrainian",
    "el": "greek",
    "ms": "malay",
    "cs": "czech",
    "ro": "romanian",
    "da": "danish",
    "hu": "hungarian",
    "ta": "tamil",
    "no": "norwegian",
    "th": "thai",
    "ur": "urdu",
    "hr": "croatian",
    "bg": "bulgarian",
    "lt": "lithuanian",
    "la": "latin",
    "mi": "maori",
    "ml": "malayalam",
    "cy": "welsh",
    "sk": "slovak",
    "te": "telugu",
    "fa": "persian",
    "lv": "latvian",
    "bn": "bengali",
    "sr": "serbian",
    "az": "azerbaijani",
    "sl": "slovenian",
    "kn": "kannada",
    "et": "estonian",
    "mk": "macedonian",
    "br": "breton",
    "eu": "basque",
    "is": "icelandic",
    "hy": "armenian",
    "ne": "nepali",
    "mn": "mongolian",
    "bs": "bosnian",
    "kk": "kazakh",
    "sq": "albanian",
    "sw": "swahili",
    "gl": "galician",
    "mr": "marathi",
    "pa": "punjabi",
    "si": "sinhala",
    "km": "khmer",
    "sn": "shona",
    "yo": "yoruba",
    "so": "somali",
    "af": "afrikaans",
    "oc": "occitan",
    "ka": "georgian",
    "be": "belarusian",
    "tg": "tajik",
    "sd": "sindhi",
    "gu": "gujarati",
    "am": "amharic",
    "yi": "yiddish",
    "lo": "lao",
    "uz": "uzbek",
    "fo": "faroese",
    "ht": "haitian creole",
    "ps": "pashto",
    "tk": "turkmen",
    "nn": "nynorsk",
    "mt": "maltese",
    "sa": "sanskrit",
    "lb": "luxembourgish",
    "my": "myanmar",
    "bo": "tibetan",
    "tl": "tagalog",
    "mg": "malagasy",
    "as": "assamese",
    "tt": "tatar",
    "haw": "hawaiian",
    "ln": "lingala",
    "ha": "hausa",
    "ba": "bashkir",
    "jw": "javanese",
    "su": "sundanese",
    "yue": "cantonese",
}
# Generate HTML code for language options
language_options = ""
for code, name in LANGUAGES.items():
    language_options += '<option value="{}">{}</option>\n'.format(code, name)

with open("lang.txt", "w") as f:
    f.write(language_options)

exit()
import sys

sys.exit()
# Include language options in the HTML template
html_template = """
{% extends "base.html" %}

{% block title %}Audio Transcription - Tekstitysapuri.fi{% endblock %}

{% block content %}
<style>
    h1 {{
        color: #3498db;
        text-align: center;
    }}

    form {{
        max-width: 400px;
        margin: 20px auto;
        padding: 20px;
        background-color: #ecf0f1;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    }}

    label {{
        display: block;
        margin-top: 10px;
    }}

    input[type="file"],
    select,
    input[type="submit"] {{
        width: 100%;
        padding: 10px;
        margin-top: 5px;
        margin-bottom: 15px;
        border: 1px solid #3498db;
        border-radius: 4px;
        box-sizing: border-box;
    }}

    input[type="submit"] {{
        background-color: #3498db;
        color: #ecf0f1;
        cursor: pointer;
        transition: background-color 0.3s;
    }}

    input[type="submit"]:hover {{
        background-color: #2980b9;
    }}
</style>

<h1 class="mt-4">Audio Transcription</h1>
<form action="/transcribe" method="post" enctype="multipart/form-data">
    <label for="audio_file">Choose an audio file:</label>
    <input type="file" id="audio_file" name="audio_file" accept=".wav, .mp3, .m4a, .mov, .mp4" required>

    <label for="model">Choose a model (optional):</label>
    <select id="model" name="model">
        <option value="tiny">Tiny Model</option>
        <option value="base" selected>Basic Model</option>
        <option value="small">Small Model</option>
        <option value="medium">Medium Model</option>
        <option value="large">Large Model</option>
    </select>

    <label for="language">Choose a language:</label>
    <select id="language" name="language">
        {}
    </select>

    <input type="submit" value="Transcribe">
</form>
{{% endblock %}}
""".format(
    language_options
)

# Save the modified HTML template to a file
with open("audio_transcription_template.html", "w") as file:
    file.write(html_template)

print(
    "HTML template with language options generated and saved to 'audio_transcription_template.html'"
)
