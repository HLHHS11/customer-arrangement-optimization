function combination (n, r, i = 0) {
    if (r > n/2) {  // ここ変える必要あり。帰ってくるイテレータがn-r個の組になってしまう
        r = n-r;
    }
    if (r===0) {
        return [];
    } else if (r===1) {
        let arrReturn = [];
        for (let j=i+1; j<=n-r+1; j++) {
            arrReturn.push([j]);
        }
        return arrReturn;
    } else {
        let arrReturn = [];
        for (let j=i+1; j<=n-r+1; j++) {
            //console.log(`j=${j}`)
            let tempArrReturn = combination(n, r-1, j); 
            for (let k=0; k<tempArrReturn.length; k++) {
                tempArrReturn[k].unshift(j);
            } 
            arrReturn = arrReturn.concat(tempArrReturn); 
        }
        return arrReturn;
    }
}

//const fs = require('fs');
let arrReturn = combination(6,2);
console.log(`arrReturn.length : ${arrReturn.length}`);
for (let nPos=0;nPos<arrReturn.length;nPos++) {
    console.log(arrReturn[nPos]);
    //fs.appendFileSync("output.txt",String(arrReturn[nPos])+"\n");
}