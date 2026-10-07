// Cross-language evidence only; not EchoMap implementation.
import {createHash} from 'node:crypto';
import {readFileSync} from 'node:fs';
import assert from 'node:assert/strict';
const vectors=JSON.parse(readFileSync(new URL('./canonical-v1.json',import.meta.url),'utf8'));
const hash = text => createHash('sha256').update(text,'utf8').digest('hex');
// Python str.strip whitespace set, explicit because JS trim has different semantics.
const trimFrozen = text => text.replace(/^[\u0009-\u000d\u001c-\u0020\u0085\u00a0\u1680\u2000-\u200a\u2028\u2029\u202f\u205f\u3000]+|[\u0009-\u000d\u001c-\u0020\u0085\u00a0\u1680\u2000-\u200a\u2028\u2029\u202f\u205f\u3000]+$/gu,'');
const textNormalize = raw => trimFrozen(raw.replace(/\r\n?/g,'\n').replace(/^\uFEFF/u,''));
for(const v of vectors){
 assert.equal(textNormalize(v.raw_inputs.claim),v.normalized_inputs.claim);
 assert.equal(textNormalize(v.raw_inputs.context),v.normalized_inputs.context);
 const normalizedUrls=v.raw_inputs.urls.map(raw=>{
  const parsed=new URL(raw);
  return 'https://'+parsed.hostname.toLowerCase()+parsed.pathname;
 }).sort(); // These are prevalidated vector URLs; this is not a production URL validator.
 assert.deepEqual(normalizedUrls,v.normalized_inputs.urls);
 const request=JSON.stringify(['EIM-V1-STUDIO',v.creator.toLowerCase(),v.raw_inputs.client_key]);
 const payload=JSON.stringify(['EIM-V1-STUDIO',textNormalize(v.raw_inputs.claim),textNormalize(v.raw_inputs.context),normalizedUrls]);
 assert.equal(request,v.request_canonical_json);
 assert.equal(payload,v.payload_canonical_json);
 assert.equal(hash(request),v.request_id);
 assert.equal(hash(payload),v.payload_digest);
}
console.log(`${vectors.length} vectors verified using Node crypto / UTF-8 JSON`);
