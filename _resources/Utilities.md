---
layout: page
title: Utilities
---

<script type="text/javascript" src="/public/js/resources/utilities.js"></script>
<script>

function noopEncodeString(inputString) {
	return inputString
}

var idToFunctionMapping = {
	"decodedText" : { "encode" : noopEncodeString,
			  "decode" : noopEncodeString },
	"encodedText" : { "decode" : base64DecodeString, 
			  "encode" : base64EncodeString }
}

processInputChange = function(event) {
	// Get the element that triggered the change
	var inputElement = event.target
	var inputElementId = inputElement.id
	
	// Now get the list of elements that need to be updated
	var outputElements = [];
	for (var id in idToFunctionMapping) {
		if (id != inputElementId) {
			var outputElement = document.getElementById(id);
			outputElements.push(outputElement)
		}
	}

	// Get the string that was modified apply the decode function
	// to get the raw value
	var inputText = inputElement.value
	var mappedDecodeFunction = idToFunctionMapping[inputElementId]['decode']
	var decodedText = mappedDecodeFunction(inputText)

	// Now iterate over all the other text areas and apply the 
	// appropriate encoding to each one of them
	outputElements.forEach(function(element) {
		var outputElementId = element.id
		var mappedEncodeFunction = idToFunctionMapping[outputElementId]['encode']
		var encodedText = mappedEncodeFunction(decodedText)
		element.value = encodedText
	});

}

</script>

<div style="width:50%;float:left">
<p>Unencoded String</p>
<textarea rows="8" id="decodedText" style="width:100%;resize:none" onkeyup="processInputChange(event)" onchange="processInputChange(event)"></textarea>
</div>

<div style="width:50%;float:right">
<p>Base64 Encoded String</p>
<textarea rows="8" id="encodedText" style="width:100%;resize:none" onkeyup="processInputChange(event)" onchange="processInputChange(event)"></textarea>
</div>
