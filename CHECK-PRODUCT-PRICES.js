function priceCheck(products, productsPrices, productsSold, soldPrice) {
    let hash = {};
    let count = 0;
    for(let i=0; i < products.length; i++){
        if(!hash[products[i]]){
            hash[products[i]] = productsPrices[i]
        }
    }
    for(let j=0; j < productsSold.length; j++){
        if(hash[productsSold[j]] !== soldPrice[j]){
            count++;
        }
    }

    return count;
}
