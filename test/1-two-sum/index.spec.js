"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
const chai_1 = require("chai");
const _1_two_sum_1 = require("../../src/1-two-sum");
beforeEach(() => __awaiter(void 0, void 0, void 0, function* () {
}));
describe('Two Sum', () => {
    it('case: nums = [2, 7, 11, 15] - target = 9', () => {
        const result = _1_two_sum_1.twoSum.call(null, [2, 7, 11, 15], 9);
        chai_1.assert.deepEqual(result, [0, 1]);
    });
    it('case: nums = [3, 2, 4] - target = 6', () => {
        const result = _1_two_sum_1.twoSum.call(null, [3, 2, 4], 6);
        chai_1.assert.deepEqual(result, [1, 2]);
    });
    it('case: nums = [3, 3] - target = 6', () => {
        const result = _1_two_sum_1.twoSum.call(null, [3, 3], 6);
        chai_1.assert.deepEqual(result, [0, 1]);
    });
});
