function handleEncoding (encodingBlock) 
{
	try {
		return encodingBlock();
	} catch (e) {
		console.log(e)
		return e.name + ":" + e.message;
	}

}

function base64EncodeString(inputString) {
	return handleEncoding(function(){
		return window.btoa(inputString);
	}) 
}

function base64DecodeString(inputString) {
	return handleEncoding(function(){
		return window.atob(inputString);
	}) 
}

function uppercaseEncodeString(inputString) {
	return handleEncoding(function(){
		return inputString.toUpperCase();
	}) 
}

function lowercaseEncodeString(inputString) {
	return handleEncoding(function(){
		return inputString.toLowerCase();
	}) 
}

function urlEncodeString(inputString) {
	return handleEncoding(function(){
		return encodeURI(inputString);
	}) 
}

function urlDecodeString(inputString) {
	return handleEncoding(function(){
		return decodeURI(inputString);
	}) 
}

function urlComponentEncodeString(inputString) {
	return handleEncoding(function(){
		return encodeURIComponent(inputString);
	}) 
}

function urlComponentDecodeString(inputString) {
	return handleEncoding(function(){
		return decodeURIComponent(inputString);
	}) 
}

function decimalToBinary(inputString) {
	return handleEncoding(function() {
		var decimal = parseInt(inputString, 10)
		var outputString = decimal.toString(2)
		return outputString
	})
}


function binaryToDecimal(inputString) {
	return handleEncoding(function() {
		var decimal = parseInt(inputString, 2)
		return decimal.toString(10)
	})
}

function hexToBinary(inputString) {
	return handleEncoding(function() {
		var decimal = parseInt(inputString, 16)
		return decimal.toString(2)
	})

}

function binaryToHex(inputString) {
	return handleEncoding(function() {
		var decimal = parseInt(inputString, 2)
		return decimal.toString(16)
	})

}

function binaryToSignedDecimal(inputString) {
	return handleEncoding(function() {
		if (inputString.length < 2)
			return "Value too short"
		// Extract the value after the first bit
		var binValue = inputString.substring(1);
		if (inputString.charAt(0) == '1') {
			// If the first character is 1, then thi will be a
			// negative number.
			var nBitsValue = Math.pow(2, binValue.length)
			var decimal = parseInt(binValue, 2)
			var twosComplement = nBitsValue - decimal;
			return (-1 * twosComplement).toString(10)
		} else {
			// If the first character is not 1, parse everything
			// afterwards as a regular integer
			return parseInt(binValue, 2).toString(10)
		}
	})
}

function signedDecimalToBinary(inputString) {
	return handleEncoding(function() {
		var signChar = inputString.charAt(0)
		var testSignChar = '-'
		if (signChar == testSignChar) {
			// Transform -3 to 3
			var decimal = parseInt(inputString.substring(1), 10)
			var nBitsValue = Math.pow(2, 32)
			var twosComplement = nBitsValue - decimal
			return twosComplement.toString(2)
		} else {
			var decimal = parseInt(inputString, 10)
			var outputString = "0" + decimal.toString(2)
			return outputString
		}
	})
}
