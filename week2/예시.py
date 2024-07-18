import datetime


def find_weekday(year, month, day):
    # 주어진 날짜 객체 생성
    date = datetime.date(year, month, day)

    # 요일을 숫자로 반환 (월요일=0, 일요일=6)
    weekday_number = date.weekday()

    # 숫자를 요일 문자열로 변환
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekday_name = weekdays[weekday_number]

    return weekday_name


# 현재 날짜를 입력받기
year = 2024
month = int(input("Month: "))
day = int(input("Day: "))

# 요일 찾기
weekday = find_weekday(year, month, day)
print(f"The date {month}/{day}/{year} is a {weekday}.")
