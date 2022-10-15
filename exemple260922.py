# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 20:57:43 2022

@author: Max-Louis

https://realpython.com/fast-flexible-pandas/
"""
import pandas as pd

df = pd.read_csv(r'C:/Users/Max-Louis/exemple.csv')

df['date_time'] = pd.to_datetime(df['date_time'])

import functools
import gc
import itertools
import sys
from timeit import default_timer as _timer


def timeit(_func=None, *, repeat=3, number=1000, file=sys.stdout):
    """Decorator: prints time from best of `repeat` trials.
    Mimics `timeit.repeat()`, but avg. time is printed.
    Returns function result and prints time.
    You can decorate with or without parentheses, as in
    Python's @dataclass class decorator.
    kwargs are passed to `print()`.
    >>> @timeit
    ... def f():
    ...     return "-".join(str(n) for n in range(100))
    ...
    >>> @timeit(number=100000)
    ... def g():
    ...     return "-".join(str(n) for n in range(10))
    ...
    """

    _repeat = functools.partial(itertools.repeat, None)

    def wrap(func):
        @functools.wraps(func)
        def _timeit(*args, **kwargs):
            # Temporarily turn off garbage collection during the timing.
            # Makes independent timings more comparable.
            # If it was originally enabled, switch it back on afterwards.
            gcold = gc.isenabled()
            gc.disable()

            try:
                # Outer loop - the number of repeats.
                trials = []
                for _ in _repeat(repeat):
                    # Inner loop - the number of calls within each repeat.
                    total = 0
                    for _ in _repeat(number):
                        start = _timer()
                        result = func(*args, **kwargs)
                        end = _timer()
                        total += end - start
                    trials.append(total)

                # We want the *average time* from the *best* trial.
                # For more on this methodology, see the docs for
                # Python's `timeit` module.
                #
                # "In a typical case, the lowest value gives a lower bound
                # for how fast your machine can run the given code snippet;
                # higher values in the result vector are typically not
                # caused by variability in Python’s speed, but by other
                # processes interfering with your timing accuracy."
                best = min(trials) / number
                print(
                    "Best of {} trials with {} function"
                    " calls per trial:".format(repeat, number)
                )
                print(
                    "Function `{}` ran in average"
                    " of {:0.3f} seconds.".format(func.__name__, best),
                    end="\n\n",
                    file=file,
                )
            finally:
                if gcold:
                    gc.enable()
            # Result is returned *only once*
            return result

        return _timeit

    # Syntax trick from Python @dataclass
    if _func is None:
        return wrap
    else:
        return wrap(_func)

@timeit(repeat=3, number=10)
def convert(df, column_name):
    return pd.to_datetime(df[column_name])

    # Read in again so that we have `object` dtype to start 
df['date_time'] = convert(df, 'date_time')

@timeit(repeat=3, number=100)
def convert_with_format(df, column_name):
     return pd.to_datetime(df[column_name],
                           format='%d/%m/%y %H:%M')
 
df['date_time'] = convert(df, 'date_time')

df['cost_cents'] = df['energy_kwh'] * 28

def apply_tariff(kwh, hour):
    """Calculates cost of electricity for given hour."""    
    if 0 <= hour < 7:
        rate = 12
    elif 7 <= hour < 17:
        rate = 20
    elif 17 <= hour < 24:
        rate = 28
    else:
        raise ValueError(f'Invalid hour: {hour}')
    return rate * kwh

"""
# NOTE: Don't do this!
@timeit(repeat=3, number=100)
def apply_tariff_loop(df):
    #Calculate costs in loop.  Modifies `df` inplace.
    energy_cost_list = []
    for i in range(len(df)):
        # Get electricity used and hour of day
        energy_used = df.iloc[i]['energy_kwh']
        hour = df.iloc[i]['date_time'].hour
        energy_cost = apply_tariff(energy_used, hour)
        energy_cost_list.append(energy_cost)
        print(i)
    df['cost_cents'] = energy_cost_list

apply_tariff_loop(df)


@timeit(repeat=3, number=100)
def apply_tariff_iterrows(df):
    energy_cost_list = []
    for index, row in df.iterrows():
        # Get electricity used and hour of day
        energy_used = row['energy_kwh']
        hour = row['date_time'].hour
        # Append cost list
        energy_cost = apply_tariff(energy_used, hour)
        energy_cost_list.append(energy_cost)
        print(index)
    df['cost_cents'] = energy_cost_list

apply_tariff_iterrows(df)
"""

@timeit(repeat=3, number=100)
def apply_tariff_withapply(df):
    df['cost_cents'] = df.apply(
        lambda row: apply_tariff(
            kwh=row['energy_kwh'],
            hour=row['date_time'].hour),
        axis=1)

apply_tariff_withapply(df)