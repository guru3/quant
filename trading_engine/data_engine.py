from pandas_datareader import data as data_reader
import pandas as pd

class data_engine:
	
	def __init__( self ):
		self.data_source = 'yahoo';
		
	def get_data( self, ticker : str, start_date : str, end_date : str ):
		data = data_reader.DataReader( ticker, data_source, start_date, end_date );
		data = data['Close'];

		# we got the data, now we need to clean it up and fill the NaNs
		all_valid_days = pd.data_range( start = start_date, end = end_date, freq = 'B' )
		data = data.reindex( all_valid_days )  # have data entries for all these days
		data = data.fillna( method = 'ffill' ) # fill NaNs with last valid value
		return data;

	def get_symbols( self ):
		stock_symbol_lists = './stock_sym.te'
		symbol_list_file = open( stock_symbol_lists, 'r' )
		symbol_list = [];
		for line in symbol_list_file.read().splitlines():
			if line.startswith( '#' ):
				continue;
			symbol_list.append( line );
		return symbol_list;
