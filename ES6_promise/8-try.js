export default function divideFunction(numerator, denominator) {
    return new Promise((resolve, reject) => {
        try {
            if (denominator === 0) {
                throw new Error('cannot divide by 0');
            }
            const result = numerator / denominator;
            resolve(result);
        } catch (error) {
            reject(error);
        }
    });
}