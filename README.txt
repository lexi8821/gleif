About gleif
===========
Gleif is an GEIF database API python wrapper. It abstracts and objectify data returned by the GEIF API.

Official documentation of the GLEIF API is available [here] (https://documenter.getpostman.com/view/7679680/SVYrrxuU)

Usage
=====

  from gleif.record import Record,
  from gleif.search import autocomplete, fuzzysearch

  search_phrase = "Komercni banka"

  entites = fuzzysearch(search_phrase)

  print(entites)

  r = Record(entities[0][1])

  print(r.attributes)

  # Choose one from r.attributes
  isins = r.isins


Licence
=======

Gleif is licenced under GNU GEneral Public Licence v3.0

Authors
=======

Tomas Olexa
