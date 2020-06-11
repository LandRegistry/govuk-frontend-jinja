const diffComponentAgainstReferenceNunjucks = require('./utils/govuk-frontend-diff');
const examples = require('../.cache/govuk-frontend-examples/header.json');

diffComponentAgainstReferenceNunjucks('header', examples);