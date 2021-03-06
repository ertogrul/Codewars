function memAlloc(banks) {
  	/*
  	todo:
  	- polaczyc funkcje addtopreviousconfig i checkpreviousconfigs
  	- nadlużej schodzi na sprawdzaniu 'no match'; jak przyspieszyc funkcje check previous configs?
  	- sprawdz funkcje tie - 
  	- znalazlem blad - macierz previousconfigs moze miec rozne kongiruacje zapisane w ten sam sposob np. 1,11,3,4 i 11,1,3,4.
  	*/
  	var allPreviousConfigs = [];

 	function addToPreviousConfigs(banks) {
		var currentConfig = "";		
		for (var i = 0; i < banks.length; i++) {
   			currentConfig = currentConfig + banks[i].toString() + "-";
   			//console.log(currentConfig);
  		}
  		allPreviousConfigs.push(currentConfig);
  		//console.log("allPreviousConfigs " + allPreviousConfigs);
  	}


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
	      var indexOfNextElement;    
	      banks[indexOfHighestValue] = 0;
	      //console.log(banks[indexOfHighestValue]);
	      //console.log("aa: "+indexOfHighestValue);
	      //console.log("banks just before: " + banks);
	      if (indexOfHighestValue == banks.length - 1) {
	        indexOfNextElement = 0; 
	      } else {
	        indexOfNextElement = indexOfHighestValue + 1;
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


	function checkPreviousConfigs(banks, allPreviousConfigs) {
	  var checkTrue = false;
	    //moving banks to String value (currentConfig)
	    var currentConfig = "";   
	    for (var i = 0; i < banks.length; i++) {
	        currentConfig = currentConfig + banks[i].toString() + "-";
	        //console.log(currentConfig);
	      }
	      //console.log("currentConfig " + currentConfig);

	  //checking previous config has the same config
	  for (var z = 0; z < allPreviousConfigs.length; z++) {
	    if (currentConfig == allPreviousConfigs[z]) {
	      //console.log("There is a match: " + allPreviousConfigs[z]);
	      checkTrue = true;
	      break;
	    } //else { 
	    //  console.log("No match: " + allPreviousConfigs[z]);
	    //}
	  }
	  return checkTrue;
	}

	//************************************************
	//*                    START                     *
	//************************************************
  	
	addToPreviousConfigs(banks);

	var counter = 0;
	var theEnd = false;
  	while (theEnd == false) {  		
  		findHighestValue(banks);
  		redistributeHighestValue(banks, highestValue, indexOfHighestValue);
  		//console.log("banks after redistribute: " + banks);

  		theEnd = checkPreviousConfigs(banks, allPreviousConfigs);	
  		//console.log("theEnd " + theEnd);
  		//console.log("counter " + counter);

  		addToPreviousConfigs(banks);

  		counter += 1;
  	}


  return counter;
}



//var banks = [0,2,7,0]; //result 5, OK;
//var banks = [5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 600] // 70 - OK
//var banks = [53, 21, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 60];// 316 OK;
//var banks = [14, 21, 10, 0, 1, 7, 0, 14, 3, 12, 8, 10, 17, 12, 0, 19] // 826 OK;
var banks = [5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 6] // 5042; wychodzi 1671 ?? < --------- TU JEST PROBLEM
// label: 199.530ms

// var banks = [17, 17, 3, 5, 1, 10, 6, 2, 0, 12, 8, 11, 16, 2, 1, 6] // 158378 OK!!!!!!


console.time('label');
var result = memAlloc(banks);
console.log("result is " + result);
console.log("time: " + process.hrtime());
console.timeEnd('label');