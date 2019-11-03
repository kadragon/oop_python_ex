from project_ex.kakao_api import *


class Kakao_local_api(Kakao_api):
    def url_maker(self, url):
        return 'https://dapi.kakao.com' + url

    def local_address(self, query: str, page=1, size=10):
        """
        https://developers.kakao.com/docs/restapi/local#주소-검색
        주소를 지도 위에 정확하게 표시하기 위해 해당 주소의 좌표 정보를 제공합니다.
        주소 유형에 구분없이 변환할 수 있으며, 주소에 해당하는 지번 주소, 도로명 주소, 좌표, 우편번호, 빌딩명 등의 다양한 정보를 함께 제공하여 다양하게 활용할 수 있습니다.
        :param query: 검색을 원하는 질의어 | String
        :param page: 결과 페이지 번호 | default 1 | Integer
        :param size: 한 페이지에 보여질 문서의 개수 | default 10 | 1~30
        :return: json
        """
        payload = {
            'query': query,
            'page': page,
            'size': size
        }

        return self.get_json(self.url_maker('/v2/local/search/address.json'), payload)['documents']

    def local_keyword(self, query: str, category_group_code=None,
                      x=None, y=None, radius=None, rect=None,
                      page=1, size=15, sort='accuracy'):
        """
        https://developers.kakao.com/docs/restapi/local#키워드로-장소-검색
        질의어에 매칭된 장소 검색 결과를 지정된 정렬 기준에 따라 제공합니다.
        현재 위치 좌표, 반경 제한, 정렬 옵션, 페이징 등의 기능을 통해 원하는 결과를 요청 할 수 있습니다.
        각 장소는 이름, 주소, 좌표, 카테고리 등의 기본 정보와 다양한 부가정보, 다음 지도의 장소 상세 페이지로 연결되는 URL 정보도 제공됩니다.
        :param query: 검색을 원하는 질의어 | String
        :param category_group_code: 카테고리 그룹 코드 | Code
        :param x: 중심 좌표의 X값 혹은 longitude. 특정 지역을 중심으로 검색하려고 할 경우 radius와 함께 사용 가능. | String
        :param y: 중심 좌표의 Y값 혹은 latitude. 특정 지역을 중심으로 검색하려고 할 경우 radius와 함께 사용 가능. | String
        :param radius: 중심 좌표부터의 반경거리. 특정 지역을 중심으로 검색하려고 할 경우 중심좌표로 쓰일 x,y와 함께 사용. 단위 meter | 0~20000
        :param rect: 사각형 범위내에서 제한 검색을 위한 좌표. 지도 화면 내 검색시 등 제한 검색에서 사용가능. 좌측 X좌표, 좌측 Y좌표, 우측 X좌표, 우측 Y좌표 형식. | String
        :param page: 결과 페이지 번호 | default 1 | 1~45
        :param size: 한 페이지에 보여질 문서의 개수 | default 15 | 1~15
        :param sort: 결과 정렬 순서. distance 정렬을 워할때는 기준좌표로 쓰일 x,y와 함께 사용. | default: accuracy | distance or accuracy
        :return: json
        """
        payload = {
            'query': query,
            'category_group_code': category_group_code,
            'x': x,
            'y': y,
            'radius': radius,
            'rect': rect,
            'page': page,
            'size': size,
            'sort': sort
        }

        return self.get_json(self.url_maker('/v2/local/search/keyword.json'), payload)['documents']


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
    k = Kakao_local_api()

    data_list = k.local_address('세종특별자치시 달빛1로 265')
    print(data_list[0])

    data_list = k.local_keyword('편의점', x='127.24904338902533', y='36.52262151763814', sort='distance', radius=1000)
    for data in data_list:
        print("%s | %13s | %s | %s" % (data['place_name'], data['phone'], data['place_url'], data['road_address_name']))
