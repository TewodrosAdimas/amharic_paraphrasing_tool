# translator/views.py
from django.shortcuts import render
from googletrans import Translator
from transformers import pipeline
from .forms import TextForm

def translate_paraphrase(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            amharic_text = form.cleaned_data['amharic_text']

            # Step 1: Translate Amharic to English
            translator = Translator()
            translated = translator.translate(amharic_text, src='am', dest='en').text

            # Step 2: Paraphrase the English translation
            paraphrase_model = pipeline('paraphrase', model="Vamsi/T5_Paraphrase_Paws")
            paraphrased = paraphrase_model(translated)[0]['generated_text']

            # Step 3: Translate the paraphrased text back to Amharic
            retranslated = translator.translate(paraphrased, src='en', dest='am').text

            return render(request, 'translator/result.html', {
                'original_text': amharic_text,
                'translated': translated,
                'paraphrased': paraphrased,
                'retranslated': retranslated,
            })
    else:
        form = TextForm()

    return render(request, 'paraphrase/translate.html', {'form': form})
