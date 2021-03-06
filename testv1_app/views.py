# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import Test, Question, Result
from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import login_required




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
						tm = datetime.datetime.now()
						data = {}
						data['name'] = name
						data['surname'] = surname
						data['rating'] = result_test
						data['choices'] = answers
						data['tm'] = tm
						data['test_owner'] = test.name
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
						tm = datetime.datetime.now()
						data = {}
						data['name'] = name
						data['surname'] = surname
						data['rating'] = result_test
						data['choices'] = answers
						data['tm'] = tm
						data['test_owner'] = test.name
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


########################
@login_required
def results(request):
  results = Result.objects.get_queryset().all()
  return render(request, 'results.html', {'results':results})





###########################################################################
@login_required
def add_test(request):
    if request.method == "POST":
    	test = request.POST.get('test', '').strip()
    	if not test:
    		if request.POST.get('next') is not None:
		        errors = {}
		        data = {}
		        name = request.POST.get('name', '').strip()
		        if not name:
		        	errors['name'] = 'Назва обовязкова!'   
		        else:
		        	data['name'] = name		              
		        # save
		        if not errors:
		        	test = Test(**data)
		        	test.save()
		        	return render(request, 'add_test.html',
		        	{'test': test})
		        else:
		        	return render(request, 'add_test.html',
		        	{'errors': errors, 'test': test})
    	else:
    		if request.POST.get('next') is not None:
    			errors = {}
    			data = {}
    			description = request.POST.get('description', '').strip()
    			if not description:
    				errors['description'] = 'Назва обовязкова!'
    			else:
    				data['description'] = description
    			version_a = request.POST.get('version_a', '').strip()
    			if not version_a:
    				errors['version_a'] = 'Назва обовязкова!'
    			else:
    				data['version_a'] = version_a
    			version_b = request.POST.get('version_b', '').strip()
    			if not version_b:
    				errors['version_b'] = 'Назва обовязкова!'
    			else:
    				data['version_b'] = version_b
    			version_c = request.POST.get('version_c', '').strip()
    			if not version_c:
    				errors['version_c'] = 'Назва обовязкова!'
    			else:
    				data['version_c'] = version_c
    			version_d = request.POST.get('version_d', '').strip()
    			if not version_d:
    				errors['version_d'] = 'Назва обовязкова!'
    			else:
    				data['version_d'] = version_d
    			true = request.POST.get('true', '').strip()
    			if not true:
    				errors['true'] = 'Назва обовязкова!'
    			else:
    				data['true'] = true
    			test1 = Test.objects.get(name=test)	
    			data['test'] = test1
    			# save
    			if not errors:
    				qn = Question(**data)
    				qn.save()
    				num_qn = len(Question.objects.get_queryset().all())
    				new = 'Нове питання додано!'
    				return render(request, 'add_test.html',
	 	          		{'test': test, 'new': new, 'num_qn': num_qn})
    			else:
    				num_qn = len(Question.objects.get_queryset().all())
    				return render(request, 'add_test.html',
	 	          		{'test': test, 'errors': errors,
	 	          		'num_qn': num_qn})			              	      	
    else:
    	return render(request, 'add_test.html', {})
