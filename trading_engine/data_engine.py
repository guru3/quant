import pandas as pd
from pandas_datareader import data as data_reader

class data_engine:
	
	def __init__( self, config ):
		self.data_source = config.get('data.source');
		self.data_symbol_list = config.get('data.symbol_list');
		
	def get_data( self, ticker, start_date, end_date ):
		data = data_reader.DataReader( ticker, self.data_source, start_date, end_date );
		data = data['Close'];
		
		# we got the data, now we need to clean it up and fill the NaNs
		all_valid_days = pd.date_range( start = start_date, end = end_date, freq = 'B' )
		data = data.reindex( all_valid_days )  # have data entries for all these days
		data = data.fillna( method = 'ffill' ) # fill NaNs with last valid value
		return data;

	def get_symbols( self ):
		symbol_list_file = open( self.data_symbol_list, 'r' )
		symbol_list = [];
		for line in symbol_list_file.read().splitlines():
			if line.startswith( '#' ):
				continue;
			symbol_list.append( line );
		return symbol_list;