# openid-foudation-cal-to-wg-cals
Transform OpenID Foundation general iCal data into sepearated Working Group iCals

## Usage
```
python3 transform.py [-h] (-i INPUT_FILE | -u URL) [-o OUTPUT_DIR] [-f FILTER]

Transform OpenID Foundation general iCal data into sepearated Working Group iCals

options:
  -h, --help            show this help message and exit
  -i INPUT_FILE, --input-file INPUT_FILE
  -u URL, --url URL
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
  -f FILTER, --filter FILTER
```
## Extract from the official feed
`python3 transform.py -u https://calendar.google.com/calendar/ical/o6vc2o4nrv8ihi1dng0l2rhfhs%40group.calendar.google.com/public/basic.ics`

## Notes
An example of the general ics file is provided in `example/basic.ics`. It is an export of the official calendar as of March 17th 2025

