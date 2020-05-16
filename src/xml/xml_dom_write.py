
from xml.dom.minidom import Document
doc = Document()

collection = doc.createElement("collection")
collection.setAttribute("self", "New Arrivals")
doc.appendChild(collection)

def createMovie(title, type, format, rating, description):
	typeElement = doc.createElement("type")
	typeElement.appendChild(doc.createTextNode(type))
	
	formatElement = doc.createElement("format")
	formatElement.appendChild(doc.createTextNode(format))
	
	ratingElement = doc.createElement("rating")
	ratingElement.appendChild(doc.createTextNode(rating))
	
	descriptionElement = doc.createElement("description")
	descriptionElement.appendChild(doc.createTextNode(description))
	
	movie = doc.createElement("movie")
	movie.setAttribute("title", title)
	movie.appendChild(typeElement)
	movie.appendChild(formatElement)
	movie.appendChild(ratingElement)
	movie.appendChild(descriptionElement)
	return movie
	
collection.appendChild(createMovie(
	title ="Enemy Behind"
	, type ="War, Thriller"
	, format ="DVD"
	, rating = "PG"
	, description = "Talk about a US-Japan war"
))

collection.appendChild(createMovie(
	title ="Transformers"
	, type ="Anime, Science Fiction"
	, format ="DVD"
	, rating = "R"
	, description = "A schientific fiction"
))

collection.appendChild(createMovie(
	title ="Trigun"
	, type ="War, Thriller"
	, format ="DVD"
	, rating = "PG"
	, description = "Vash the Stampede!"
))

collection.appendChild(createMovie(
	title ="Ishtar"
	, type ="Comedy"
	, format ="DVD"
	, rating = "PG"
	, description = "Viewable boredom"
))

with open("movies.xml", "w") as f:
#	f.write(doc.toprettyxml(indent="\t", newl="\n"))
	doc.writexml(f, indent="\t", addindent="\t", newl="\n", encoding="utf-8")