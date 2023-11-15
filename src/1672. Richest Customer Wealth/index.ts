// https://leetcode.com/problems/richest-customer-wealth/
export function maximumWealth(accounts: number[][]): number {
    let wealth: number = 0;
    let m: number = accounts.length;
    for (let i = 0; i < m; i++) {
        let wealthTemp: number = 0;
        for (let j = 0; j < accounts[i].length; j++) {
            wealthTemp += accounts[i][j];
        }
        if (wealthTemp > wealth) wealth = wealthTemp;
    }
    return wealth;
};