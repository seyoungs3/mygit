import pprint
import requests

# 상품과 옵션 정보들을 담고 있는 새로운 객체를 만들어 반환하시오.
# [힌트] 상품 리스트와 옵션 리스트를 금융상품 코드를 기준으로 매칭할 수 있습니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 변수에 저장합니다.
# 3. 2번의 결과 중 key 값이 "baseList" 인 데이터를 변수에 저장합니다.
# 4. 2번의 결과 중 key 값이 "optionList" 인 데이터를 변수에 저장합니다.
# 5. 3번에서 저장된 변수를 순회하며, 4번에서 저장된 값들에서 금융 상품 코드가 
#     같은 모든 데이터들을 가져와 새로운 딕셔너리로 저장합니다.
#     저장 시, 명세서에 맞게 출력되도록 저장합니다.
# 6. 5번에서 만든 딕셔너리를 결과 리스트에 추가합니다.


def get_deposit_products():
    # 본인의 API KEY 로 수정합니다.
    api_key = 'a705f1eb0b39905e84072c14726a1bc3'

    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'

    # http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth=a705f1eb0b39905e84072c14726a1bc3&topFinGrpNo=020000&pageNo=1
    
    params = {
        'auth' : api_key,
        'topFinGrpNo' : '020000',
        'pageNo' : 1
    }
    
    response = requests.get(url, params = params).json()
    return response
    
    
# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    # pprint.pprint(result)
    hmm1 = result['result']['baseList']
    hmm2 = result['result']['optionList']

    ansarr = []
    for i in hmm1:
        big_dict = dict()
        rate_infos_arr = []
        for j in hmm2:
            small_dict = dict()
            if i['fin_prdt_cd'] == j['fin_prdt_cd']:
                small_dict['저축 금리'] = j['intr_rate']
                small_dict['저축 기간'] = j['save_trm']
                small_dict['저축 금리 유형'] = j['intr_rate_type']
                small_dict['저축 금리 유형명'] = j['intr_rate_type_nm']
                small_dict['최고 우대 금리'] = j['intr_rate2']
                rate_infos_arr.append(small_dict)
        big_dict['금리정보'] = rate_infos_arr
        big_dict['금융상품명'] = i['fin_prdt_nm']
        big_dict['금융회사명'] = i['kor_co_nm']
        ansarr.append(big_dict)

pprint.pprint(ansarr)