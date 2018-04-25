function memAlloc(banks) {
  	//code away :)
  	var allPreviousConfigs = [];
  	var counter = 0;

 	function addToPreviousConfigs(banks) {
		var currentConfig = "";		
		for (var i = 0; i < banks.length; i++) {
   			currentConfig = currentConfig + banks[i].toString();
   			console.log(currentConfig);
  		}
  		allPreviousConfigs.push(currentConfig);
  		console.log("allPreviousConfigs " + allPreviousConfigs);
  	}

  	function findHighestValue(banks) {
  		var highestValue = 0
  		var indexOfhighestMemBank = 0
  		for (var a = 0; a < banks.length; a++) {
  			if (highestValue < banks[a]) {
  				highestValue = banks[a];
  				indexOfhighestMemBank = a;
  			}
  			if (highestValue == banks[a]) {
  				console.log("Tie on index " + a + " and " + indexOfhighestMemBank);
  				continue;
  			}
  			console.log("Highest Value: " + highestValue);
  		}
  		return highestValue;
  	}

  	function redistributeHighestValue(banks) {
  		var indexOfMemBankToAddBlocksTo = indexOfhighestMemBank+1;
  		if (indexOfMemBankToAddBlocksTo > banks.length - 1) indexOfMemBankToAddBlocksTo = 0;
  		while (highestValue > 0) {
  			banks[indexOfMemBankToAddBlocksTo] = banks[indexOfMemBankToAddBlocksTo + 1];
  			indexOfMemBankToAddBlocksTo += 1;
  			highestValue -= 1;
  			console.log("banks: " + banks);
  		}
  		return banks;
  	}

  	function checkPreviousConfigs(banks) {
  		for (var z = 0; z < banks.length; z++) {
  			if (currentConfig == banks[z]) {
  				console.log("There is a match: " + currentconfig);
  			} 
  		}
  	}
  	
	addToPreviousConfigs(banks); 
  	

  	do {
  		//loop through banks to search highest value
  		//redistribute this value withing banks
  		//save new configuration of banks
  		//check if currentconfig is in previous configs
  		
  		findHighestValue(banks);

  		redistributeHighestValue(banks);
  		console.log("banks after redistribute: " + banks);

  		addToPreviousConfigs(banks);


  		counter += 1;
  	}
  	while(/*new configuration is not in allPreviousConfigs --> continue*/);


  return 0;
}



var banks = [0,2,7,0];
var result = memAlloc(banks);
console.log("result is " + result);