#! /usr/bin/env python
# coding=utf-8

from xml.dom.minidom import parse
import xml.dom.minidom

doc = xml.dom.minidom.parse("movies.xml")
root = doc.documentElement
print("root-name:", root.tagName)
if root.hasAttribute("self"):
	print("root-self:", root.getAttribute("self"))

movies = root.getElementsByTagName("movie")
for movie in movies:
	print("\n----------%s----------" % (movie.getAttribute("title")))
	type = movie.getElementsByTagName("type")[0]
	format = movie.getElementsByTagName("format")[0]
	rating = movie.getElementsByTagName("rating")[0]
	description = movie.getElementsByTagName("description")[0]
	print("Type: {0}\n" \
		"Format: {1}\n" \
		"Rating: {2}\n" \
		"Description: {3}\n"
		.format(type.childNodes[0].data
				, format.childNodes[0].data
				, rating.childNodes[0].data
				, description.childNodes[0].data
				)
		)