import stringprep
import unicodedata


def unicode_normalizer(source: str, param: str="value")-> str:
    """This function is based off of passlib.utils.saslprep"""
    """Normalizes unicode strings using SASLPrep stringprep profile.

    The SASLPrep profile is defined in :rfc:`4013`.
    It provides a uniform scheme for normalizing unicode usernames
    and passwords before performing byte-value sensitive operations
    such as hashing. Among other things, it normalizes diacritic
    representations, removes non-printing characters, and forbids
    invalid characters such as ``\\n``. Properly internationalized
    applications should run user passwords through this function
    before hashing.

    :arg source: str
        unicode string to normalize & validate

    :param param: str:
        Optional noun identifying source parameter in error messages
        (Defaults to the string ``"value"``). This is mainly useful to make the caller's error
        messages make more sense contextually.

    :raises ValueError:
        if any characters forbidden by the SASLPrep profile are encountered.

    :raises TypeError:
        if input is not :class:`!str`

    :returns str
    """
    # saslprep - http://tools.ietf.org/html/rfc4013
    # stringprep - http://tools.ietf.org/html/rfc3454
    #              http://docs.python.org/library/stringprep.html

    if not isinstance(source, str):
        raise TypeError("source must be str, not %s" % type(source))


    sp = stringprep
    # mapping stage
    #   - map non-ascii spaces to U+0020 (stringprep C.1.2)
    #   - strip 'commonly mapped to nothing' chars (stringprep B.1)
    USPACE = " "
    data = ''.join(
        USPACE if sp.in_table_c12(c) else c
        for c in source if not sp.in_table_b1(c)
    )

    # normalize to KC form
    data = unicodedata.normalize('NFKC', data)
    if not data:
        return ""

    # check for invalid bi-directional strings.
    # stringprep requires the following:
    #   - chars in C.8 must be prohibited.
    #   - if any R/AL chars in string:
    #       - no L chars allowed in string
    #       - first and last must be R/AL chars
    # this checks if start/end are R/AL chars. if so, prohibited loop
    # will forbid all L chars. if not, prohibited loop will forbid all
    # R/AL chars instead. in both cases, prohibited loop takes care of C.8.
    if sp.in_table_d1(data[0]):
        if not sp.in_table_d1(data[-1]):
            raise ValueError(f"malformed bidi sequence in {param}")
        # forbid L chars within R/AL sequence.
        is_forbidden_bidi_char = stringprep.in_table_d2
    else:
        # forbid R/AL chars if start not setup correctly; L chars allowed.
        is_forbidden_bidi_char = sp.in_table_d1

    # check for prohibited output - stringprep tables A.1, B.1, C.1.2, C.2 - C.9
    for c in data:
        # check for chars mapping stage should have removed
        assert not sp.in_table_b1(c), "failed to strip B.1 in mapping stage"
        assert not sp.in_table_c12(c), "failed to replace C.1.2 in mapping stage"

        # check for forbidden chars
        if sp.in_table_a1(c):
            raise ValueError(f"unassigned code points forbidden in {param}")
        if sp.in_table_c21_c22(c):
            raise ValueError(f"control characters forbidden in {param}")
        if sp.in_table_c3(c):
            raise ValueError(f"private use characters forbidden in {param}")
        if sp.in_table_c4(c):
            raise ValueError(f"non-char code points forbidden in {param}")
        if sp.in_table_c5(c):
            raise ValueError(f"surrogate codes forbidden in {param}")
        if sp.in_table_c6(c):
            raise ValueError(f"non-plaintext chars forbidden in {param}")
        if sp.in_table_c7(c):
            # XXX: should these have been caught by normalize?
            # if so, should change this to an assert
            raise ValueError(f"non-canonical chars forbidden in {param}")
        if sp.in_table_c8(c):
            raise ValueError(f"display-modifying / deprecated chars forbidden in {param}")
        if sp.in_table_c9(c):
            raise ValueError(f"tagged characters forbidden in {param}")

        # do bidi constraint check chosen by bidi init, above
        if is_forbidden_bidi_char(c):
            raise ValueError(f"forbidden bidi character in {param}")

    return data
