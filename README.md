## Synopsis

A script to mimic the capabilities of IRAF's hedit command

## Code Example

Below is the usage for ```fitshedit``` and some examples of editing fits headers

```
usage: fitshedit [-h] [-e E] [-k K] [--dry_run] [--verify] filename

A convenience script to edit fits headers

positional arguments:
  filename           Filename or wildcard list of filenames

optional arguments:
  -h, --help         show this help message and exit
  -e E, --ext E      Extension of HDU to edit
  -k K, --keyword K  Header keyword to edit. This can be used mutliple times
  --dry_run          Show changes but do not commit them
  --verify           Verify each file change manually before commiting
```

To edit the image ```test.fits``` setting the header keyword ```EXPTIME``` to ```35``` instead of the current value of ```30```. Run:

```
$> fitshedit test.fits -k EXPTIME=30
Updating EXPTIME=35 --> 30
```

It is also possible to give multiple keywords using ```-k``` each time:

```
$> fitshedit test.fits -k EXPTIME=30 -k IMAGTYP='FLAT FIELD'
Updating EXPTIME=35 --> 30
Updating IMAGTYP=TEST --> FLAT FIELD
```

If a keyword does not exist, it is created. ```--dry_run``` can be used to see the changes without applying them. ```--verify``` is used to manually verify each combined changes for each file.

## Motivation

I want to get away from IRAF, but I like some of its features. I am therefore writing them in Python

## Installation

```
git clone https://github.com/jmccormac01/fitshedit.git
```

## API Reference

N/A

## Tests

To do

## Contributors

James McCormac

## License

MIT License

