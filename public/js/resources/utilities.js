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
		return decimal.toString(2)
	})
}


function binaryToDecimal(inputString) {
	return handleEncoding(function() {
		var binary = parseInt(inputString, 2)
		return binary.toString(10)
	})
}

function hexToBinary(inputString) {
	return handleEncoding(function() {
		var hex = parseInt(inputString, 16)
		return hex.toString(2)
	})

}

function binaryToHex(inputString) {
	return handleEncoding(function() {
		var binary = parseInt(inputString, 2)
		return binary.toString(16)
	})

}

function BEBinaryToLEBinary(inputString) {
	return handleEncoding(function() {
		return inputString
	}) 
}

function LEBinaryToBEBinary(inputString) {
	return handleEncoding(function() {
		return inputString
	})
}

