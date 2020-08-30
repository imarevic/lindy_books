base_url = 'https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json'
api_key_name = 'api-key'
# offsets
initial_offset = 0
op_offset = 20
# api limits
max_req_per_minute = 10
max_req_per_day = 4000
req_sleep = 60 / max_req_per_minute
