
class portfolio_manager:

	def __init__( self, config ):
		portfolio_file_name = config.get('portfolio.file')
		self.portfolio = config_reader.read_config( portfolio_file_name )

	def buy( self, symbol, quantity ):
		# we bought, so add the quantity in our portfolio
		self.portfolio[ symbol ] = self.portfolio[ symbol ] + quantity;

	def sell( self, symbol, quantity ):
		# we sold, so we remove the quantity in our portfolio
		self.portfolio[ symbol ] = self.portfolio[ symbol ] - quantity;

	def __del__( self ):
		portfolio_file_name = config.get('portfolio.file')
		config_manager.write_config( portfolio_file_name, self.portfolio );
		
