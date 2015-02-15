#!/usr/bin/env python

"""Print a loaddata-compatible JSON string for the Weight model."""

pts = \
    [ #("2015-02-15T10:10:00+10:00", 50.0, 20.0, 10)
    #, ("2015-02-16T10:11:00+10:00", 50.5, 20.1, 11)
    ]

fmt = r'''{
  "model": "weight.weight",
  "fields": {
    "time": "%s",
    "kg": %f,
    "body_fat": %f
  },
  "pk": %d
}'''

str_entries = [fmt % p for p in pts]

print('[')
print(',\n'.join(str_entries))
print(']')
