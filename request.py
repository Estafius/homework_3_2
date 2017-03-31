import requests
import glob
import os.path
import codecs

def translate_it(text,source_language,target_language):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    params = {
        'key': key,
        'lang': source_language.lower() + '-' + target_language.lower(),
        'text': text,
    }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))


def processing_files(file,target_language):
    with codecs.open(file,'r','utf-8') as original_file:
        file_content = original_file.readlines()
        translation = translate_it(file_content,file[0:2],target_language)
        return translation

def retrieve_files(pattern):
    files = glob.glob(os.path.join('', pattern))
    return files

def write_result_translation_to_file(file,translation):
    with open(file.replace('.txt','_after_traslation.txt.txt'), 'w') as result_translation:
        result_translation.write(translation)

def main():
    files = retrieve_files('*txt')
    target_language = 'ru'
    for file in files:
     translation = processing_files(file,target_language)
     write_result_translation_to_file(file,translation)


main()