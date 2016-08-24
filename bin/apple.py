import web

from discounting import map

f=open("test.txt", 'a')



urls = (
	'/game', 'GameEngine', 
	'/', 'index',
	'/week', 'reindex',
	'/month', 'reindex_2',
	'/6_months', 'reindex_3',
	'/year', 'reindex_4',
	'/5_years', 'reindex_5',
	'/25_years', 'reindex_6',
)

app = web.application(urls, globals())
# little hack so that it runs on the web instead of just on your computer
app = app.wsgifunc()


# little hack so that debug mode works with sessions
#if web.config.get('_session') is None:
#    store = web.session.DiskStore('sessions')
#    session = web.session.Session(app, store, initializer={'room': None})
#    web.config._session = session
#else:
#    session = web.config._session

# define render
render = web.template.render('templates/', base="layout")

class index(object):
    def GET(self):
#sets initial values
	    session.room = map.START        
	    web.seeother("/game")		

class reindex(object):
    def GET(self):
#sets initial values
	    session.room = map.reSTART        
	    web.seeother("/game")	

class reindex_2(object):
    def GET(self):
#sets initial values
	    session.room = map.reSTART_2        
	    web.seeother("/game")

class reindex_3(object):
    def GET(self):
#sets initial values
	    session.room = map.reSTART_3        
	    web.seeother("/game")
	
class reindex_4(object):
    def GET(self):
#sets initial values
        session.room = map.reSTART_4        
        web.seeother("/game")

class reindex_5(object):
    def GET(self):
#sets initial values
        session.room = map.reSTART_5        
        web.seeother("/game")

class reindex_6(object):
    def GET(self):
#sets initial values
        session.room = map.reSTART_6        
        web.seeother("/game")

class GameEngine(object):
    def GET(self):
        if session.room.ss_d == "Task Complete":
    		f.write(session.room.ss_a)
    		f.write("\n")
    		f.write(session.room.ll_a)
    		f.write("\n")
    		print session.room.ss_a
    		print session.room.ll_a
		if session.room.ll_a =="IN 9125 DAYS":
			f.close()

        if session.room:
            return render.show_room(room=session.room)
        else:          
            return render.you_died()

    def POST(self):
        form = web.input(action=None)

        if form.action:
            if form.action=="n" or form.action=="v":
            	session.room = session.room.go(form.action)
            else:
            	session.room = session.room
        web.seeother("/game")

if __name__ == "__main__":
	app.run()
