$(function() {

	$('select[multiple].active.3col').multiselect({
	  columns: 2,
	  placeholder: 'Select States',
	  search: true,
	  searchOptions: {
	      'default': 'Search States'
	  },
	  selectAll: true
	});

});