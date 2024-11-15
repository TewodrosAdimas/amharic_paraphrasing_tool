from django.shortcuts import render
from googletrans import Translator
from transformers import pipeline
from .forms import TextForm
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Use the appropriate model and tokenizer
tokenizer = T5Tokenizer.from_pretrained("Vamsi/T5_Paraphrase_Paws")
model = T5ForConditionalGeneration.from_pretrained("Vamsi/T5_Paraphrase_Paws")

# Initialize the paraphrase model globally to avoid reloading it for each request
paraphrase_model = pipeline('text2text-generation', model="Vamsi/T5_Paraphrase_Paws")

def translate_paraphrase(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            amharic_text = form.cleaned_data['amharic_text']
            number_of_suggestions = form.cleaned_data.get('number_of_suggestions', 1)

            try:
                # Step 1: Split the text on ፡፡
                sentences = amharic_text.split('፡፡')

                final_paraphrased_texts = []
                for sentence in sentences:
                    if sentence.strip():  # Skip empty parts from splitting
                        # Step 2: Translate Amharic to English for each sentence
                        translator = Translator()
                        translated = translator.translate(sentence, src='am', dest='en').text

                        # Step 3: Generate paraphrases (limited by user input)
                        paraphrased_texts = []
                        for _ in range(number_of_suggestions):
                            paraphrased = paraphrase_model(translated)[0]['generated_text']
                            paraphrased_texts.append(paraphrased)

                        # Step 4: Translate paraphrased text back to Amharic
                        retranslated_texts = []
                        for paraphrased in paraphrased_texts:
                            retranslated = translator.translate(paraphrased, src='en', dest='am').text
                            retranslated_texts.append(retranslated)

                        # Append the results for each sentence
                        final_paraphrased_texts.append({
                            'original': sentence.strip(),
                            'translated': translated,
                            'paraphrased_texts': paraphrased_texts,
                            'retranslated_texts': retranslated_texts,
                        })

                return render(request, 'paraphrase/result.html', {
                    'final_paraphrased_texts': final_paraphrased_texts,
                })

            except Exception as e:
                return render(request, 'paraphrase/result.html', {'error': f"An error occurred: {e}"})

    else:
        form = TextForm()

    return render(request, 'paraphrase/translate.html', {'form': form})
