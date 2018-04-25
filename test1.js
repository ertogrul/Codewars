function redistributeHighestValue(banks, HighestValue, IndexofHighestValue ) {
    var indexOfMemBankToAddBlocksTo = IndexofHighestValue+1;
    if (indexOfMemBankToAddBlocksTo > banks.length - 1) indexOfMemBankToAddBlocksTo = 0;
    while (highestValue > 0) {
      banks[indexOfMemBankToAddBlocksTo] = banks[indexOfMemBankToAddBlocksTo + 1];
      indexOfMemBankToAddBlocksTo += 1;
      highestValue -= 1;
      console.log("banks: " + banks);
    }
    return banks;
}

var arr = [0,2,7,0]; 
var HighestValue = 7; 
var IndexofHighestValue = 2; 
findHighestValue(arr, HighestValue, IndexofHighestValue);




