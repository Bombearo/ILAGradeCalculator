def remove_n_smallest(lst, n):
	return sorted(lst)[n:]

def WeeklyQuizzes (arr):
	listr = list(map(float, arr))
	grades = remove_n_smallest(listr,2)
	return (sum(float(i) for i in grades) / (len(grades)*10))*40

def Handins(arr):
	listr = list(map(float, arr))
	listdiv = [i/2 for i in listr]
	grades = remove_n_smallest(listdiv,1)
	return float(sum(float(i) for i in grades)/30)*100
# TODO: Add Synoptic Test
def Synoptic(p):
	return 30 * float(p/100)
def AnnoyingGradeBoundaries(g):
	# Inspired by yandere dev <3
	if g>=90:
		return "A1: Excellent"
	elif g < 90 and g >= 80:
		return "A2: Excellent"
	elif g < 80 and g >= 70:
		return "A3: Excellent"
	elif g < 70 and g >= 60:
		return "B: Very Good"
	elif g < 60 and g >= 50:
		return "C: Good"
	elif g < 50 and g > 40:
		return "D: Passing"
	else:
		return "Failing"

def main():
	week = input("what week of ILA have you last completed \n")
	handins = input("how many hand-ins have you done \n")
	has_synoptic = input("have you done the synoptic yet: Y/n \n")
	quizzes = []
	handin_result_list = []
	synoptic = 0
	i = 1
	j = 1
	while i <= int(week):
		quizzes.append(input("what was your grade out of 10 for week"+str(i)+"\n"))
		i+=1
	while j <= int(handins):
		handin_result_list.append(input("what did you get for handin "+str(j)+"\n"))
		j+=1
	if has_synoptic.lower() == "y":
		synoptic = input("what did you get for your synoptic")
	weekly_results = WeeklyQuizzes(quizzes)
	handin_results = Handins(handin_result_list)
	print("Your grade is:")
	print(f"For Weekly Quizzes, you have {str(weekly_results)}% out of the 40% available")
	print(f"For Hand-ins, you have {str(float(handin_results/100)*30)}% out of the 30% available")
	# get results, and get ready for your mood to come tumbling down, tumbling down, tumbling down. https://www.youtube.com/watch?v=rQiHzcdUPAU
	# why are you reading the comments and why did i add something unfunny to it
	# oh well, hi!
	if synoptic:
		synoptic_results = Synoptic(synoptic)
		print(f"For the synoptic test, you have {str(synoptic_results*100)}%")
		print(f"Your total is: {str((weekly_results+(float(handin_results/100)*30)+synoptic_results))}%")
		print(f"Your Grade Boundary is: {AnnoyingGradeBoundaries((weekly_results+(float(handin_results/100)*30)+synoptic_results))} out of the 30% available")
	else:
		if week == 10:
			print("ignore the scaling now")
		print(f"Your current total is: {str((weekly_results+(float(handin_results/100)*30)))}% out of your available 70% (scaled to 100% it would be: {str((weekly_results+(float(handin_results/100)*30))*1.42857142857)}")
		print(f"Your Grade Boundary is: {AnnoyingGradeBoundaries((weekly_results+(float(handin_results/100)*30)))} scaled: {AnnoyingGradeBoundaries((weekly_results+(float(handin_results/100)*30))*1.42857142857)}")
if __name__ == '__main__':
	main()

