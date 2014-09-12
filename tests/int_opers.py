#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(os.path.pardir)

from cpmoptimize import cpmoptimize


# Some global constant
global_const = 4

def raw_int_opers(n):
    # Definition of using some global variable
    global global_var
    
    # Some local constants
    local_const = 9
    k1_base = 4
    k1_or = 32
    k2 = 3
    offset = -43
    
    # Some variables
    a = 1
    b = 2
    res = 0
    # Test complex "xrange" expression
    # in loop with used but not modified counter
    for i in xrange(n, -143, -23):
        # Test stack usage and expressions processing
        a, b = b, a
        a, b = b, (a + b * (k1_base | k1_or)) * k2 + offset
        c = b
        
        # Test unary operations with constants
        d = 4348
        d -= +d
        d += -d
        d -= not local_const
        d += ~global_const
        
        # Test unary operations with variables
        c = +c
        c = -c
        
        # Test binary operations with constants
        e = 8944
        e -= local_const ** global_const
        e += local_const * global_const
        e -= local_const / global_const
        e += local_const // global_const
        e -= local_const % global_const
        e += local_const + global_const
        e -= local_const - global_const
        e += local_const >> global_const
        e -= local_const & global_const
        e += local_const ^ global_const
        e -= local_const | global_const
        g = f = e
        
        # Execute some namescope resolutions
        global_var = g
        local_var = global_var
        
        # Test binary operations with variables
        h = d - e
        loop_const = 321
        h = g * loop_const + d * local_const + a * loop_const + i
        a += h
        a += i
        res += a
    else:
        # Test "else" case
        res += 8943 * (res ^ 2321)
    # Test that local and global variables were successfully assigned
    # after the ending of the loop
    res += global_var + local_var
    
    r = 3
    # Loop with unused counter
    for it1 in xrange(-3231, n):
        r = r - 33 + d * 2
    
    q = 43
    # Loop with used and modified counter
    for it2 in xrange(-3231, n, 4345):
        q = (3 + 4) * q - (it2 * 2 - 8) * 3
        it2 = q + 3 - e
    
    # Empty loop
    for it3 in xrange(n):
        pass
    
    # Return ordered list with values of all local variables
    return tuple(sorted(locals().items(), key=lambda item: item[0]))

cpm_int_opers_no_mc = cpmoptimize(
    strict=True, iters_limit=0,
    opt_min_rows=False, opt_clear_stack=False,
)(raw_int_opers)
cpm_int_opers_no_m = cpmoptimize(
    strict=True, iters_limit=0,
    opt_min_rows=False,
)(raw_int_opers)
cpm_int_opers_no_c = cpmoptimize(
    strict=True, iters_limit=0,
    opt_clear_stack=False,
)(raw_int_opers)
cpm_int_opers = cpmoptimize(
    strict=True, iters_limit=0,
)(raw_int_opers)


if __name__ == '__main__':
    import core

    core.run(
        'int_opers', None,
        [
            ('raw', raw_int_opers),
            ('cpm -mc', cpm_int_opers_no_mc),
            ('cpm -m', cpm_int_opers_no_m),
            ('cpm -c', cpm_int_opers_no_c),
            ('cpm', cpm_int_opers),
        ],
        [
            ('linear', 'linear', core.linear_scale(500000, 25)),
        ],
        True, True,
    )