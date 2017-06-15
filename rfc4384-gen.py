#!/usr/bin/env python
#https://tools.ietf.org/html/rfc4384
#<AS>:<R><X><CC>
#<AS> is the 16-bit AS
#<R>  is the 5-bit Region Identifier
#<X>  is the 1-bit satellite link indication
#X = 1 for satellite links, 0 otherwise
#<CC> is the 10-bit ISO-3166-2 country code
import logging
import argparse
import mappings

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='count', help='Increase verbosity')
    parser.add_argument('country', help='Country Name')
    args = parser.parse_args()
    log_level = logging.ERROR
    if args.verbose == 1:
        log_level = logging.WARN
    elif args.verbose == 2:
        log_level = logging.INFO
    elif args.verbose > 2:
        log_level = logging.DEBUG
    logging.basicConfig(level=log_level)
    print int(mappings.get_bit_string(args.country),2)

if __name__ == "__main__":
    main()
