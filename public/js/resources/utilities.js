function base64EncodeString(inputString) {
	try {
		var encodedData = window.btoa(inputString);
		return encodedData;
	} catch (e) {
		console.log(e)
		if (e instanceof DOMException) {
			return "INVALID INPUT"
		} else {
			return "UNEXPECTED ERROR";
		}
	}
}

function base64DecodeString(inputString) {
	try {
		var encodedData = window.atob(inputString);
		return encodedData;
	} catch (e) {
		console.log(e)
		if (e instanceof DOMException) {
			return "INVALID INPUT"
		} else {
			return "UNEXPECTED ERROR";
		}
	}
}
