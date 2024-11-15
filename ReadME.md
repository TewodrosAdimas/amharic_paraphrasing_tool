### `README.md`

# Amharic Paraphrasing Tool

This project is a Django-based web application that allows users to input Amharic text, which is then translated to English, paraphrased, and translated back to Amharic. The paraphrasing is done using a pre-trained model from Hugging Face's `transformers` library.

## Features

- **Amharic to English Translation**: Translates the input Amharic text to English.
- **Paraphrasing**: Generates paraphrased versions of the translated text using a transformer model.
- **Back to Amharic**: Translates the paraphrased English text back to Amharic.
- **Multiple Paraphrase Suggestions**: Users can specify how many paraphrased versions they'd like to generate.

## Requirements

- **Python 3.8+**
- **Django 3.x or higher**
- **googletrans** for translation
- **transformers** and **torch** for paraphrasing

### Dependencies

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Setup

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/TewodrosAdimas/amharic_paraphrasing_tool.git
cd amharic_paraphrasing_tool
```

### 2. Install Dependencies

Ensure you have Python installed, and then install the necessary packages:

```bash
pip install -r requirements.txt
```

### 3. Run Migrations

Before running the server, make sure to apply the migrations for your Django app:

```bash
python manage.py migrate
```

### 4. Start the Development Server

Run the Django development server:

```bash
python manage.py runserver
```

Visit [http://localhost:8000](http://localhost:8000) in your browser to access the application.

## Usage

1. Enter Amharic text in the input field on the homepage.
2. Optionally, specify the number of paraphrased suggestions you would like (default is 1).
3. Press **Submit** to process the text.
4. The page will display:
    - The original Amharic text.
    - The translated text in English.
    - One or more paraphrased versions in English.
    - The retranslated paraphrased text back into Amharic.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Hugging Face Transformers**: For providing the pre-trained models used for paraphrasing.
- **Googletrans**: For translation between Amharic and English.

```