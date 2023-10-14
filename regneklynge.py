## Klasse for representasjon av regneklynge i et datasenter.
#
from rack import Rack
from node import Node

class Regneklynge:
	## Oppretter en regneklynge og setter maks antall
	# det er plass til i et rack
	# @param noderPerRack max antall noder per rack
	def __init__(self, noderPerRack):
		self._racks = []

		if noderPerRack > 0:
			self._noderPerRack = noderPerRack
		else:
			self._noderPerRack = 1

	## Plasserer en node inn i et rack med ledig plass, eller i et nytt
	# @param node referanse til noden som skal settes inn i datastrukturen
	def settInnNode(self, node):
		ledigRack = None
		i = 0

		while ledigRack == None and i < len(self._racks):
			if self._racks[i].getAntNoder() < self._noderPerRack:
				ledigRack = self._racks[i]
			i += 1

		if ledigRack == None:
			ledigRack = Rack()
			self._racks.append(ledigRack)

		ledigRack.settInn(node)

	## Beregner totalt antall prosessorer i hele regneklyngen
	# @return totalt antall prosessorer
	def antProsessorer(self):
		antPros = 0
		for rack in self._racks:
			antPros += rack.antProsessorer()
		return antPros

	## Beregner antall noder i regneklyngen med minne over angitt grense
	# @param paakrevdMinne hvor mye minne skal noder som telles med ha
	# @return antall noder med tilstrekkelig minne
	def noderMedNokMinne(self, paakrevdMinne):
		antNoder = 0
		for rack in self._racks:
			antNoder += rack.noderMedNokMinne(paakrevdMinne)
		return antNoder

	## Henter antall racks i regneklyngen
	# @return antall racks
	def antRacks(self):
		return len(self._racks)
