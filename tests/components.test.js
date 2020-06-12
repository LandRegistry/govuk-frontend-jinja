const diffComponentAgainstReferenceNunjucks = require('./utils/govuk-frontend-diff');
const exec = require('child_process').execFileSync;

diffComponentAgainstReferenceNunjucks(function(component, params) {
    const output = exec('./tests/utils/render.py', ['--component', component, '--params', JSON.stringify(params)]);
    return output.toString('utf8');
});