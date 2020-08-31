## Lindy Books

The notebook in this repo extracts books from the NY Times Bestseller list that adhere to the lindy effect.


> **Lindy Effect**:<br>
> The Lindy effect is a theory that the future life expectancy of some non-perishable things like a technology, an idea
> or a book is proportional to their current age, so that every additional period of survival implies a longer remaining life expectancy.

*Dependencies:* `Python 3`

---
**Setup**

1. run `pip install requirements.txt` in the console (ideally in a virtual environment).
2. create a developer account at https://developer.nytimes.com/ and create an app. This will provide
   you with an API-key.
3. create an `auth.yaml` file in the root directory of this project and copy your NY-Times API-KEY into
   the file like so:

    `api-key : 'YOUR API KEY'`

---
**Usage**

1. run `jupyter notebook` on the console and open `lindy_books_list.ipynb`.
2. if you want to load just a few batches of data (each batch contains 20 books) then
   set `n_batches` in the function call `get_ny_times_data('auth.yaml', n_batches=None)`.
   If nothing is set, then all the data is loaded.
3. Click on `Cell` and `Run All`.
4. Sit back and wait for a few hours until results are displayed.
5. Modify the notebook to explore books regarding different dimensions.

Note: Fetching the data from the NY-Times-API takes approx. 2-3 hours due to request limits.
If you want to speed up things contact NY-Times and request to lift these limits.

---
**License**<br>
Apache Software License 2.0
