import pandas as pd
import matplotlib.pyplot as plt
from math import ceil

# 엑셀 데이터 상의 최소, 최대 연도
MIN_YEAR = 1990
MAX_YEAR = 2017

def show_philips_curve(x_axis, y_axis, year_range):
    """
    (x_axis: array<float>,
     y_axis: array<float>, 
     year_range: (start=int, end=int)) -> None
     
    시작, 끝 연도를 받아서 범위 내의 필립스 곡선을 보여주는 함수
    """
    
    plt.figure(figsize=(20, 10))
    
    start = year_range[0]
    end = year_range[1]
    
    data_range = slice(start - MIN_YEAR, end - MIN_YEAR + 1)
    data_x_axis = x_axis['data'][data_range]
    data_y_axis = y_axis['data'][data_range]
    
    plt.plot(data_x_axis, data_y_axis, marker='o')
    
    # 3 칸을 추가하면 더 보기가 쉽다
    max_x_value = ceil(max(data_x_axis)) + 3
    max_y_value = ceil(max(data_y_axis)) + 3
    
    plt.axis([0, max_x_value, 0, max_y_value])
    plt.xticks(range(max_x_value + 1))
    plt.yticks(range(max_y_value + 1))
    
    plt.xlabel(x_axis['label'])
    plt.ylabel(y_axis['label'])
    
    for year in range(start, end + 1):
        index = year - start
        plt.annotate(year, (data_x_axis[index], data_y_axis[index]) )

    plt.show()
    
def load_data():
    """
    () -> (dict, dict)
    
    물가상승률과 실업률 엑셀 파일을 읽어들여서 각각을 data와 label_name을 가진 데이터로 반환
    """

    excel_files = ('inflation_rates.xls', 'unemployment_rates.xls')

    unemployment_rate = {
        'data': pd.read_excel(excel_files[1]).loc['실업률(%)'].values,
        'label': 'unemployment rate'
    }

    inflation_rate = {
        'data': pd.read_excel(excel_files[0]).loc['소비자물가상승률(%)'].values,
        'label': 'inflation rate'
    }
    
    # TODO: fix manual float conversion
    # 일부 데이터가 str 타입으로 로드되는 문제가 있음
    unemployment_rate['data'] = [float(n) for n in unemployment_rate['data']]
    
    return unemployment_rate, inflation_rate
    
def main():
    print(f'필립스 곡선을 보여주는 프로그램입니다. {MIN_YEAR}년부터 최대 {MAX_YEAR}년까지의 데이터를 조회할 수 있습니다. \n')
    start_year = int(input(f'시작년도를 입력해주세요. ex) {MIN_YEAR} \n'))
    end_year = int(input(f'마지막년도를 입력해주세요. ex) {MAX_YEAR} \n'))
    
    if (start_year < MIN_YEAR) or (end_year > MAX_YEAR):
        print("error: year out of range")
        return
    
    unemployment_rate, inflation_rate = load_data()

    show_philips_curve(
        x_axis=unemployment_rate, 
        y_axis=inflation_rate, 
        year_range=(start_year, end_year)
    )

main()    
       
