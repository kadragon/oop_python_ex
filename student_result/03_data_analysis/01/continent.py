# 국가코드별 대륙(set 자료구조 이용)
asia = {'KR', 'JP', 'CN', 'TH', 'TW', 'VN', 'HK', 'PH', 'RU', 'SG', 'ID', 'MY', 'IR', 'MN', 'MO', 'KH', 'GU', 'SA',
        'KZ', 'LK', 'IN', 'MM', 'KW', 'QA', 'IQ', 'LA', 'OM', 'BN', 'UZ', 'BD', 'LB', 'BH', 'KG', 'PK', 'NP', 'TL',
        'MV', 'JO'}
africa = {'TN', 'TZ', 'GH', 'ZA', 'EG', 'CI', 'AE', 'GN', 'SC', 'NG', 'MR', 'KE', 'SN', 'LY', 'RW', 'TG', 'BJ', 'MZ',
          'MU', 'GW', 'MA', 'LR', 'SD', 'RE', 'DZ', 'UG', 'SL', 'GM', 'NA', 'AO', 'MG', 'SO', 'TZ', 'CG'}
america = {'US', 'CA', 'EC', 'MX', 'UY', 'BR', 'CL', 'SR', 'AR', 'PY', 'PE', 'GT', 'BO', 'CO', 'PA', 'BZ', 'NI', 'DO',
           'HN', 'CU', 'VE', 'GL', 'FK', 'AG', 'GY', 'HT'}
europe = {'FR', 'ES', 'IT', 'DE', 'PT', 'GB', 'NL', 'BE', 'TR', 'UA', 'MP', 'MT', 'AT', 'PL', 'CH', 'LT', 'CZ', 'NO',
          'IL', 'SE', 'GR', 'LV', 'EE', 'DK', 'HU', 'MK', 'FI', 'GE', 'BG', 'SK', 'IE', 'IS', 'RO', 'HR', 'AL', 'FO',
          'CY'}
oceania = {'AU', 'NZ', 'VU', 'KI', 'FJ', 'FM', 'SB', 'PF', 'PW', 'MH', 'PG', 'AS', 'TO'}

# 대륙 set의 리스트와 대륙 이름의 리스트
world = [asia, africa, america, europe, oceania]
world_name = ["asia", "africa", "america", "europe", "oceania"]


def get_where_continent(country):
    """
    나라를 인자로 넘겨 받아 속해 있는 대륙을 반환합니다. 
    :parameter country: 어느 대륙에 속해 있는지 알고 싶은 나라입니다. 
    :return: 대륙 이름을 반환합니다. (asia, europe 등)
    """
    for i in range(len(world)):
        if country in world[i]:
            return world_name[i]


def num_of_country(cont):
    """
    대륙 이름을 인자로 넘겨 받아 그 대륙의 속한 국가의 수를 반환힙니다. 
    :parameter cont: 국가 수를 알고 싶은 대륙입니다. 
    :return: 그 대륙에 속한 국가의 수를 반환합니다.
    """
    for i in range(len(world)):
        if world_name[i] == cont:
            return len(world[i])


if __name__ == "__main__":
    print("test...")
    print('kr'.upper() in asia)
