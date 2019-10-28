from data_engine import data_engine

class test_data_engine:

	def __init__( self, config ):
		print( 'Testing data engine' )
		self.data_engine = data_engine( config )

	def run( self ):
		#check if data is queried
		symbols = self.data_engine.get_symbols();
		for symbol in symbols:
			data = self.data_engine.get_data( 'AAPL', '2018-01-01', '2018-01-31' )
			assert( data.size == 23 )

		print( '... OK!' );
