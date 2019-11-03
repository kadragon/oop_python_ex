from project_ex.kakao_api import *


class Kakao_vision_api(Kakao_api):
    def url_maker(self, url):
        return 'https://kapi.kakao.com' + url

    def vision_face_detect(self, image_url=None, file=None, threshold=0.7):
        """
        https://developers.kakao.com/docs/restapi/vision#얼굴-검출
        :param image_url: 이미지 url
        :param file: 이미지 파일
        :param threshold: 얼굴 판정의 기준값 | default: 0.7 | 0~1.0
        :return:
        """
        target_url = self.url_maker('/v1/vision/face/detect')

        if image_url is not None:
            payload = {
                'image_url': image_url,
                'threshold': threshold
            }
            return self.post_json(target_url, data=payload)['result']
        elif file is not None:
            payload = {
                'threshold': threshold
            }
            return self.post_json(target_url, file=file, data=payload)['result']


s = Kakao_vision_api()
result = s.vision_face_detect(image_url='https://file.mk.co.kr/meet/neds/2019/10/image_readtop_2019_783017_15698844653918925.jpg')
for i in result['faces']:
    print(i['facial_attributes']['gender'])
