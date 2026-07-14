const fs = require('fs');
const s = fs.readFileSync('index_final_sakura_curved_float.html', 'utf8');
const m = s.match(/<script>([\s\S]*?)<\/script>/);
if (!m) {
  console.log('NO_SCRIPT');
  process.exit(1);
}
try {
  new Function(m[1]);
  console.log('JS_OK');
} catch (e) {
  console.log('JS_ERROR: ' + e.message);
  process.exit(2);
}
