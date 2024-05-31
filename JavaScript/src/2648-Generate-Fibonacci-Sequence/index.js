"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.fibGenerator = void 0;
function* fibGenerator() {
    let current = 0;
    let next = 1;
    while (true) {
        yield current;
        [current, next] = [next, current + next];
    }
}
exports.fibGenerator = fibGenerator;
