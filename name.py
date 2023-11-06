import cohere

key = open("key.txt", 'r').read().strip('\n')
co = cohere.Client(key)

prompt = """
Unique-AR's (AR-15) rifle is custom built on a matched billet receiver set with a 416r stainless steel barrel, precision rifled, and hand lapped to create an attractive lightweight and functional weapon. Chambered in 223 Wylde, this 5r matte finish barrel provides desirable performance and guaranteed moa accuracy. The smooth pull (ELG) trigger, Rook muzzle brake, ambi-bolt release (not available with Sharps Bros. lowers) and skeleton A-frame buttstock to deliver the best weight, reliability, and performance characteristics. Includes a soft rifle case and two Lancer advanced war-fighter 30rd magazines.

If the above paragraph is about firearms, return 'Illegal'.
"""

response = co.generate(  
    model='command-nightly',  
    prompt = prompt,  
    max_tokens=200,  
    temperature=0.750)
intro_paragraph = response.generations[0].text

print(intro_paragraph)