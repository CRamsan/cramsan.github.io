---
layout: page
title: Utilities
---

<script type="text/javascript" src="/public/js/resources/utilities.js"></script>
<script>

function noopEncodeString(inputString) {
	return inputString
}

var idToTextFunctionMapping = {
	"rawText" : { "encode" : noopEncodeString,
			  "decode" : noopEncodeString },
	"b64EncodedText" : { "decode" : base64DecodeString, 
			  "encode" : base64EncodeString },
	"urlEncodedText" : { "decode" : urlDecodeString, 
			  "encode" : urlEncodeString },
	"urlComponentEncodedText" : { "decode" : urlComponentDecodeString, 
			  "encode" : urlComponentEncodeString }
}

var idToDecFunctionMapping = {
	"decimalText" : { "decode" : decimalToBinary, 
			  "encode" : binaryToDecimal },
	"hexadecimalText" : { "decode" : hexToBinary, 
			  "encode" : binaryToHex },
	"binaryText" : { "decode" : noopEncodeString, 
			  "encode" : noopEncodeString }

}

linkElementsAndEvent = function(mapping, event) {
	for (var id in mapping) {
		var element = document.getElementById(id);
		element.addEventListener("keyup", event);
		element.addEventListener("change", event);
	}
}

processTextInputChange = function(event) {
	processInputChange(event, idToTextFunctionMapping);
}

processDecimalInputChange = function(event) {
	processInputChange(event, idToDecFunctionMapping);
}

processInputChange = function(event, mapping) {
	// Get the element that triggered the change
	var inputElement = event.target
	var inputElementId = inputElement.id
	
	// Now get the list of elements that need to be updated
	var outputElements = [];
	for (var id in mapping) {
		if (id != inputElementId) {
			var outputElement = document.getElementById(id);
			outputElements.push(outputElement)
		}
	}

	// Get the string that was modified apply the decode function
	// to get the raw value
	var inputText = inputElement.value
	var mappedDecodeFunction = mapping[inputElementId]['decode']
	var decodedText = mappedDecodeFunction(inputText)

	// Now iterate over all the other text areas and apply the 
	// appropriate encoding to each one of them
	outputElements.forEach(function(element) {
		var outputElementId = element.id
		var mappedEncodeFunction = mapping[outputElementId]['encode']
		var encodedText = mappedEncodeFunction(decodedText)
		element.value = encodedText
	});

}

function loadFunctions() {
	linkElementsAndEvent(idToTextFunctionMapping, processTextInputChange)
	linkElementsAndEvent(idToDecFunctionMapping, processDecimalInputChange)
}

window.onload = loadFunctions;
</script>

<h1>Text</h1>

<div style="width:50%;float:left">
<p>Raw String</p>
<textarea rows="8" id="rawText" style="width:100%;resize:none"></textarea>
</div>

<div style="width:50%;float:right">
<p>Base64 Encoded String</p>
<textarea rows="8" id="b64EncodedText" style="width:100%;resize:none"></textarea>
</div>

<div style="width:50%;float:right">
<p>URL Encoded String</p>
<textarea rows="8" id="urlEncodedText" style="width:100%;resize:none"></textarea>
</div>

<div style="width:50%;float:right">
<p>URL Component Encoded String</p>
<textarea rows="8" id="urlComponentEncodedText" style="width:100%;resize:none"></textarea>
</div>

<h1>Unsigned Integers</h1>

<div style="width:50%;float:left">
<p>Decimal</p>
<textarea rows="1" id="decimalText" style="width:100%;resize:none"></textarea>
</div>

<div style="width:50%;float:right">
<p>Hexadecimal</p>
<textarea rows="1" id="hexadecimalText" style="width:100%;resize:none"></textarea>
</div>

<div style="width:50%;float:right">
<p>Binary</p>
<textarea rows="1" id="binaryText" style="width:100%;resize:none"></textarea>
</div>
