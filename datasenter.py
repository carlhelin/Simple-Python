## Klasse for representasjon av et datasenter
#
from regneklynge import Regneklynge
from node import Node

class Datasenter:

	## Oppretter et datasenter
	#
	def __init__(self):
		self._regneklynger = {}

	## Leser inn data om en regneklynge fra fil og legger
	# den til i ordboken
	# @param filnavn filene der dataene for regneklyngen ligger
	def lesInnRegneklynge(self, filnavn):
		fil = open(filnavn, "r")
		navn = filnavn.split(".")[0]
		noderPerRack = int(fil.readline().strip())
		regneklynge = Regneklynge(noderPerRack)
		self._regneklynger[navn] = regneklynge

		for linje in fil:
			data = linje.strip().split()
			for i in range(0, int(data[0])):
				node = Node(int(data[1]), int(data[2]))
				regneklynge.settInnNode(node)

		fil.close()

	## Skriver ut informasjon om alle regneklyngene
	#
	def skrivUtAlleRegneklynger(self):
		for navn in self._regneklynger:
			self.skrivUtRegneklynge(navn)

	## Skriver ut informasjon om en spesifikk regeklynge
	# @param navn navnet på regnekyngen
	def skrivUtRegneklynge(self, navn):
		if navn in self._regneklynger:
			regneklynge = self._regneklynger[navn]
			print(navn, "har", regneklynge.antRacks(), "racks")
			print("Noder med minst 32GB:", regneklynge.noderMedNokMinne(32))
			print("Noder med minst 64GB:", regneklynge.noderMedNokMinne(64))
			print("Noder med minst 128GB:", regneklynge.noderMedNokMinne(128))
		else:
			print("Det finnes ingen regneklynge med dette navnet i datasenteret")
