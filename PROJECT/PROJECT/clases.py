import xml.dom.minidom


class Parse():

    def lecturaXML(self, archivo):
        domtree = xml.dom.minidom.parse(archivo)

        return domtree
    
    def lecturaNodos(self, domtree):
        definitions = domtree.documentElement

        return 0

