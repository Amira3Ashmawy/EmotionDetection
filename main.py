import cherrypy
import os.path
from Fuetures import Extraction

#http://127.0.0.1:8080/
class BuggedComputersTotorial101:
	def index(self):
		output = '''
		<form action="featureExt" method ="GET">
		Enter Your NAme
		<input type="text" name="sentences" />
		<input type="submit" />
		</form>
		'''
		return output
	index.exposed = True


	def hello(self):
		output = '''
		this is hello page
		'''
		return output
	hello.exposed = True


	def featureExt(self,sentences=None):
		if sentences:
			Extraction(sentences)
			f = open('res.txt','r')
			res = f.read()
			resls = res.split('\n')
			f.close()
			output="The Result is  %s !" % res
			#output+="esraa"
		else:
			output =" You must enter sentences"
		return output
	featureExt.exposed = True

configfile = os.path.join(os.path.dirname(__file__),'server.conf')
cherrypy.quickstart(BuggedComputersTotorial101(),config=configfile)