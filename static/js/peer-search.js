var peersList = [
	"Ella Brown",
	"Derek Jacobs",
	"Joanna Pope",
	"Max Thompson",
	"Lily Downey",
	"Joseph Hugener",
	"Vivek Rao",
	"Helena Vazov",
	"Catherine Huffman",
	"Hanna Macguire",
	"Tommy Rosenberg",
	"Sammy Allen",
	"Elsa Manchester",
	"Julia Reagan",
	"Brandon Zimmerman",
	"Stephen Brown",
	"Chris Olson",
	"Amy Tyler"
];

$(document).ready(function() {
	$("#peer-search").autocomplete({
		source: peersList,
		select: function() {
			var name = $("#peer-search").val().split(" ")[0].toLowerCase();
			console.log(name);
			$(".panel").hide();
			$("."+name).show();
		}
	});
})