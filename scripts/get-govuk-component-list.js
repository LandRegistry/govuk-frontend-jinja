const path = require('path');
const glob = require('glob');

function getGovukComponentList() {
  const govukComponentPath = path.join(
    path.dirname(require.resolve('govuk-frontend/package.json')),
    'govuk/components'
  );
  return glob
    .sync(path.join(govukComponentPath, '**/macro.njk'))
    .map((componentPath) =>
      path.relative(govukComponentPath, path.dirname(componentPath))
    );
}

module.exports = getGovukComponentList;
