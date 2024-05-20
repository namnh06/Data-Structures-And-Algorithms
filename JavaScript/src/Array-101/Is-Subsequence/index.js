"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.isSubsequence = void 0;
function isSubsequence(s, t) {
    const slen = s.length;
    const tlen = t.length;
    let i = 0;
    let j = 0;
    while (i < slen && j < tlen) {
        if (s[i] === t[j++]) {
            i++;
        }
    }
    return i === slen;
}
exports.isSubsequence = isSubsequence;
