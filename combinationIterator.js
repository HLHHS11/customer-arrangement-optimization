function combination (n, r, i = 0) {
    if (r===1) {
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

let arrReturn = combination(6,3)
console.log(`arrReturn.length : ${arrReturn.length}`)
for (let nPos=0;nPos<arrReturn.length;nPos++) {
    console.log(arrReturn[nPos]);
}