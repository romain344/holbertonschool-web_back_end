export default class Building {
    constructor(sqft) {
        this._sqtf = sqft;
        if (typeof sqft !== 'number'){
            throw new TypeError('Sqft must be a number');
        }
        if (new.target === Building) {
            throw new Error('Building is an abstract class and cannot be instantiated directly');
        }
    }

    get sqft() {
        return this._sqtf;
    }
}