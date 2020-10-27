def parse(family):
	lastname,*members=family.split()
	return lastname.upper(),*members

pr=parse('simpsons homer merge bart lisa sally')
print(pr)