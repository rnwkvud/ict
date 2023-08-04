import xlrd
import json
import os

def excel_to_json(file_path):
    # Excel 파일 열기
    workbook = xlrd.open_workbook(file_path, encoding_override='utf-8')
    # 첫 번째 시트 선택
    sheet = workbook.sheet_by_index(0)
##
    data = []
    # 각 행을 순회하면서 데이터 추출
    for row in range(1, sheet.nrows):  # 첫 번째 행은 헤더이므로 제외하고 시작
        row_data = {}
        term_name = sheet.cell_value(row, 0)  # '용어 명'은 첫 번째 열에 위치
        term_definition = sheet.cell_value(row, 1)  # '용어 정의'는 두 번째 열에 위치
        if term_name != "" and term_definition != "":  # 둘 다 빈 문자열이 아닌 경우에만 추가
            row_data["용어 명"] = term_name
            row_data["용어 정의"] = term_definition
            data.append(row_data)

    # JSON 파일로 저장
    json_data = json.dumps(data, indent=4, ensure_ascii=False)
    with open(os.path.dirname(os.path.abspath(__file__)) + '/output.json', 'w', encoding='utf-8') as json_file:
        json_file.write(json_data)

    print("JSON 파일로 변환 완료.")

# Excel 파일 경로 설정
file_path = os.path.dirname(os.path.abspath(__file__)) + '/용어사전.xls'
# Excel 파일을 JSON으로 변환
excel_to_json(file_path)
