from flask import Flask, render_template,request
import json

w=json.load(open("worldl.json"))
for c in w:
    c['tld']=c['tld'][1:]
page_size=20
app=Flask(__name__)



@app.route('/')
def mainpage():
    #return 'Seventeen right here'
    #return w[117]['name']
    #return '<br>'.join([c['name'] for c in w])
    return render_template('index.html',
        w=w[0:page_size])

@app.route('/begin/<b>')
def beginPage(b):
    bn = int(b)
    return render_template('index.html',
        w = w[bn:bn+page_size],
        page_number = bn,
        page_size = page_size
        )

@app.route('/country/<i>')
def country(i):
    return render_template('country.html', c = w[int(i)])
    #return w[int(i)]['name']+w[int(i)]['continent']+w[int(i)]['capital']

@app.route('/continent/<a>')
def continent(a):
    c1=[c for c in w if c['continent']==a]
    return render_template (
    	'continent.html',
    	length_of_c1=len(c1),
    	c1 = c1,
    	a = a)

@app.route('/countryByName/<n>')
def countryByName(n):
	c=None
	for x in w:
		if x['name'] == n:
			c=x
	return render_template('country.html',c=c)

@app.route('/delete/<n>')
def deleteCountry(n):
    i=0
    for c in w:
        if c['name']==n:
            break
    i=i+1
    del w[i]
    return render_template('index.html',
        page_number=0,
        page_size=page_size,
        w=w[0:page_size])

@app.route('/editcountryByName/<n>')
def editcountryByName(n):
    c=None
    for x in w:
        if x['name'] == n:
            c=x
    return render_template('countryedit.html',c=c)

@app.route('/updateCountryByName')
def updateCountryByName():
    n=request.args.get('name')
    c=None
    for x in w:
        if x['name'] == n:
            c=x
        c['capital'] =request.args.get('capital')
        c['continent'] =request.args.get('continent')
    return render_template(
            'countryedit.html',
            c=c)


app.run(host='0.0.0.0', port=5641, debug=True)
