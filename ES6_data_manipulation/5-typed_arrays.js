function createInt8TypedArray() {
    if (position < 0 || position >= length) {
        throw new Error('Position outside range')
    }
    const buffer = new ArrayBuffer(length);
    const view = new DataView(buffer);
    view.setInt8(position, value);
    return view;
}