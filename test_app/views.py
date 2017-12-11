# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import Test, Question, Result
from django.http import HttpResponse




###########################################################################
def test_list(request):
  tests = Test.objects.get_queryset().all()
  return render(request, 'tests_list.html', {'tests':tests})


###########################################################################
def one_test(request, pk):
	test = Test.objects.get(pk=pk)
	questions = Question.objects.filter(test=test).order_by('id')
	list1 = []
	for p in questions:	 
			list1.append(p)
	one_question = list1[0]
	result = 0
	qn = len(questions)
	personal = 1
	ans = request.POST.get('ans', '').strip()

		
	if request.method == "POST":
		errors = {}
		name = request.POST.get('name', '').strip()
		surname = request.POST.get('surname', '').strip()
		l = request.POST.get('result_test', '').strip()
		ans = request.POST.get('answers', '').strip()
		if not name:
			errors['name'] = u"Імя є обов'язковим"
		if not surname:
			errors['surname'] = u"Прізвище є обов'язковим"	
			# return render(request, 'one_test.html', 
			# 	{'personal': personal}) 	
		if not l:
			result_test = 0
		else:
			result_test = int(l)
		if not errors:
			num = request.POST.get('test_num', '').strip()
			if not num:
				num = -1

			q = list1[int(num)]	

			if request.POST.get('next') is not None:
				a = '0' 
				one = list1[int(num)].true
				c = request.POST.get('count', '').strip()
				if not c:
					count = 0
				else:
					count = 1	

				if request.POST.get('1a'):
					a = request.POST.get('1a')
					count = count + 1
					if request.POST.get('1a') == one:
						result = 1
				if request.POST.get('1b'):
					a = request.POST.get('1b')
					count = count + 1
					if request.POST.get('1b') == one:
						result = 1
				if request.POST.get('1c'):
					a = request.POST.get('1c')
					count = count + 1
					if request.POST.get('1c') == one:
						result = 1
				if request.POST.get('1d'):
					a = request.POST.get('1d')
					count = count + 1
					if request.POST.get('1d') == one:
						result = 1

				if count == 0:
					if ans:	
						answers = ans 
					num = int(num)
					ch = 'Зробіть вибір!'
					n = num + 1
					return render(request, 'one_test.html',
							 {'one_test':list1[num],'test': test,
							  'num': num, 
							 'result_test': result_test,
							 'name': name, 'surname': surname,
							 'ch': ch, 'qn': qn, 'n': n,
							 'answers': answers})
				elif count > 1:
					if ans:	
						answers = ans
					num = int(num)
					ch = 'Оберіть лише один варіант!!'
					n = num + 1		
					return render(request, 'one_test.html',
							 {'one_test':list1[num],'test': test, 
							 'num': num, 
							 'result_test': result_test,
							 'name': name, 'surname': surname,
							 'ch': ch, 'qn': qn, 'n': n,
							 'answers': answers})
				if ans:
					if ans == '0':	
						answers = a
					else:
						answers = ans + '' + a 	
				else:
					answers = a	
				if result == 1:
					num = int(num) + 1
					result_test = result_test + 1
					if num + 1 <= qn:
						n = num + 1
						return render(request, 'one_test.html',
						 {'one_test':list1[num],'test': test, 'num': num, 
						 'result_test': result_test, 
						 'name': name, 'surname': surname, 'qn': qn, 
						 'n': n, 'answers': answers})
					else:
						data = {}
						data['name'] = name
						data['surname'] = surname
						data['rating'] = result_test
						data['choices'] = answers
						result = Result(**data)
						result.save()
						n = num + 1	
						return render(request, 'finish.html',
						 {'result_test': result_test,
						 'name': name, 'surname': surname, 'qn': qn, 
						 'n': n, 'answers': answers})
				elif result == 0:
					num = int(num) + 1
					if num + 1 <= qn:
						n = num + 1
						return render(request, 'one_test.html',
							 {'one_test':list1[num],'test': test, 
							 'num': num, 
							 'result_test': result_test,
							 'name': name, 'surname': surname,
							  'qn': qn, 'n': n, 'answers': answers})
					else:
						data = {}
						data['name'] = name
						data['surname'] = surname
						data['rating'] = result_test
						data['choices'] = answers
						result = Result(**data)
						result.save()
						n = num + 1	
						return render(request, 'finish.html',
						 {'result_test': result_test,
						 'name': name, 'surname': surname, 
						 'qn': qn, 'n': n, 'answers': answers})
						
		else:				
			return render(request, 'one_test.html', {
			'test': test, 'personal': personal, 'errors': errors})	           
	else:
		num = 0
		personal = 1		
		return render(request, 'one_test.html', {
			'test': test, 'personal': personal})


########################333
def results(request):
  results = Result.objects.get_queryset().all()
  return render(request, 'tests_list.html', {'results':results})