About gleif
===========
Gleif is an GEIF database API python wrapper. It abstracts and objectify data returned by the GEIF API.

Official documentation of the GLEIF API is available [here] (https://documenter.getpostman.com/view/7679680/SVYrrxuU)

Usage
=====

  from gleif import Record, autocomplete, fuzzysearch

  search_phrase = "Komercni banka"

  entites = fuzzysearch(search_phrase)

  print(entites)

  r = Record(entities[0][1])

  print(r.attributes)

  isins = r.isins


Licence
=======

Gleif is licenced underGNU GEneral Public Licence v3.0

Authors
=======

Tomas Olexa
