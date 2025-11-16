function monthlySavings(payments, livingCost) {
    if (!Array.isArray(payments) || typeof livingCost !== "number") {
        return "invalid input";
    }
    
    let totalSavings = 0;
    for (let p of payments) {
        if (p >= 3000) {
            p = p - (p * 0.20);
        }
        totalSavings += p;
    }

    const finalAmount = totalSavings - livingCost;
    if (finalAmount < 0) {
        return "earn more";
    }
    return finalAmount;
}

console.log(monthlySavings(100, [900, 2700, 3400]));
