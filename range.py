import mappings

def get_range(continent):
    lower = 0
    upper = 0
    for country in continent:
        try:
            value =  mappings.get_int_by_alpha2(country)
            if not lower or value < lower:
                lower = value
            if value > upper:
                upper = value
        except:
            pass
    return '{} - {}'.format(lower, upper)
africa  = [ k for k,v in mappings.countries.items() if v == '00001' ]
oceania = [ k for k,v in mappings.countries.items() if v == '00010' ]
asia    = [ k for k,v in mappings.countries.items() if v == '00011' ]
antarctica = [ k for k,v in mappings.countries.items() if v == '00100' ]
europe = [ k for k,v in mappings.countries.items() if v == '00101' ]
s_america = [ k for k,v in mappings.countries.items() if v == '00110' ]
n_america = [ k for k,v in mappings.countries.items() if v == '00111' ]
print 'africa:{}'.format(get_range(africa))
print 'oceania:{}'.format(get_range(oceania))
print 'asia:{}'.format(get_range(asia))
print 'antarctica:{}'.format(get_range(antarctica))
print 'europe:{}'.format(get_range(europe))
print 's_america:{}'.format(get_range(s_america))
print 'n_america:{}'.format(get_range(n_america))

