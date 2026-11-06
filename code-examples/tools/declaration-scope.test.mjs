import test from 'node:test';
import assert from 'node:assert/strict';
import {enclosingObjCScope} from './declaration-scope.mjs';
test('global after closed category has no enclosing class',()=>{
  assert.equal(enclosingObjCScope(['@interface Object (Category)','- (void)action;','@end','extern int value;'],4),null);
});
test('member inside category retains exact enclosing line',()=>{
  assert.equal(enclosingObjCScope(['@interface Object (Category)','- (void)action;'],2).line,1);
});
test('forward protocol is not an opened scope',()=>{
  assert.equal(enclosingObjCScope(['@protocol Other;','extern int value;'],2),null);
});
test('open protocol and whitespace are accepted',()=>{
  assert.equal(enclosingObjCScope(['  @protocol Other','- (void)action;'],2).line,1);
});
test('commented example cannot create a declaration scope',()=>{
  assert.equal(enclosingObjCScope(['/*','@interface Example','*/','extern int value;'],4),null);
});
