function checkPreviousConfigs(banks, allPreviousConfigs) {
  var checkTrue = false;
    //moving banks to String value (currentConfig)
    var currentConfig = "";   
    for (var i = 0; i < banks.length; i++) {
        currentConfig = currentConfig + banks[i].toString();
        console.log(currentConfig);
      }
      console.log("currentConfig " + currentConfig);

  //checking previous config has the same config
  for (var z = 0; z < allPreviousConfigs.length; z++) {
    if (currentConfig == allPreviousConfigs[z]) {
      console.log("There is a match: " + allPreviousConfigs[z]);
      checkTrue = true;
      break;
    } else { 
      console.log("No match: " + allPreviousConfigs[z]);
    }
  }
  return checkTrue;
}

var banks = [0,2,7,0];
allPreviousConfigs = ['1301', '2421', '1100', '3344', '0270', '6543'];

var x = checkPreviousConfigs(banks, allPreviousConfigs);
console.log("result: " + x);



