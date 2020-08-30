import pandas as pd
import numpy as np
import math
import time
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
    for batch in range(1, 2):
         resp = get_data(i_offset, api_token)
         resp_list = resp['results']
         resp_dict = process_response(resp_list)

        # sleep for 6 seconds so we do not exceed limit
         time.sleep(t_sleep)
         i_offset+=c.op_offset

    return data_batch

def process_response(resp_list):

    # initialize empty df
    final_df = pd.DataFrame(columns=['title', 'description', 'contributor', 'author', 'contributor_note',
                                     'price', 'age_group', 'publisher', 'rank', 'list_name', 'display_name',
                                     'published_date', 'bestsellers_date', 'weeks_on_list', 'ranks_last_wek',
                                     'asterix', 'dagger'])
    # process data and append to df
    for elem in resp_list:
        f_dict = {key : [value] for key, value in elem.items()}
        f_dict['rank'] = [d['rank'] for d in f_dict['ranks_history'][0]]
        f_dict['list_name'] = [d['list_name'] for d in f_dict['ranks_history'][0]]
        f_dict['display_name'] = [d['display_name'] for d in f_dict['ranks_history'][0]]
        f_dict['published_date'] = [d['published_date'] for d in f_dict['ranks_history'][0]]
        f_dict['bestsellers_date'] = [d['bestsellers_date'] for d in f_dict['ranks_history'][0]]
        f_dict['weeks_on_list'] = [d['weeks_on_list'] for d in f_dict['ranks_history'][0]]
        f_dict['ranks_last_week'] = [d['ranks_last_week'] for d in f_dict['ranks_history'][0]]
        f_dict['asterisk'] = [d['asterisk'] for d in f_dict['ranks_history'][0]]
        f_dict['dagger'] = [d['dagger'] for d in f_dict['ranks_history'][0]]
        # cleanup
        del f_dict['isbns']
        del f_dict['ranks_history']
        del f_dict['reviews']
        # convert to df and full up key values
        f_df = pd.DataFrame.from_dict(f_dict, orient='index').transpose()
        final_df = pd.concat([final_df, f_df])
        print(final_df)
    return None
