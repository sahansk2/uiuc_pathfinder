import MySQLdb
from MySQLdb.cursors import DictCursor
import cherrypy
import cherrypy_cors

cherrypy_cors.install()
#Connects to database server
admin_user = "me" or "cs411ppdb_admin"
db_name = "cs411ppdb_experimental" + "_local"

connection = MySQLdb.connect(
    cursorclass=DictCursor,
    user=admin_user,
    passwd="passAdmin1",
    db=db_name
)

@cherrypy.expose
class Courses():
    @cherrypy.tools.json_out()
    def GET(self, dept, num):
        return {'this': 'isacourse'}
    
    @cherrypy.tools.json_out()
    def POST(self):
        pass

    @cherrypy.tools.json_out()
    def DELETE(self):
        pass
    
    @cherrypy.tools.json_out()
    def PUT(self):
        pass


@cherrypy.expose
class Professors():
    @cherrypy.tools.json_out()
    def GET(self):
        pass
    @cherrypy.tools.json_out()
    def POST(self):
        pass
    @cherrypy.tools.json_out()
    def DELETE(self):
        pass
    @cherrypy.tools.json_out()
    def PUT(self):
        pass

@cherrypy.expose
class Section():
    @cherrypy.tools.json_out()
    def GET(self):
        pass
    @cherrypy.tools.json_out()
    def POST(self):
        pass
    @cherrypy.tools.json_out()
    def DELETE(self):
        pass
    @cherrypy.tools.json_out()
    def PUT(self):
        pass


@cherrypy.expose
class Interest():
    @cherrypy.tools.json_out()
    def GET(self):
        pass
    @cherrypy.tools.json_out()
    def POST(self):
        pass
    @cherrypy.tools.json_out()
    def DELETE(self):
        pass
    @cherrypy.tools.json_out()
    def PUT(self):
        pass

conf = {
    '/': {
        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        'cors.expose.on': True
    }
}

cherrypy.quickstart(Courses(), '/', conf)
