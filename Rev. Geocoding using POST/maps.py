import random
import string

import cherrypy

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
          <body>
            <form method="post" action="generate">
              <input name="latlng" type="text" value="40.714224,-73.961452">
              <button type="submit">Reverse Geocode</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def generate(self, latlng="34,45"):
      f1 = open("maps.html", "r")
      line1=f1.readlines()
      s=''.join(line1)
      return s.replace("{{VALUE}}", latlng)
        

if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())
