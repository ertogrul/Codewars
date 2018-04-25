var sum = 0;
function m35 (number){
	for (i = 0; i < number; i++) {
		if (i % 3 == 0) {
			sum = sum + i;

			console.log("%3");
			console.log("i= " + i);
			console.log("sum= " + sum);
		}
		if ((i % 5 == 0) && (i % 3 != 0)) {
			sum = sum + i;

			console.log("%3");
			console.log("i= " + i);
			console.log("sum= " + sum);
		}
	}
  	return sum;
}

var x = m35(0)
console.log("result: " + x);




/*
20
Expected 78, got 101 - Expected: 78, instead got: 101

200
Expected 9168, got 9269 - Expected: 9168, instead got: 9269
Completed in 4ms
 smallest cases

-1
Expected 0, got 9269 - Expected: 0, instead got: 9269

0
Expected 0, got 9269 - Expected: 0, instead got: 9269

1
Expected 0, got 9269 - Expected: 0, instead got: 9269

2
Expected 0, got 9269 - Expected: 0, instead got: 9269

3
Expected 0, got 9269 - Expected: 0, instead got: 9269

4
Expected 3, got 9272 - Expected: 3, instead got: 9272

5
Expected 3, got 9275 - Expected: 3, instead got: 9275

6
Expected 8, got 9283 - Expected: 8, instead got: 9283
 random cases


Expected 4185, got 13468 - Expected: 4185, instead got: 13468
Expected 5325, got 18793 - Expected: 5325, instead got: 18793
Expected 2625, got 21418 - Expected: 2625, instead got: 21418
Expected 5325, got 26743 - Expected: 5325, instead got: 26743
Expected 1673, got 28416 - Expected: 1673, instead got: 28416
Expected 78, got 28494 - Expected: 78, instead got: 28494
Expected 8204, got 36698 - Expected: 8204, instead got: 36698
Expected 753, got 37451 - Expected: 753, instead got: 37451
Expected 60, got 37511 - Expected: 60, instead got: 37511
Expected 2418, got 39929 - Expected: 2418, instead got: 39929




*/