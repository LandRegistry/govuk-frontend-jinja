const exec = require('child_process').execFileSync;
const diffComponentAgainstReferenceNunjucks = require('./utils/govuk-frontend-diff');

diffComponentAgainstReferenceNunjucks(function (component, params) {
  const output = exec('./tests/utils/render.py', [
    '--component',
    component,
    '--params',
    JSON.stringify(params),
  ]);
  return output.toString('utf8');
});
