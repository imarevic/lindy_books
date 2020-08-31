import pandas as pd
import numpy as np
import math
import time
from src.helpers import *
import src.consts as c

# initialize empty df
init_df = pd.DataFrame(columns=['title', 'description', 'contributor', 'author', 'contributor_note',
                                     'price', 'age_group', 'publisher', 'rank', 'list_name', 'display_name',
                                     'published_date', 'bestsellers_date', 'weeks_on_list', 'ranks_last_week',
                                     'asterix', 'dagger'])


def get_ny_times_data(auth_filename, n_batches=None):

    # api key
    api_key = get_api_key('auth.yaml')
    # determine n iterations
    resp = get_data(c.initial_offset, api_key)
    n_results = resp['num_results']
    if n_results % c.op_offset == 0:
        n_iter = n_results / c.op_offset
    else:
        n_iter = math.ceil(n_results / c.op_offset)
    if n_batches != None:
        n_iter = n_batches
    # estimate loading time
    estimated_loading_time = (n_iter * c.req_sleep) // 60
    print("Estimated loading time: {} minutes.".format(estimated_loading_time))
    # load and preprocess data
    data = get_books_data(init_df, n_iter, c.req_sleep, api_key)
    return data

def get_books_data(init_df, n_iter, t_sleep, api_token):

    data_batch = init_df.copy()
    i_offset = c.op_offset
    for batch in range(1, n_iter):
        resp = get_data(i_offset, api_token)
        resp_list = resp['results']
        resp_df = process_response(init_df, resp_list)
        data_batch = pd.concat([data_batch, resp_df])
        # sleep for 6 seconds so we do not exceed limit
        print("{}/{} batches loaded.".format(batch, n_iter))
        time.sleep(t_sleep)
        i_offset+=c.op_offset

    return data_batch

def process_response(init_df, resp_list):

    processed_df = init_df.copy()
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
        # convert to df and fill up key values
        f_df = pd.DataFrame.from_dict(f_dict, orient='index').transpose()
        f_df.fillna(method='ffill', inplace=True)
        processed_df = pd.concat([processed_df, f_df])

    return processed_df
