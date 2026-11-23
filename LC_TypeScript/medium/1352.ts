class ProductOfNumbers {
    products: number[] = [];

    constructor() {}

    add(num: number): void {
        if (num === 0) {
            this.products = [];
        } else if (this.products.length > 0) {
            this.products.push(this.products.at(-1)! * num);
        } else {
            this.products.push(num);
        }
    }

    getProduct(k: number): number {
        if (k > this.products.length) {
            return 0;
        } else if (k === this.products.length) {
            return this.products.at(-1)!;
        } else {
            return Math.floor(
                this.products.at(-1)! / this.products[this.products.length - k - 1]
            );
        }
    }
}
