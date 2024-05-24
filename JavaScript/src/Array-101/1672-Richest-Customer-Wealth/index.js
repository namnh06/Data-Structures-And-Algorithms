"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.maximumWealth = void 0;
// https://leetcode.com/problems/richest-customer-wealth/
function maximumWealth(accounts) {
    let wealth = 0;
    let m = accounts.length;
    for (let i = 0; i < m; i++) {
        let wealthTemp = 0;
        for (let j = 0; j < accounts[i].length; j++) {
            wealthTemp += accounts[i][j];
        }
        if (wealthTemp > wealth)
            wealth = wealthTemp;
    }
    return wealth;
}
exports.maximumWealth = maximumWealth;
;
