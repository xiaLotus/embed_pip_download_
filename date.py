from datetime import datetime, timedelta
import calendar

# 获取今天的日期
today = datetime.now()

# # 找上個月的月份和日期
# last_month_year = today.year if today.month > 1 else today.year - 1
# last_month_month = today.month - 1 if today.month > 1 else 12

# # 找上個月有幾天
# last_month_days = calendar.monthrange(last_month_year, last_month_month)[1]

# # 找上個月個今天，比如今天是4/15，那就會找3/15
# query_date = today.replace(year = last_month_year, month = last_month_month)

print("今天日期", today)
# print("上個月的日期:", query_date)
# print("上個月的天數:", last_month_days)



# import pip

# 下載 calendra 包
# pip.main(['install', 'calendra'])
