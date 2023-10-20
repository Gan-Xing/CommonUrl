const html2json = require('html2json').html2json;

function convert(html) {
	return html2json(html);
}

module.exports = convert;
