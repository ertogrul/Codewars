


var currentConfig = ["a", "b" , "c", "a", "e"];
var banks = 'zzzz';


var dict = []



for (var i = 0; i < 5; i++) {
	dict.push({
    key:   currentConfig[i],
    value: banks
	});

	console.log(dict)

}



/*
var maxi  = -1;
var indexOfMaxi = 0;

function findHighestValue(banks) {
  		maxi = Math.max.apply(null, banks);
  		indexOfMaxi = banks.indexOf(maxi);
  	}

var banks = [5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 6] // 5042;
findHighestValue(banks);
console.log(maxi);
console.log(indexOfMaxi);
*/


/*
function checkX(banks, allPreviousConfigs) {
	var configFound = false;   	    
	for (var z = 0; z < allPreviousConfigs.length; z++) {
		console.log(allPreviousConfigs[z]);
		var arr = allPreviousConfigs[z];
		console.log(arr[0]);
		
		
		
		if (banks[0] == arr[0]) {
			var checkArr = arr[z];
			console.log("There is a match: " + checkArr);
			for (var i = 1; i < banks.length; i++) {
				if (banks[i] == checkArr[i]) {
					console.log("Check");

				} else {
					configFound = false;
					break;
				}
			}
			configFound = true;
			console.log("There is a match: " , banks);
		}

  	}
}


banks = [0,2,7,0];
allPreviousConfigs = [[2, 1, 1, 0], [5, 6, 7, 7], [0, 2, 7, 0], [6, 5, 4, 3], [11, 98, 765, 3345]];


checkX(banks, allPreviousConfigs);
*/