import data_engine as dataE;

class trading_engine:

	def __init__( self ):
		pass

	def exit( self ):
		print('Exiting...')
	
	def main( self ):
		print('Welcome to the trading engine!')
		self.exit();

if __name__ == "__main__":
    te = trading_engine()
    te.main()