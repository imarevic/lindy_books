import pandas as pd
import numpy as np
import math
from src.helpers import *
import src.consts as c

def get_ny_times_data(auth_filename):

    # api key
    api_key = get_api_key('auth.yaml')
    # determine n iterations
    resp = get_data(c.initial_offset, api_key)
    n_results = resp['num_results']
    if n_results % c.op_offset == 0:
        n_iter = n_results / c.op_offset
    else:
        n_iter = math.ceil(n_results / c.op_offset)
    # get base schema
    

    # load data
    data = get_books_data(n_iter, c.req_sleep, api_key)

def get_books_data(n_iter, t_sleep, api_token):

    i_offset = c.op_offset
    for batch in range(1, 4):
         resp = get_data(i_offset, api_token)
         data_batch = pd.json_normalize(resp['results'])

         i_offset+=c.op_offset

    return None
