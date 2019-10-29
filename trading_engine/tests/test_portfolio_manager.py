from portfolio_manager import portfolio_manager

class test_portfolio_manager:

	def __init__( self, config ):
		print( 'Testing portfolio manager' )
		self.portfolio_manager = portfolio_manager( config )

	def run( self ):
		symbol_to_query = 'AAPL';
		#let's start with zero
		self.portfolio_manager.set_position( symbol_to_query, 0.0 );
		assert( self.portfolio_manager.get_position( symbol_to_query ) == 0 )

		#let's buy 1000
		self.portfolio_manager.buy( symbol_to_query, 1000 )
		assert( self.portfolio_manager.get_position( symbol_to_query ) == 1000 )
		#let's sell 500
		self.portfolio_manager.sell( symbol_to_query, 500 )
		assert( self.portfolio_manager.get_position( symbol_to_query ) == 500 )
		#let's reverse position
		self.portfolio_manager.reverse_position( symbol_to_query )
		assert( self.portfolio_manager.get_position( symbol_to_query ) == -500 )

		#let's buy 500 again
		self.portfolio_manager.buy( symbol_to_query, 500 )
		assert( self.portfolio_manager.get_position( symbol_to_query ) == 0 )

		print( '... OK!' );