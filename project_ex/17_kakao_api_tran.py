from project_ex.kakao_api import *


class Kakao_translation(Kakao_api):
    def url_maker(self, url):
        return 'https://kapi.kakao.com' + url

    def translation_translate(self, query: str, src_lang: str, traget_lang: str):
        data = {
            'query': query,
            'src_lang': src_lang,
            'target_lang': traget_lang
        }

        return self.get_json(self.url_maker('/v1/translation/translate'), payload=data)['translated_text'][0]


if __name__ == '__main__':
    t = Kakao_translation()
    print(t.translation_translate('Hello', 'en', 'kr'))
    print(t.translation_translate('세종과학예술영재학교', 'kr', 'en'))
