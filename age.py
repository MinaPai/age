drive = input('你有沒有開過車? ')
age = input('請問你幾歲? ')
age = int(age)
if drive == '有':
	if age > 18:
		print('你通過測驗了')
	else:
		print('你違規駕駛!')