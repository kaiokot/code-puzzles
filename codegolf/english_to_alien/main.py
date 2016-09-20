
 #!/usr/bin/python

def to_alien(name):
	alien_vowels = {"a":"obo","e":"unu","i":"ini","o":"api","u":"iki"}
	out = ''
	for ch in name:
		if ch.lower() in alien_vowels:
			out +=   ch.replace(ch,alien_vowels[ch.lower()].capitalize() if ch.istitle() else alien_vowels[ch.lower()])
		else:
			out += ch

	return out

if __name__ =="__main__":
	names = ["Kaio","Nelice","Brasil","Shaun", "Java", "Hello World!", "Australia"]
	for n in names:
		print (n,to_alien(n))
