var bestBeers = new Bloodhound({
  datumTokenizer: Bloodhound.tokenizers.obj.whitespace('value'),
  queryTokenizer: Bloodhound.tokenizers.whitespace,
  prefetch: '../static/beers.json',
});

$('#remote .typeahead').typeahead(null, {
  name: 'best-beers',
  display: 'value',
  source: bestBeers,

});