'''
zipcheck.py: validation function for US zip code
'''

def zip_errors(z):
    """
    Validate z as either NNNNN or NNNNN-NNNN.
    
    :param z: US zip code which is a string
    :returns: return_type -- description of the return value
    :returns: None for a valid zip code
    :raises: Attrib
    """
    l = len(z)
    if l not in(5,10):
        return "Zip codes should be 5 or 10 characters long"
    if (not z[:5].isdigit() or
        l == 10 and not z[6:].isdigit()):
        return "Zip code contains non-numeric characters"
    if l == 10 and z[5] != "-":
        return "Ten-digit zips must have a dash between the two parts"
    return
