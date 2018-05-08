function memAlloc(banks) {
 
  	var allPreviousConfigs = [[0, 1]];
  	var highestValue;
  	var indexOfHighestValue;
	
	function findHighestValue(banks) {
  		highestValue = Math.max.apply(null, banks);
  		indexOfHighestValue = banks.indexOf(highestValue);
  	}

	function redistributeHighestValue(banks, highestValue, indexOfHighestValue) {
    
	      banks[indexOfHighestValue] = 0;
	      if (indexOfHighestValue == banks.length - 1) {
	        var indexOfNextElement = 0; 
	      } else {
	        var indexOfNextElement = indexOfHighestValue + 1;
	      }      
	      
	      while (highestValue > 0) {
	        banks[indexOfNextElement] = banks[indexOfNextElement] + 1;
	        if (indexOfNextElement == banks.length - 1) {
	          indexOfNextElement = 0;
	        } else {
	          indexOfNextElement += 1;  
	        }
	        highestValue -= 1;
	      }
	      return banks;
    }

    function checkPreviousConfigs (banks, allPreviousConfigs) {
    	// pseudokod:
    	// 1 szukaj pierwszej takiej samej liczy przez wszystkie stare configi.
    	// 2 jesli znajdziesz, przejdz i porownaj druga, trzecia, czwart etc.
    	// 3 jesli nie - szukaj nastepnej pierwszej liczby do konca
    	// 4 jesli znajdziesz znowu - krok
	  	var foundSameConfig = false;
	    var currentConfig = "";

    	for (var b = 0; b < allPreviousConfigs.length; b++) {
    		if (highestValue == allPreviousConfigs(b))  <++++++++++++++++++++++++++++++++++++++
    	}
    }

	/*function checkPreviousConfigs(banks, allPreviousConfigs) {
	  	var foundSameConfig = false;
	    var currentConfig = "";
	    
	    for (var i = 0; i < banks.length; i++) {
	        currentConfig = currentConfig + banks[i].toString() + "-";
	    }

		for (var z = 0; z < allPreviousConfigs.length; z++) {
			if (currentConfig == allPreviousConfigs[z]) {
		  		//console.log("There is a match: " + allPreviousConfigs[z]);
		  		foundSameConfig = true;
		  		break;
		  	}
		}
		addToPreviousConfigs(currentConfig, allPreviousConfigs);
		return foundSameConfig;
	}*/

	function addToPreviousConfigs (currentConfig, allPreviousConfigs) {
		allPreviousConfigs.push(currentConfig);
	}

	//************************************************
	//*                    START                     *
	//************************************************

	var counter = 0;
	var foundTheSameConfig = false;
	checkPreviousConfigs(banks, allPreviousConfigs);
  	
  	while (foundTheSameConfig == false) {  		
  		findHighestValue(banks);
  		redistributeHighestValue(banks, highestValue, indexOfHighestValue);
  		foundTheSameConfig = checkPreviousConfigs(banks, allPreviousConfigs);	
  		counter += 1;
  	}


  return counter;
}






// var banks = [0,2,7,0]; //result 5, OK;
// var banks = [5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 600] // 70 - OK                        time: 125627,473617510
// var banks = [53, 21, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 60];// 316 OK;
// var banks = [14, 21, 10, 0, 1, 7, 0, 14, 3, 12, 8, 10, 17, 12, 0, 19] // 826 OK;
// 
var banks = [5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 6] // 5042; wychodzi 1671 ?? SOLVED!! 
// label: 189.669ms // dla dwóch funkcji - 200.000 ms
// after Math.max usage - 250.000 ms



// var banks = [17, 17, 3, 5, 1, 10, 6, 2, 0, 12, 8, 11, 16, 2, 1, 6] // 158378 OK!!!!!!


console.time('label');
var result = memAlloc(banks);
console.log("result is " + result);
console.log("time: " + process.hrtime());
console.timeEnd('label');