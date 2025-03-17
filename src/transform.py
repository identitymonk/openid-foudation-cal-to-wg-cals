import icalendar
import pathlib
from pathlib import Path
import argparse
import requests

def main():
    parser = argparse.ArgumentParser(
        prog='python3 transform.py',
        description='Transform OpenID Foundation general iCal data into sepearated Working Group iCals',
        epilog='Open issues if it does not work')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-i', '--input-file', type=pathlib.Path)
    group.add_argument('-u','--url', type=ascii)
    parser.add_argument('-o', '--output-dir', type=pathlib.Path, default="../output")
    parser.add_argument('-f', '--filter', type=ascii)

    args = parser.parse_args()

    cals = {}

    if args.input_file is not None:
        ics_pathname = args.input_file
        ics_path = Path(ics_pathname)
        
        with ics_path.open() as f:
            calendar = icalendar.Calendar.from_ical(f.read())
    else:
        if args.url is not None:
            calData = requests.get(args.url[1:-1]).text
            calendar = icalendar.Calendar.from_ical(calData)
    
    for event in calendar.walk('VEVENT'):
        if event.get("SUMMARY") is None:
            continue
        else:
            if args.filter is not None:
                if args.filter[1:-1] not in event["SUMMARY"]:
                    continue
            if event["SUMMARY"] in cals:
                currentCal = cals[event["SUMMARY"]]
                currentCal.add_component(event)
                cals[event["SUMMARY"]] = currentCal
            else:
                currentCal = icalendar.Calendar()
                currentCal.add_component(event)
                cals[event["SUMMARY"]] = currentCal
    
    for key in cals:
        with open(f"{args.output_dir}/{key.replace('/','_')}.ics", "wb") as f:
            f.write(cals[key].to_ical())


if __name__ == "__main__":
    main()
