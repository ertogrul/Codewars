function memAlloc(banks) {
  	/*
  	todo:
	- pomysl na przyspieszenie - allPrevious configs array of arrays of numbers.
	


  	- kod z funkcji addtopreviousconfig i checkpreviousconfigs powtarza sie; wyeliminowac to;
  	- nadlużej schodzi na sprawdzaniu 'no match'; jak przyspieszyc funkcje check previous configs?
  	- sprawdz funkcje tie - 
  	- znalazlem potencjalny blad - macierz previousconfigs moze miec rozne konfiguracje zapisane w ten sam sposob 
  	np. 1,11,3,4 == 11134
  	    11,1,3,4 == 11134

  	*/
  	var allPreviousConfigs = ['1'];
  	var highestValue;
  	var indexOfHighestValue;
	
	function findHighestValue(banks) {
  		highestValue = -1
  		indexOfHighestValue = 0
  		for (var a = 0; a < banks.length; a++) {
  			if (highestValue == banks[a]) {
          		//console.log("Tie on index " + a + " and " + indexOfHighestValue);
          		continue;
        	}
        	if (highestValue < banks[a]) {
  				highestValue = banks[a];
  				indexOfHighestValue = a;
  				//console.log("Highest Value: " + highestValue);
  			}	  			
  			
  		}
	  	//return highestValue;
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
	          //console.log ("loop");
	          indexOfNextElement = 0;
	        } else {
	          indexOfNextElement += 1;  
	        }
	        highestValue -= 1;
	        //console.log("banks: " + banks)
	      }
	      return banks;
    }

    //MOZE ZROBIC ODDZIELNĄ FUNKCJĘ ADD TO PREV CONFIGS? CZY TAKA FUNKCJA ZAMIAST LINII allPreviousConfigs.push BARDZ OPOZNI PROGRAM? SPRAWDZ TO.

	function checkPreviousConfigs(banks, allPreviousConfigs) {
	  	var checkTrue = false;
	    var currentConfig = "";   
	    
	    for (var i = 0; i < banks.length; i++) {
	        currentConfig = currentConfig + banks[i].toString() + "-";
	    }

		for (var z = 0; z < allPreviousConfigs.length; z++) {
			if (currentConfig == allPreviousConfigs[z]) {
		  		//console.log("There is a match: " + allPreviousConfigs[z]);
		  		checkTrue = true;
		  		break;
		  	}
		}
		allPreviousConfigs.push(currentConfig);
		return checkTrue;
	}

	//************************************************
	//*                    START                     *
	//************************************************


	var counter = 0;
	var theEnd = false;
	checkPreviousConfigs(banks, allPreviousConfigs);
  	while (theEnd == false) {  		
  		//addToPreviousConfigs(banks);
  		findHighestValue(banks);
  		redistributeHighestValue(banks, highestValue, indexOfHighestValue);
  		//console.log("banks after redistribute: " + banks);

  		theEnd = checkPreviousConfigs(banks, allPreviousConfigs);	
  		//console.log("theEnd " + theEnd);
  		//console.log("counter " + counter);
  		counter += 1;
  	}


  return counter;
}






// var banks = [0,2,7,0]; //result 5, OK;
// var banks = [5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 600] // 70 - OK                        time: 125627,473617510
// var banks = [53, 21, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 60];// 316 OK;
// var banks = [14, 21, 10, 0, 1, 7, 0, 14, 3, 12, 8, 10, 17, 12, 0, 19] // 826 OK;
// 
var banks = [5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 6] // 5042; 
// label: 189.669ms // dla dwóch funkcji - 200.000 ms

// var banks = [17, 17, 3, 5, 1, 10, 6, 2, 0, 12, 8, 11, 16, 2, 1, 6] // 158378 OK!!!!!!


console.time('label');
var result = memAlloc(banks);
console.log("result is " + result);
console.log("time: " + process.hrtime());
console.timeEnd('label');