<script type="text/javascript" src="/public/js/resources/utilities.js"></script>
<script>
function noopEncodeString(inputString) {
	return inputString
}

var ValueToEncodingFunctionMapping = [{
	"title" : "Text",
	"mapping" : [{ "label" : "Raw Text",
			"id" : "rawText",
			"encode" : noopEncodeString,
			"decode" : noopEncodeString },
		{ "label" : "Base64 Encoded",
			"id" : "b64Encoded",
			"decode" : base64DecodeString, 
			"encode" : base64EncodeString },
		{ "label" : "URL Encoded",
			"id" : "urlEncoded",
			"decode" : urlDecodeString, 
			"encode" : urlEncodeString },
		{ "label" : "URL Component Encoded",
			"id" : "urlComponentEncoded",
			"decode" : urlComponentDecodeString, 
			"encode" : urlComponentEncodeString },
		{ "label" : "Lower Case",
			"id" : "lowercase",
			"decode" : noopEncodeString,
			"encode" : lowercaseEncodeString },
		{ "label" : "Upper Case",
			"id" : "uppercase",
			"decode" : noopEncodeString,
			"encode" : uppercaseEncodeString }]
},{
	"title" : "Binary",
	"mapping" : [{ "label" : "Binary",
			"id" : "binary",
			"rows" : 1,
			"decode" : noopEncodeString, 
			"encode" : noopEncodeString },
		{ "label" : "Hexadecimal",
			"id" : "hexadecimal",
			"rows" : 1,
			"decode" : hexToBinary, 
			"encode" : binaryToHex },
		{ "label" : "Unsigned Decimal",
			"id" : "decimal",
			"rows" : 1,
			"decode" : decimalToBinary, 
			"encode" : binaryToDecimal },
		{ "label" : "Signed Decimal(32 bits)",
			"id" : "sdecimal",
			"rows" : 1,
			"decode" : signedDecimalToBinary,
			"encode" : binaryToSignedDecimal}]
}]

processInputChange = function(event, mapping) {
	// Get the element that triggered the change
	var inputElement = event.target
	var inputElementId = inputElement.id
	
	// Now get the list of elements that need to be updated
	var outputElements = [];
	var mappedDecodeFunction;
	mapping.forEach(function(map) {
		var id = map["id"]
		if (id != inputElementId) {
			var outputElement = document.getElementById(id);
			outputElements.push({"element" : outputElement, "decodeFunction" : map["encode"]})
		} else {
			mappedDecodeFunction = map['decode']
		}
	})

	// Get the string that was modified apply the decode function
	// to get the raw value
	var inputText = inputElement.value
	var decodedText = mappedDecodeFunction(inputText)

	// Now iterate over all the other text areas and apply the 
	// appropriate encoding to each one of them
	outputElements.forEach(function(element) {
		var outputElementId = element.element.id
		var mappedEncodeFunction = element.decodeFunction
		var encodedText = mappedEncodeFunction(decodedText)
		element.element.value = encodedText
	});
}

function loadFunctions() {
	var mainContainer = document.getElementById("divContainer")
	ValueToEncodingFunctionMapping.forEach(function(dict) {
		var sectionTitle = dict["title"]
		var mappingArray = dict["mapping"]
		var title = document.createElement("h1")
		title.innerHTML = sectionTitle
		mainContainer.appendChild(title)

		sectionFunc = function(event) {
			processInputChange(event, mappingArray)
		}

		var contentContainer = document.createElement("div");
		contentContainer.classList.add('utilContainerDiv');
		mappingArray.forEach(function(section) {
			var div = document.createElement("div");
			div.classList.add('utilInputContainer');
			var sectionLabel = section["label"]
	
			var label = document.createElement("p")
			label.classList.add('utilInputLabel')
			label.innerHTML = sectionLabel
			div.appendChild(label)

			var textArea = document.createElement("textArea")
			textArea.classList.add('utilInputText');
			textArea.rows = 4
			textArea.id = section["id"]
			textArea.addEventListener("keyup", sectionFunc);
			textArea.addEventListener("change", sectionFunc);
			textArea.addEventListener("keydown", function(event){
				if(event.keyCode == 13)
				{ return false; }
				else
				{ return true; }
			});
			
			var rowCount = section["rows"]
			if (rowCount !== undefined) {
				textArea.rows = rowCount
			}

			div.appendChild(textArea)
			contentContainer.appendChild(div);
		})
		mainContainer.appendChild(contentContainer)
		mainContainer.appendChild(document.createElement("hr"))
	})
}

window.onload = loadFunctions;
</script>

<form>
  <div id="divContainer">
  </div>
</form>

